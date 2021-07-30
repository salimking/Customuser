from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser,Adminuser,Customer



admin.site.register(Customer)
admin.site.register(CustomUser)

admin.site.register(Adminuser)

