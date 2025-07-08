from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .models import Event
from .forms import BookingForm
from django.conf import settings

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def events(request):
    dict_eve = {
        'eve': Event.objects.all()
    }
    return render(request, 'events.html', dict_eve)

def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()

            # ✅ Send confirmation email
            send_mail(
                subject='Event Booking Confirmation',
                message=f"Dear {booking.cus_name},\n\nYour booking for the event '{booking.name.name}' on {booking.booking_data} has been confirmed.",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[booking.cus_email],
                fail_silently=True,
            )

            # ✅ Show popup
            messages.success(request, "Booking confirmed! Confirmation email sent.")
            return redirect('/booking')

    form = BookingForm()
    dict_form = {
        'form': form
    }
    return render(request, 'booking.html', dict_form)

def contact(request):
    return render(request, 'contact.html')
