
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class CustomUser(AbstractUser):
    ac_type=((1,'Admin'),(2,'User'))
    u_t=models.CharField(max_length=50,choices=ac_type,default=1)
   


class Adminuser(models.Model):
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE,primary_key=True)  
    password=models.CharField(max_length=50)
    USERNAME_FIELD='username'

class Customer(models.Model):
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE,primary_key=True)
    password=models.CharField(max_length=50)

    USERNAME_FIELD='username'
    def __str__(self) :
        return self.user.u_t

@receiver(post_save,sender=CustomUser)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        if instance.u_t==1:
            Adminuser.objects.create(user=instance)
        if instance.u_t==2:
            Customer.objects.create(user=instance)


@receiver(post_save,sender=CustomUser)
def save_user_profile(sender,instance,**kwargs):
    if instance.u_t==1:
        instance.adminuser.save()
    if instance.u_t==2:
        instance.customer.save()


