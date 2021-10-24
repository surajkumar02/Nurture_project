from django.db import models
from django.utils import timezone

# Create your models here.

class Advisor(models.Model):
    advisor_id=models.AutoField(primary_key=True)
    advisor_name=models.CharField(max_length=100,unique=True)
    advisor_photo=models.FileField(upload_to='users/advisor_pics/',null=True,blank=True)
    advisor_photo_url=models.URLField()

    def __str__(self):
        return self.advisor_name

class User(models.Model):
    id=models.AutoField(primary_key=True)
    user_name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=50)

    def __str__(self):
        return self.user_name

class Booking(models.Model):
    booking_id=models.AutoField(primary_key=True)
    advisor=models.ForeignKey(Advisor,on_delete=models.CASCADE)
    booking_time=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.advisor.advisor_name