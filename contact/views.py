from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render
from django.http import HttpResponse


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Customer Query"
            body = {
                'name': form.cleaned_data['name'],
                'email_address': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'codeinstitutestudent1@gmail.com',
                          ['codeinstitutestudent1@gmail.com'])
                return render(request, "contact/contact_confirmation.html",
                              {'form': form})
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return render(request, "products/products.html", {'form': form})

    form = ContactForm()
    return render(request, "contact/contact.html", {'form': form})
