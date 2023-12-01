from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from user.models import UserProfile
from datetime import datetime

def validate_file_extension(value):
   import os
   from django.core.exceptions import ValidationError
   ext = os.path.splitext(value.name)[1]
   valid_extensions = ['.jpg', '.png']
   if not ext.lower() in valid_extensions:
      raise  ValidationError('ساپورت نمیشه این فایل.')
    
class Home(models.Model):
    
    HOME_TYPE = (
      ('فروش','فروش'),
      ('رهن و اجاره','رهن و اجاره'),
    )

    title = models.CharField(max_length=128, null=False, blank=False)
    cover = models.ImageField(upload_to='files/property_cover/home', null=True, blank=True)
    description = models.CharField(max_length=512, null=False, blank=False)
    meterage = models.IntegerField(null=False, blank=False)
    constructedDate = models.IntegerField(null=False, blank=False)
    address = models.CharField(max_length=256, null=True, blank=True)
    rooms = models.IntegerField(null=False, blank=False)
    homeType = models.CharField(max_length=60, null=True, blank=True, choices=HOME_TYPE)
    attributes = models.ManyToManyField('HomeAttributes', null=True, blank=True, related_name='attributes')

    ## if type == sell
    price = models.IntegerField(null=True, blank=True)
    pricePerMeter = models.IntegerField(null=True, blank=True)

    ## if type == rent
    mortgage = models.IntegerField(null=True, blank=True)
    rent = models.IntegerField(null=True, blank=True)

    createdAt = models.DateTimeField(default=datetime.now, blank=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    ownersPhone = models.CharField(max_length=11)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    score = models.IntegerField(default=0, validators=[
      MaxValueValidator(5),
      MinValueValidator(0)
    ])

    def __str__(self):
      return self.title

class Car(models.Model):
    
    title = models.CharField(max_length=128, null=False, blank=False)
    cover = models.ImageField(upload_to='files/property_cover/car', null=True, blank=True)
    description = models.CharField(max_length=512, null=False, blank=False)
    color = models.CharField(max_length=128, null=True, blank=True)
    address = models.CharField(max_length=256, null=True, blank=True)
    dateModel = models.IntegerField(null=True, blank=True)
    brand = models.CharField(max_length=128, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    motorStation = models.CharField(max_length=128, null=True, blank=True)
    gearbox = models.CharField(max_length=128, null=True, blank=True)
    operation = models.IntegerField(null=True, blank=True)
    createdAt = models.DateTimeField(default=datetime.now, blank=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    attributes = models.ManyToManyField('CarAttributes', null=True, blank=True, related_name='attributes')
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    ownersPhone = models.CharField(max_length=11)
    score = models.IntegerField(default=0, validators=[
      MaxValueValidator(5),
      MinValueValidator(0)
    ])

    def __str__(self):
      return self.title

class Other(models.Model):
    
    title = models.CharField(max_length=128, null=False, blank=False)
    cover = models.ImageField(upload_to='files/property_cover/other', null=True, blank=True)
    address = models.CharField(max_length=256, null=True, blank=True)
    description = models.CharField(max_length=512, null=False, blank=False)
    createdAt = models.DateTimeField(default=datetime.now, blank=False)
    price = models.IntegerField(null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    ownersPhone = models.CharField(max_length=11)
    score = models.IntegerField(default=0, validators=[
      MaxValueValidator(5),
      MinValueValidator(0)
    ])

    def __str__(self):
        return self.title

class Category(models.Model):
   title = models.CharField(max_length=30, null=False, blank=False)

   def __str__(self):
      return self.title
   
class HomeAttributes(models.Model):
    title = models.CharField(max_length=156)

    def __str__(self):
        return self.title
    
class CarAttributes(models.Model):
    title = models.CharField(max_length=156)

    def __str__(self):
        return self.title