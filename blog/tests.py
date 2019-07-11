from django.test import TestCase
from .models import Post

# Create your tests here.
class BlogTests(TestCase):
    """ Tests for the Ticket model """
    
    # Set up test database and register a blog post
    def setUp(self):
        Post.objects.create(title="Example Blog Post",
                        content="This is the blog content",
                        tag='Test').save()
                        
    # Ensure created post renders on page load
    def test_blog_post_render(self):
        response = self.client.get('/blog/')
        self.assertIn(b'<h6>Example Blog Post</h6>', response.content)