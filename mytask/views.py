from django.shortcuts import render
from django.core.mail import EmailMessage

def index(request):
    context={}
    return render(request, 'index.html', context)

def send_email(request):
    subject = request.POST.get('subject')
    body = request.POST.get('body')
    sender = request.POST.get('sender')
    email = EmailMessage(subject, body, to=[sender])
    email.send()