# utility meaning

import random

import string

from twilio.rest import Client

from decouple import config

from django.template.loader import render_to_string

from django.core.mail import EmailMultiAlternatives

def generate_password():

    password = ''.join(random.choices(string.ascii_letters+string.digits,k=8))

    return password

def generate_otp():

    otp = ''.join(random.choices(string.digits,k=4))

    return otp

def send_otp(phone_num,otp):
   
    account_sid = config('TWILIO_ACCOUNT_SID')
    auth_token = config('TWILIO_AUTH_TOKEN')
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    from_=config('TWILIO_NUMBER'),
    to=config('MY_NUMBER'),
    body= f'OTP For Verification : {otp}'
    # body is the parameter..nthann msg ayeeitt poovandath ath type cheyannum
    )


def send_email(recipient,template,subject,context):
    #   recipient --- eth mail annu ayakande
    # template --- icons,images vech annu mail ayee varunne..otp mail..by using html
    # subject -- mail ulla subject
    # context -- nthakkillum html pageill koduvarn

     sender = config('EMAIL_HOST_USER')

     content = render_to_string(template,context)
    #  render to string used to convert html to txt

     msg = EmailMultiAlternatives(from_email=sender,to=[recipient],subject=subject)
    #  email direct cheyan pettilla....html should be convert to text 

     msg.attach_alternative(content,'text/html')

     msg.send()
    
