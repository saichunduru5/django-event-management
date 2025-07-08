from django import forms
from .models import Booking

class DateInput(forms.DateInput):
    input_type = 'date'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

        widgets = {
            'booking_data': DateInput(),
        }

        labels = {
            'cus_name': "Customer Name:",
            'cus_email': "Email:",
            'cus_ph': "Customer Phone:",
            'name': "Event Name:",
            'booking_data': "Booking Date:",
        }
