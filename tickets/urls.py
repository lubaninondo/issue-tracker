from django.conf.urls import url
from .views import all_tickets, upvote, ticket_detail, create_bug, create_feature_request, edit_ticket, upvote_payment, change_status_in_progress, change_status_complete, change_status_backlog, delete_ticket

urlpatterns = [
    url(r'^$', all_tickets, name='index'),
    url(r'^(?P<sort>\w+)$', all_tickets, name='sort'),
    url(r'^upvote/bug/(?P<pk>\d+)$', upvote, name='upvote'),
    url(r'^upvote/feature-request/(?P<pk>\d+)$', upvote_payment, name='upvote_payment'),
    url(r'^(?P<pk>\d+)/$', ticket_detail, name='ticket_detail'),
    url(r'^create/bug$', create_bug, name='create_bug'),
    url(r'^create/feature-request$', create_feature_request, name='create_feature_request'),
    url(r'^edit/(?P<pk>\d+)$', edit_ticket, name='edit_ticket'),
    url(r'^delete/(?P<pk>\d+)$', delete_ticket, name='delete_ticket'),
    url(r'^change-status/backlog/(?P<pk>\d+)$', change_status_backlog, name='backlog'),
    url(r'^change-status/in-progress/(?P<pk>\d+)$', change_status_in_progress, name='in_progress'),
    url(r'^change-status/complete/(?P<pk>\d+)$', change_status_complete, name='complete'),
]
