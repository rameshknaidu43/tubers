from django.shortcuts import redirect, render
from .models import Contactus
from django.contrib import messages

# Create your views here.

def contactus(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        phone = request.POST['phone']
        emails = request.POST['emails']
        company_name = request.POST['company_name']
        subject = request.POST['subject']
        message = request.POST['message']



        contactus = Contactus(full_name=full_name, phone=phone, emails=emails, company_name=company_name, subject=subject, message=message)
        contactus.save()
        messages.success(request, 'Thanks for contacting us!')
        return redirect('home')

