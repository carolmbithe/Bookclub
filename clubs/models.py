from django.db import models
import datetime as dt


# Create your models here.

class Role(models.Model):

    name=models.CharField(max_length =50)

class People(models.Model):
    fullnames=models.CharField(max_length =50,blank=True)
    phone=models.IntegerField(null=True)
    email = models.EmailField(blank=True)
    photo=models.ImageField(upload_to='people/',blank=True)
    id_number=models.IntegerField(null=True)
    postal_address=models.CharField(max_length =100,null=True)
    city=models.CharField(max_length =30,blank=True)
    dob=models.DateTimeField(null=True)
    Role_id=models.ForeignKey(Role,on_delete=models.CASCADE,null=True)
    subcription=models.CharField(max_length=50)

    

class Club(models.Model):
    name=models.CharField(max_length =30)
    manager_id=models.ForeignKey(People,on_delete=models.CASCADE,null=True)
    creation_date=models.DateTimeField(auto_now_add=True)


class Venue(models.Model):
    name=models.CharField(max_length =30)
    min_number=models.IntegerField(null=True)
    max_number=models.IntegerField()
    cost_per_person=models.IntegerField(null=True)
    cost_per_sitting=models.IntegerField(null=True)



class Book(models.Model):
    title=models.CharField(max_length =30)
#     author
#     isbn
#     date_published
#     cover_photo
#     cost
#     selling_price
#     quantity=models.IntegerField(blank=True,null=True)
#     book_location=models.ForeignKey(Club)
#     status
#     payment_reference=
#
#
# class BookSales
#     book
#     amount
#     customer
#     seller
#     date

class Event(models.Model):
    club=models.ForeignKey(Club,on_delete=models.CASCADE,null=True)
    date=models.DateTimeField(auto_now_add=True)
    # start_time
    # end_time
    venue=models.ForeignKey(Venue,on_delete=models.CASCADE,null=True)


class Volunteer(models.Model):
    person=models.ForeignKey(People,on_delete=models.CASCADE,null=True)
    event=models.ForeignKey(Event,on_delete=models.CASCADE,null=True)

class Attendance(models.Model):

    People=models.PositiveIntegerField()
    Events=models.ForeignKey(Event,on_delete=models.CASCADE,null=True)
    times=models.IntegerField(blank=True,null=True)

class PaymentType(models.Model):
    type=models.CharField(max_length=100)
    amount=models.IntegerField()



class Payment(models.Model):
    person=models.ForeignKey(People,on_delete=models.CASCADE,null=True)
    receiving=models.ForeignKey(Role,on_delete=models.CASCADE,null=True)
    club=models.ForeignKey(Club,on_delete=models.CASCADE,null=True)
    amount=models.IntegerField(blank=True,null=True)
    payment_type=models.ForeignKey(PaymentType,on_delete=models.CASCADE,null=True)


class Subscription(models.Model):
    subcription_type=models.CharField(max_length=100)
    amount=models.IntegerField(blank=True,null=True)
    number_days=models.IntegerField(blank=True,null=True)


class PeopleSubcription(models.Model):
    person=models.ForeignKey(People,on_delete=models.CASCADE,null=True)
    subcription=models.ForeignKey(Subscription,on_delete=models.CASCADE,null=True)
    start_date=models.DateTimeField(null=True)
    end_date=models.DateTimeField(null=True)
