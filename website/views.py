from django.shortcuts import render, redirect
from .forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

# /
def welcome(request):
    context = {}
    return render(request, 'website/welcome.html', context)

# /about
def about_page(request):
    context = {}
    return render(request, 'website/about.html', context)

# /contact
def contact_page(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            app_email = settings.DEFAULT_FROM_EMAIL
            your_email = form.cleaned_data["your_email"]
            message = your_email+'<br>'+form.cleaned_data['message']
            try:
                send_mail(subject, message,app_email,[app_email])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect("success")
    return render(request, 'website/contact.html', {"form": form})

# /success
def success(request):
    context = {}
    return render(request, 'website/success.html', context)
