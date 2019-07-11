from django.shortcuts import render
from tickets.models import Ticket



def get_charts(request):
    total_bugs = Ticket.objects.filter(ticket_type='Bug').count()
    total_feature_requests = Ticket.objects.filter(ticket_type='Feature Request').count()
    user = request.user
    user_bugs = Ticket.objects.filter(ticket_type='Bug', creator=user).count()
    user_feature_requests = Ticket.objects.filter(ticket_type='Feature Request', creator=user).count()
    open_bugs = Ticket.objects.filter(ticket_type='Bug', status='Backlog').count()
    in_progress_bugs = Ticket.objects.filter(ticket_type='Bug', status='In Progress').count()
    completed_bugs = Ticket.objects.filter(ticket_type='Bug', status='Complete').count()
    open_feature_requests = Ticket.objects.filter(ticket_type='Feature Request', status='Backlog').count()
    in_progress_feature_requests = Ticket.objects.filter(ticket_type='Feature Request', status='In Progress').count()
    completed_feature_requests = Ticket.objects.filter(ticket_type='Feature Request', status='Complete').count()
    highest_voted_bug = Ticket.objects.filter(ticket_type='Bug').exclude(status='Complete').order_by('-upvotes').first()
    highest_voted_feature_request = Ticket.objects.filter(ticket_type='Feature Request').exclude(status='Complete').order_by('-upvotes').first()
    
    return render(request, 'charts.html', {'total_bugs': total_bugs, 
                                            'total_feature_requests': total_feature_requests,
                                            'user': user,
                                            'user_bugs': user_bugs,
                                            'user_feature_requests': user_feature_requests,
                                            'open_bugs': open_bugs,
                                            'in_progress_bugs': in_progress_bugs,
                                            'completed_bugs': completed_bugs,
                                            'open_feature_requests': open_feature_requests,
                                            'in_progress_feature_requests': in_progress_feature_requests,
                                            'completed_feature_requests': completed_feature_requests,
                                            'highest_voted_bug': highest_voted_bug,
                                            'highest_voted_feature_request': highest_voted_feature_request
    })