from django.contrib import admin
from .models import Bunk, User, Bunkform
# Register your models here.
admin.site.register(Bunkform)
admin.site.register(Bunk)
admin.site.register(User)
