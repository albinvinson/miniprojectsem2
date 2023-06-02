from django.db import models
from django.contrib.auth.models import User

# class Salon(models.Model):
#     name = models.CharField(max_length=255)
#     address = models.CharField(max_length=255)
#     phone_number = models.CharField(max_length=20)
#     created_by = models.ForeignKey(User, on_delete=models.CASCADE)

# class Service(models.Model):
#     name = models.CharField(max_length=255)
#     price = models.DecimalField(max_digits=8, decimal_places=2)
#     duration = models.PositiveIntegerField(help_text="Duration of service in minutes")

# class Appointment(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     salon = models.ForeignKey(Salon, on_delete=models.CASCADE)
#     service = models.ForeignKey(Service, on_delete=models.CASCADE)
#     appointment_time = models.DateTimeField()

class UserDetail(models.Model):
    uname=models.CharField(max_length=90)
    phone=models.CharField(max_length=25)
    email=models.CharField(max_length=25)
    passwd=models.CharField(max_length=25)


class Booking(models.Model):
    user = models.ForeignKey(UserDetail, on_delete=models.CASCADE)
    phone=models.CharField(max_length=25)
    gender=models.CharField(max_length=25)
    appointment_time = models.TimeField()
    date=models.DateField()

    def __str__(self):
        f=f"{self.user.uname} booked on {self.date}"
        return f





