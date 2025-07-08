from django.db import models

# Create your models here.
class Event(models.Model):
    img=models.ImageField(upload_to="pic")
    name=models.CharField(max_length=50)
    desc=models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    combo_offer_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)


    def __str__(self):
        return self.name

class Booking(models.Model):
    cus_name=models.CharField(max_length=55)
    cus_email = models.EmailField(max_length=255)
    cus_ph=models.CharField(max_length=55)
    name=models.ForeignKey(Event,on_delete=models.CASCADE)
    booking_data=models.DateField()
    booked_on=models.DateField(auto_now=True)