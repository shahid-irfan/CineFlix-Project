from django.db import models

from django.contrib.auth.models import AbstractUser
# abstract userill ellam field vannu athinn namal import aakiye

from movies.models import BaseClass
# otp class create cheythapol; base annu vilikkunne

# Create your models here.

class RoleChoices(models.TextChoices):

    USER = 'User','User'
    
    ADMIN = 'Admin','Admin'

class Profile(AbstractUser):
    
    role = models.CharField(max_length=10,choices=RoleChoices.choices)

    phone  = models.CharField(null=True,blank=True)
    # null turue and blank true is given when namak ath pinned cheyan vandi annu (phoneno namal login cheythitt annu kodukkunne)
    # model create cheyumbol namal ath fill cheyilla..pinned cheyumbol annu namal kodukkunne

    phone_verified = models.BooleanField(default=False)
    class Meta:

        verbose_name = 'profiles'
    
        verbose_name_plural = 'profiles'

    def __str__(self):

        return f'{self.username}'
    
class OTP(BaseClass):

    profile = models.OneToOneField('Profile',on_delete=models.CASCADE)

    otp = models.CharField(max_length=4)

    email_otp = models.CharField(max_length=4)

    email_otp_verified = models.BooleanField(default=False)

    class Meta:

        verbose_name = 'OTPs'
    
        verbose_name_plural = 'OTPs'

    def __str__(self):

        return f'{self.profile.username} otp'
    

    
    


    
