from django.db import models
from django.db.models.fields import related
from accounts.models import CustomUser


# Create your models here.
class Train(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(50)

    def __str__(self):
        return self.name

class Station(models.Model):
    name = models.CharField(100)

    def __str__(self):
        return self.name

class TicketClass(models.Model):
    name = models.CharField(100)
    def __str__(self):
        return self.name


class Ticket(models.Model):
    train = models.ForeignKey(Train, on_delete=models.CASCADE, related_name="train_tickets")
    to_station = models.ForeignKey(Station, on_delete='to')
    from_station = models.ForeignKey(Station, on_delete='form')
    arival_time = models.DateTimeField(auto_now=True)
    deperture_time = models.DateTimeField(auto_now=True)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    ticket_class = models.ForeignKey(TicketClass, on_delete=models.CASCADE, related_name="tickets")
    seat_no = models.IntegerField(blank=True, null=True)
    price = models.IntegerField()
    price_bangla_text = models.TextField()
    available_qualtity = models.IntegerField(default=0)



class TicketPurchase(models.Model):
    purchase_station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='ticketpurchases')
    seller = models.ForeignKey(CustomUser, blank=True, null=True, on_delete=models.SET_NULL, related_name='ticket_sheller')
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name='ticket_buyer' )
    ticket = models.ForeignKey()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    payment_procedure = models.CharField(blank=True, null=True) 
    trxID = models.CharField(blank=True, null=True)



