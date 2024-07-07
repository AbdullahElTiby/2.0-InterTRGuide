from django.contrib import admin
from .models import CustomUser,Category,Place,Description

# Register your models here.

admin.site.register(CustomUser),
admin.site.register(Place),
admin.site.register(Category),
admin.site.register(Description),

