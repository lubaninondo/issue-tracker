from django.test import TestCase
from .models import Ticket

# Create your tests here.
class TicketTests(TestCase):
    """ Tests for the Ticket model """
    
    # Setting up test database and logging test user in before executing tests
    def setUp(self):
        Ticket.objects.create(title="Example bug",
                        summary="This is a test summary for a bug",
                        ticket_type='Bug',
                        creator='ticket_tester',
                        category='Test Category'
                    ).save()
        Ticket.objects.create(title="Test Feature Request",
                                    summary="This is a test feature request that I would like to suggest",
                                    ticket_type='Feature Request',
                                    creator='ticket_tester',
                                    category='Test Category'
                                ).save()
        self.client.post('/accounts/register/', {'email': 'ticket_test_email@test.com',
                                                'username': 'ticket_tester',
                                                'first_name': 'Tester',
                                                'last_name': 'McTestface',
                                                'password1': 'testing123',
                                                'password2': 'testing123'})
    
    # Ensure created tickets render on all tickets page
    def test_bug_rendered(self):
        response = self.client.get('/tickets/')
        self.assertIn(b'<h6 class="ticket-title">EXAMPLE BUG</h6>', response.content)
        self.assertIn(b'<h6 class="ticket-title">TEST FEATURE REQUEST</h6>', response.content)
        
    # Ensure upvoting bug increments upvotes by 1
    def test_bug_upvote_loads(self):
        ticket = Ticket.objects.filter(title="Example bug")[0]
        upvotes = ticket.upvotes
        self.assertEqual(upvotes, 0)
        self.client.get('/tickets/upvote/bug/{0}'.format(ticket.pk), follow=True)
        new_upvotes = Ticket.objects.filter(title="Example bug")[0].upvotes
        self.assertEqual(new_upvotes, 1)
        
    # Ensure user taken to payment form when upvoting feature request
    def test_feature_request_rendered(self):
        ticket = Ticket.objects.filter(title="Test Feature Request")[0]
        response = self.client.get('/tickets/upvote/feature-request/{0}'.format(ticket.pk), follow=True)
        self.assertIn(b'<h1>UPVOTE FEATURE REQUEST</h1>', response.content)
        
    # Ensure ticket detail page renders correctly
    def test_detail_rendered(self):
        ticket = Ticket.objects.filter(title="Test Feature Request")[0]
        response = self.client.get('/tickets/{0}/'.format(ticket.pk), follow=True)
        self.assertIn(b'<span><i class="fas fa-calendar-alt fa-lg page-icon"></i>CREATED DATE</span>', response.content)
        self.assertIn(b'<span><i class="fas fa-plus fa-lg page-icon"></i>ADD COMMENT</span>', response.content)
        
    # Ensure user can create a bug
    def test_bug_creation(self):
        self.client.post('/tickets/create/bug', {'title': 'Another bug',
                        'summary': 'Another test summary for a bug',
                        'ticket_type': 'Bug',
                        'creator': 'ticket_tester',
                        'category': 'Test Category'})
        ticket = Ticket.objects.filter(title="Another bug")[0]
        self.assertEqual("Another bug", ticket.title)
        
    # Ensure edit bug page renders correctly
    def test_edit_bug_rendered(self):
        ticket = Ticket.objects.filter(title="Example bug")[0]
        response = self.client.get('/tickets/edit/{0}'.format(ticket.pk), follow=True)
        self.assertIn(b'<h1>EDIT BUG</h1>', response.content)
        
    # Ensure feature request page renders correctly
    def test_edit_feature_request_rendered(self):
        ticket = Ticket.objects.filter(title="Test Feature Request")[0]
        response = self.client.get('/tickets/edit/{0}'.format(ticket.pk), follow=True)
        self.assertIn(b'<h1>EDIT FEATURE REQUEST</h1>', response.content)
        
    # Ensure editing bug saves new data
    def test_bug_edit_saves(self):
        ticket = Ticket.objects.filter(summary="This is a test summary for a bug")[0]
        self.assertEqual(ticket.title, "Example bug")
        self.client.post('/tickets/edit/{0}'.format(ticket.pk), data={
            'title': 'New Bug Title',
            'summary': 'This is a test summary for a bug',
            'ticket_type': 'Bug',
            'creator': 'ticket_tester',
            'category': 'Test Category'
        }, follow=True)
        new_title = Ticket.objects.filter(summary="This is a test summary for a bug")[0].title
        self.assertEqual(new_title, "New Bug Title")
        
    # Ensure editing feature request saves new data
    def test_feature_request_edit_saves(self):
        ticket = Ticket.objects.filter(summary="This is a test feature request that I would like to suggest")[0]
        self.assertEqual(ticket.title, "Test Feature Request")
        self.client.post('/tickets/edit/{0}'.format(ticket.pk), data={
            'title': 'Feature Request 2',
            'summary': 'This is a test feature request that I would like to suggest',
            'ticket_type': 'Feature Request',
            'creator': 'ticket_tester',
            'category': 'Test Category'
        }, follow=True)
        new_title = Ticket.objects.filter(summary="This is a test feature request that I would like to suggest")[0].title
        self.assertEqual(new_title, "Feature Request 2")
        
    # Ensure in progress status change registered
    def test_status_change_in_progress(self):
        Ticket.objects.create(title="Backlog Status Bug",
                        summary="Dummy text",
                        ticket_type='Bug',
                        creator='ticket_tester',
                        category='Test Category'
                    ).save()
        ticket = Ticket.objects.filter(title="Backlog Status Bug")[0]
        self.assertEqual(ticket.status, "Backlog")
        self.client.get('/tickets/change-status/in-progress/{0}'.format(ticket.pk), follow=True)
        new_ticket_status = Ticket.objects.filter(title="Backlog Status Bug")[0].status
        self.assertEqual(new_ticket_status, 'In Progress')
        
        
    # Ensure complete status change registered
    def test_status_change_complete(self):
        Ticket.objects.create(title="In Progress Bug",
                        summary="Dummy text",
                        status="In Progress",
                        ticket_type='Bug',
                        creator='ticket_tester',
                        category='Test Category'
                    ).save()
        ticket = Ticket.objects.filter(title="In Progress Bug")[0]
        self.assertEqual(ticket.status, "In Progress")
        self.client.get('/tickets/change-status/complete/{0}'.format(ticket.pk), follow=True)
        new_ticket_status = Ticket.objects.filter(title="In Progress Bug")[0].status
        self.assertEqual(new_ticket_status, 'Complete')
        
        
    # Ensure delete of bug functions correctly
    def test_bug_delete(self):
        Ticket.objects.create(title="Bug To Delete",
                        summary="This bug will be deleted",
                        status="In Progress",
                        ticket_type='Bug',
                        creator='ticket_tester',
                        category='Test Category'
                    ).save()
        ticket = Ticket.objects.filter(summary="This bug will be deleted")[0]
        ticket_count = Ticket.objects.filter(summary="This bug will be deleted").count()
        self.assertEqual(ticket_count, 1)
        self.client.get('/tickets/delete/{0}'.format(ticket.pk), follow=True)
        deleted_ticket = Ticket.objects.filter(title="Bug To Delete").count()
        self.assertEqual(deleted_ticket, 0)
        
        
    # Ensure delete of feature request functions correctly
    def test_feature_request_delete(self):
        Ticket.objects.create(title="Feature Request To Delete",
                        summary="This feature request will be deleted",
                        ticket_type='Feature Request',
                        creator='ticket_tester',
                        category='Test Category'
                    ).save()
        ticket = Ticket.objects.filter(summary="This feature request will be deleted")[0]
        ticket_count = Ticket.objects.filter(summary="This feature request will be deleted").count()
        self.assertEqual(ticket_count, 1)
        self.client.get('/tickets/delete/{0}'.format(ticket.pk), follow=True)
        deleted_ticket = Ticket.objects.filter(title="Feature Request To Delete").count()
        self.assertEqual(deleted_ticket, 0)