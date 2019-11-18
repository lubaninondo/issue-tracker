from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.contrib import messages
from django.utils import timezone
from django.conf import settings
from .models import Ticket
from .forms import TicketForm, PaymentForm
import stripe

stripe.api_key = settings.STRIPE_SECRET

# Create your views here.
def all_tickets(request, sort=None):
    if sort == 'bugs':
        tickets = Ticket.objects.filter(ticket_type='Bug')
    elif sort =='feature_requests':
        tickets = Ticket.objects.filter(ticket_type='Feature Request')
    else:
        tickets = Ticket.objects.all()
    return render(request, 'index.html', {'tickets': tickets})


@login_required
def upvote(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    ticket.upvotes += 1
    ticket.save()
    messages.error(request, "Upvote recorded!")
    return redirect(ticket_detail, ticket.pk)

@login_required
def upvote_payment(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)

    if request.method=="POST":
        payment_form = PaymentForm(request.POST)
        if payment_form.is_valid():
            try:
                print(payment_form['stripe_id'])
                customer = stripe.Charge.create(amount = 500,
                                                currency = "eur",
                                                description = request.user.email,
                                                card = payment_form.cleaned_data['stripe_id'],
                                                )
                if customer.paid:
                    messages.error(request, "Your payment was successful")
                    new_total = float(ticket.total_paid) + (customer.amount/100)
                    ticket.total_paid = new_total
                    ticket.save()
                    return redirect(upvote, ticket.id)

                else:
                    messages.error(request, "Unable to take payment")
                    print(payment_form.errors)

            except:
                messages.error(request, "Your card was declined")

        else:

            messages.error(request, "We were unable to take payment with that card")

    else:
        payment_form = PaymentForm()

    return render(request, "upvote-payment.html", {'ticket': ticket, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE})


def ticket_detail(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)


    return render(request, 'ticket-detail.html', {'ticket': ticket})


@login_required
def create_bug(request):
    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = Ticket(title=form.cleaned_data['title'],
                            summary=form.cleaned_data['summary'],
                            ticket_type='Bug', 
                            creator=request.user,
                            initiation_date=timezone.now())
            ticket.save()
            return redirect(ticket_detail, ticket.pk)
    else:
        form = TicketForm()
    return render(request, 'create-bug.html', {'form': form})


@login_required
def create_feature_request(request):
    if request.method=="POST":
        ticket_form = TicketForm(request.POST, request.FILES)
        payment_form = PaymentForm(request.POST)

        if ticket_form.is_valid() and payment_form.is_valid():
            ticket = Ticket(title=ticket_form.cleaned_data['title'],
                                summary=ticket_form.cleaned_data['summary'],
                                ticket_type='Feature Request',
                                creator=request.user,
                                initiation_date=timezone.now())
            ticket.save()
            try:
                customer = stripe.Charge.create(amount = 3000,
                                                currency = "eur",
                                                description = request.user.email,
                                                card = payment_form.cleaned_data['stripe_id'],
                                                )
            except:
                messages.error(request, "Your card was declined")

                if customer.paid:
                    messages.error(request, "Your payment was successful")
                    return redirect(ticket_detail, ticket.id)

            else:
                     messages.error(request, "Your payment was successful")
                     return redirect(ticket_detail, ticket.id)
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take payment with that card")

    else:
        ticket_form = TicketForm()
        payment_form = PaymentForm()

    return render(request, "create-feature-request.html", {'ticket_form': ticket_form,
                                            'payment_form': payment_form,
                                            'publishable': settings.STRIPE_PUBLISHABLE})


@login_required
def edit_ticket(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk) if pk else None
    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES, instance=ticket)
        if form.is_valid():
            ticket.title = form.cleaned_data['title']
            ticket.summary = form.cleaned_data['summary']
            ticket.save()
            return redirect(ticket_detail, ticket.pk)
    else:
        form = TicketForm(instance=ticket)
        html_page = 'edit-bug.html' if ticket.ticket_type == 'Bug' else 'edit-feature-request.html'
    return render(request, html_page, {'form': form})


@login_required
def delete_ticket(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    ticket.delete()
    return redirect(reverse('index'))


@login_required
def change_status_backlog(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    if ticket.completion_date:
        ticket.completion_date = None
    ticket.status = 'Backlog'
    ticket.save()
    return redirect(ticket_detail, ticket.id)


@login_required
def change_status_in_progress(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    if ticket.completion_date:
        ticket.completion_date = None
    ticket.status = 'In Progress'
    ticket.save()
    return redirect(ticket_detail, ticket.id)

@login_required
def change_status_complete(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)

    subject = "Unicorn Attractor - Ticket #" + str(ticket.id)
    from_email, to = 'lubaninondo@yahoo.com', request.user.email
    html_content = "<p>Hi " + ticket.creator + "</p><p>You raised the below ticket on our website:</p><p><strong>TYPE:</strong> " + ticket.ticket_type + "</p><p><strong>TITLE:</strong> " + ticket.title + "</p><p>This email is to let you know this ticket has been completed. Thanks again for raising your issue.</p><p>Many thanks,</p><p>The Unicorn Attractor Team</p>"
    msg = EmailMessage(subject, html_content, from_email, [to])
    msg.content_subtype = "html"
    msg.send()

    ticket.status = 'Complete'
    ticket.completion_date = timezone.now()
    ticket.save()
    return redirect(ticket_detail, ticket.id)