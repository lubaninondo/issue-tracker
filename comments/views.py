from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from tickets.models import Ticket
from tickets.views import ticket_detail, all_tickets
from .forms import CommentForm
from .models import Comment

# Create your views here.
@login_required
def create_comment(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES, instance=ticket)
        if form.is_valid():
            comment = Comment(ticket=ticket,
                                user=request.user,
                                comment=form.cleaned_data['comment'],
                                comment_date=timezone.now())
            comment.save()
            return redirect(ticket_detail, ticket.pk)
    else:
        form = CommentForm(instance=ticket)
    return redirect(all_tickets)