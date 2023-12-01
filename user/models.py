from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

def validate_phone(value):
    if not value.isdigit():
        raise ValidationError('شماره موبایل وارد شده عدد نیست')
    elif len(value) > 11:
        raise ValidationError('شماره موبایل وارد شده بیش از 11 رقم است')
    elif len(value) < 11:
        raise ValidationError('شماره موبایل وارد شده کمتر از 11 رقم است')

class UserProfile(AbstractUser):
    
	phone_number = models.CharField(max_length=110, unique=True, null=True, blank=True,validators=[validate_phone], error_messages={
			"unique": ("این شماره موبایل از قبل در سیستم ثبت شده است")
	})
	profile_image = models.ImageField(upload_to='profile_image', null=True, blank=True)
	email = models.EmailField(unique=True, error_messages={"unique": ("این ایمیل از قبل در سیستم ثبت شده است")})
	
	def __str__(self):
			return self.username