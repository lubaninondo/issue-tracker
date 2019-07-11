from django.test import TestCase
from django.contrib.auth.models import User

# Create your tests here.
class AccountsTests(TestCase):
    
    # Setting up user before executing tests
    def setUp(self):
        self.client.post('/accounts/register/', {'email': 'ticket_test_email2@test.com',
                                                'username': 'ticket_tester2',
                                                'first_name': 'Tester2',
                                                'last_name': 'McTestface2',
                                                'password1': 'testing123',
                                                'password2': 'testing123'})
    
    # Ensure new user can register successfully
    def test_new_user_registered(self):
        user = User.objects.filter(username="ticket_tester2")[0]
        self.assertEqual(user.email, 'ticket_test_email2@test.com')
        
    # Ensure profile page renders correctly
    def test_profile_rendered(self):
        response = self.client.get('/accounts/profile/')
        self.assertIn(b'<span><i class="fas fa-user-circle fa-lg page-icon"></i>USERNAME</span>', response.content)
        self.assertIn(b'ticket_tester2', response.content)
        
    # Ensure user logs out correctly
    def test_user_log_out(self):
        response = self.client.get('/accounts/logout/', follow=True)
        self.assertIn(b'You have successfully been logged out!', response.content)
        