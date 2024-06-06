from django.contrib import admin
from .models import *


# Register your models here.

admin.site.register(reader)
admin.site.register(Book)
admin.site.register(BookInstance)



