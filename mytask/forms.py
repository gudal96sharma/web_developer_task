from django import forms

class ContactForm(forms.Form):
    NAME = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'id': 'fullname',}))
	EMAIL = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'id': 'email',}))
	MESSAGE = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'id': 'message',}))
	