from django.contrib import admin
from .models import Student, Building, Room, Key

# Register your models here.
admin.site.register(Student)
admin.site.register(Building)
admin.site.register(Room)
admin.site.register(Key)
