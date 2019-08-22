from django import forms
from .models import Ticket

class TicketForm(forms.ModelForm):
   title = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'TITLE'}))
   summary = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'SUMMARY'}))
 
class Meta:
        model = Ticket
        fields = ['title', 'summary', 'completion_date']
        
        
class PaymentForm(forms.Form):
    MONTH_CHOICES = [(i, i) for i in range(1, 13)]
    YEAR_CHOICES = [(i, i) for i in range(2019, 2036)]
    
    # required field set to False for security purposes (Stripe handles encryption of credit card details)
    credit_card_number = forms.CharField(label="Credit Card Number", required=False)
    cvv = forms.CharField(label="Security Code (CVV)", required=False)
    expiry_month = forms.ChoiceField(label="Month", choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label="Year", choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)