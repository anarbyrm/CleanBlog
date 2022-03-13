from pyexpat.errors import messages
from django.shortcuts import redirect, render
from .forms import ContactForm
from django.contrib import messages

def emailView(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            form.save()
            messages.success(request, 'Your message has been successfully received!')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


