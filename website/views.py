from django.shortcuts import render, redirect
from .forms import ContactForm
from django.conf import settings
from django.core.mail import BadHeaderError
from django.core.mail import EmailMessage
from django.http import HttpResponse
from smtplib import SMTPDataError
from django.http import HttpResponseServerError

import logging

logger = logging.getLogger(__name__)

# /
def welcome(request):
    context = {}
    return render(request, 'website/welcome.html', context)

# /resume
def resume_page(request):
    context = {}
    return render(request, 'website/resume.html', context)

# /links
def links_page(request):
    context = {}
    return render(request, 'website/links.html', context)

# /apps
def apps_page(request):
    context = {}
    return render(request, 'website/apps.html', context)

# /contact
def contact_page(request):
    context = {}
    if request.method == "GET":
        form = ContactForm()
        context['form']=form
    else:
        form = ContactForm(request.POST)
        context['form']=form
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            app_email = settings.DEFAULT_FROM_EMAIL
            your_email = form.cleaned_data["your_email"]
            message = your_email+'\n'+form.cleaned_data['message']
            email = EmailMessage(
                subject=subject,
                body=message,
                to=[app_email],
                reply_to=[your_email],
                headers={'Content-Type': 'text/plain'},
            )
            try:
                email.send()
            except BadHeaderError:
                logger.error("Invalid header found.")
                return HttpResponseServerError("Internal Server Error")
            except SMTPDataError:
                logger.error("The SMTP server didn't accept the data.")
                return HttpResponseServerError("Internal Server Error")
            except Exception as e:
                # Code to handle the exception
                logger.error("An exception occurred:", type(e).__name__)
                logger.error("Exception message:", e)
                return HttpResponseServerError("Internal Server Error")
            return render(request, 'website/success.html',{})
        else:
            return render(request, 'website/contact.html#contact-partial', context)
    return render(request, 'website/contact.html', context)

# /success
def success(request):
    context = {}
    return render(request, 'website/success.html', context)
