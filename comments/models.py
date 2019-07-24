from django.db import models
from tickets.models import Ticket
from django.utils import timezone

# Create your models here.
class Comment(models.Model):
    
   # ticket = models.ForeignKey(Ticket, null=False)
    ticket=models.ForeignKey(on_delete=models.CASCADE, to='tickets.Ticket', null=False),
    author = models.CharField(max_length=150, blank=False)
    comment = models.TextField(blank=False)
    comment_date = models.DateTimeField(blank=False, null=False, default=timezone.now)
    
    def __str__(self):
        return "Comment {0} by {1} (Ticket {2})".format(self.id, self.author, self.ticket.title)
    