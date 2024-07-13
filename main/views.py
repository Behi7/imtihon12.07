from django.shortcuts import render, redirect
from . import models

def index(request):
    homes = models.Home.objects.all()
    services = models.Our_service.objects.all()
    teams = models.Our_team.objects.all()
    workings = models.Working_hours.objects.last()
    testimonials = models.Testemonial.objects.all()
    
    context = {
        'homes': homes,
        'services': services,
        'teams': teams,
        'workings': workings,
        'testemonials': testimonials,
    }
    return render(request, 'index.html', context)

def contact(request):
    if request.method == 'POST':
        models.Contact_us.objects.create(
            name = request.POST['Ism'],
            phone = request.POST['Telefon'],
            subject = request.POST['Mavzu'],
            message = request.POST['Xabar']
        )
    return redirect('index.html')

def see(request):
    contacts = models.Contact_us.objects.all()
    context = {
        'contacts': contacts
    }
    return render(request, 'see.html', context)


# def contact_us(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             # Create a new Contact_us instance and save the data
#             contact = Contact_us(
#                 name=form.cleaned_data['name'],
#                 phone=form.cleaned_data['phone'],
#                 subject=form.cleaned_data['subject'],
#                 message=form.cleaned_data['message']
#             )
#             contact.save()
#             # You can add logic here to send an email notification or perform other actions
#             return redirect('contact_us_success')  # Redirect to a success page
#     else:
#         form = ContactForm()
#     return render(request, 'contact.html', {'form': form})
