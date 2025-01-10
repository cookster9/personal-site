from django.shortcuts import render, redirect
from .forms import ContactForm
from django.conf import settings
from django.core.mail import BadHeaderError
from django.core.mail import EmailMessage
from django.http import HttpResponse
from smtplib import SMTPDataError

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
            message = your_email+'<br>'+form.cleaned_data['message']
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
                return HttpResponse("Invalid header found.")
            except SMTPDataError:
                return HttpResponse("The SMTP server didn't accept the data")
            except Exception as e:
                # Code to handle the exception
                print("An exception occurred:", type(e).__name__)
                print("Exception message:", e)
            return render(request, 'website/success.html',{})
        else:
            return render(request, 'website/contact.html#contact-partial', context)
    return render(request, 'website/contact.html', context)

# /success
def success(request):
    context = {}
    return render(request, 'website/success.html', context)
