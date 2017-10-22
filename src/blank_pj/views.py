from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .forms import ContactForm

# Write your code here

def home(request):
    context = {
        'title': 'Hello world!',
        'content': 'Welcome to home page'
    }
    return render(request, 'home.html', context)

def about(request):
    context = {
        "title":"About Page",
        "content":" Welcome to the about page."
    }
    return render(request, "home.html", context)

def contact(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title":"Contact",
        "content":" Welcome to the contact page.",
        "form": contact_form,
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
        if request.is_ajax():
            return JsonResponse({"message": "Thank you for your submission"})

    if contact_form.errors:
        errors = contact_form.errors.as_json()
        if request.is_ajax():
            return HttpResponse(errors, status=400, content_type='application/json')

    return render(request, 'contact.html', context)