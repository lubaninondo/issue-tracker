from django.db import models
from tickets.models import Ticket
from django.utils import timezone

# Create your models here.
class Comment(models.Model):
    
   # ticket = models.ForeignKey(Ticket, null=False),
    ticket=models.ForeignKey(on_delete=models.CASCADE, to='Ticket'),
    user = models.CharField(max_length=150, blank=False)
    comment = models.TextField(max_length=1500)
    comment_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.ticket