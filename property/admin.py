from django.contrib import admin
from .models import *

admin.site.register(Home)
admin.site.register(Car)
admin.site.register(Other)
admin.site.register(Category)
admin.site.register(HomeAttributes)
admin.site.register(CarAttributes)