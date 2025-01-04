from django import forms

class ContactForm(forms.Form):
    your_email = forms.EmailField(
        label="Your Email",
        widget=forms.EmailInput(attrs={
            'class': 'form-input p-1 block w-full rounded-md border border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50',
            'placeholder': 'Enter your email address',
        })
    )
    subject = forms.CharField(
        label="Subject",
        widget=forms.TextInput(attrs={
            'class': 'form-input p-1 block w-full rounded-md border border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50',
            'placeholder': 'Enter the subject',
        })
    )
    message = forms.CharField(
        label="Message",
        widget=forms.Textarea(attrs={
            'class': 'form-textarea p-1 block w-full rounded-md border border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50',
            'placeholder': 'Write your message here',
            'rows': 4,
        })
    )
