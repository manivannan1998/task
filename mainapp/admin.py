from django.contrib import admin
from .models import Register
from .models import student
from .models import mark

# Register your models here.
admin.site.register(Register)
admin.site.register(student)
admin.site.register(mark)