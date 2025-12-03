from django.shortcuts import render,redirect

# Create your views here.

from django.views import View

from .forms import LoginForm,SignUpForm,AddPhoneForm,OTPForm,ChangePasswordForm
# form class context through frontill knoduvarna vendi annu


from django.contrib.auth import authenticate,login,logout
# authenticate 2types...aa ullath  and authenticate
#  this is called for authentication and login functions..lastill details und

from django.contrib.auth.hashers import make_password
# admin and vere oru profile signup cheyumbol admin password #tagsill ayeeirilkum..ath matti namude 'admin' password idan annu use
# cheyunne

from cineflix.utils import generate_password,generate_otp,send_otp,send_email
# utils cheyththah vilikkunnath

from .models import OTP

from django.utils import timezone

import threading
# multithreading async aakann vendi annu ith use cheyunne
# at a time multiple process run cheyyan pattum

from django.contrib.auth.decorators import login_required
# login required is a decorator fn or class behaviour change cheyukka...without modifying code
# permission kodukkan vendi annu.. profile view chumma url type cheythal kittum..ath mattan vendi annu

# decorator....@ function decorator
# class based viewill decorator namaku direct class based used cheyan petilla...

from django.utils.decorators import method_decorator
# fun based annkill direct apply aakam...athinn annu naamaal  method_decorator use cheyune
# normal decorator classill apply cheyan method decorator use vennom


from  .permissions import permitted_user_roles
# from permissions.py fileil ninnu import cheythath


class LoginView(View):

    template = 'authentication/login.html'

    form_class = LoginForm

    def get(self,request,*args,**kwargs):

        form = self.form_class()

        data = {'form':form}

        return render(request,self.template,context=data)
    
    def post(self,request,*args,**kwargs):

        form = self.form_class(request.POST)

        error = None

        if form.is_valid():

            # print(form.cleaned_data)
            #cleaned data is an attribute

            email = form.cleaned_data.get('email')

            password = form.cleaned_data.get('password')

            user = authenticate(username=email,password=password)

            # 2 function-----"authenicate" . email and passwaord user modelill/record undo enn check cheyannum
#  aa record return cheyum  undakill.....illakill none ayeeirikum varunne.
# user undo enn check cheyam ?  if user

# ---'login fun'----usernne login cheyunne function anne

            if user:

                login(request,user)

                return redirect('home')
                #import redirect

            # for invalid user and pasword
            error = 'Invalid username or password'
             

        data = {'form':form,'error':error}

        return render(request,self.template,context=data)
    
    
@method_decorator(login_required(login_url='login'),name='dispatch') 
    #ith default aayi classil apply cheyyum...classil ella methodinum apply cheyyum
    # login url enn kodukkunnath login pageilekku redirect cheyyan vendi
       
class LogoutView(View):

    def get(self,request,*args,**kwargs):

        logout(request)

        return redirect('home')
    
class SignUpView(View):

    template = 'authentication/signup.html'

    form_class = SignUpForm

    def get(self,request,*args,**kwargs):

        form = self.form_class()
        # html pageill konduvaran vendi annu 

        data = {'page':'Sign Up','form':form}

        return render(request,self.template,context=data)
    
    #data recieve cheyan vendi post method
    def post(self,request,*args,**kwargs):

        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)
            # variable = object aaki vechu

            user.username = user.email

            password = generate_password()

            user.password = make_password(password)
            # forminn class wrk cheyunne polle annu wrk aakunne..appo athin mention cheyan vendi annu makepass using

            user.role ='User'

            user.save()

            recipient = user.email

            template = 'emails/logincredential.html'

            subject = 'Cineflix : login credentials'

            context = {'user':f'{user.first_name} {user.last_name}','username':user.email,'password':password}
            # hi shahid irfan angane render cheyan annu use cheyunne

            # send_email(recipient,template,subject,context)
            # ee code comment cheythath multithreading aakann vendi annu

            thread =threading.Thread(target=send_email,args=(recipient,template,subject,context))

            thread.start()

            return redirect('login')
        
        data ={'form':form}

        return render(request,self.template,context=data)
    

@method_decorator(permitted_user_roles('user'),name='dispatch')   
# login parameter namal login enn kodukkum

class ProfileView(View):

    template = 'authentication/profile.html'

    def get(self,request,*args,**kwargs):

        return render(request,self.template)
    
@method_decorator(login_required(login_url='login'),name='dispatch') 
    
class AddPhoneView(View):

    template = 'authentication/phone.html'

    form_class = AddPhoneForm

    def get(self,request,*args,**kwargs):

        form = self.form_class()

        data = {'form':form}
        # key value pair ayeeitt

        return render (request,self.template,context=data)
    
    def post(self,request,*args,**kwargs):

        form = self.form_class(request.POST)

        if form.is_valid():

            phone = form.cleaned_data.get('phone')
            # cleaned data used for phone number kittan

            request.session['phone']=phone
            # phone number valid annakill db eduth vekkan
            
            
            return redirect('verify-otp')
        
        data = {'form':form}

        return render(request,self.template,context=data)
    
@method_decorator(permitted_user_roles('user'),name='dispatch')   

class VerifyOTPView(View):

    template = 'authentication/otp.html'

    form_class = OTPForm

    def get(self,request,*args,**kwargs):

        form = self.form_class()

        otp = generate_otp()

        user = request.user

        phone = request.session.get('phone')

        otp_obj,created = OTP.objects.get_or_create(profile=user)
            # created givs us true or false
            # get create -- undakikll aa record tarum illakill puthiyath create cheyum

        otp_obj.otp = otp

        otp_obj.save()

        send_otp(phone,otp)

        request.session['otp_time'] = timezone.now().timestamp()
        # sessions storage--time
        # cookies okke dwld cheyth vechal namaku server kaaallum easy annu ivde kanikan.web browerill saaved img und

        remaining_time = 300

        data = {'form':form,'remaining_time':remaining_time,'phone':phone}

        return render(request,self.template,context=data)
    
    def post(self,request,*args,**kwargs):

        form = self.form_class(request.POST)

        if form.is_valid():

            user = request.user

            db_otp = user.otp.otp
            # reverse lookup ( user.otp ).. ingane ezhuthallum otp kittum..

            input_otp = form.cleaned_data.get('otp')

            otp_time = request.session.get('otp_time')  

            current_time = timezone.now().timestamp()

            if otp_time :
                # none value aalla kittirikkunnath enn urapp varuthunnath

                elapsed = current_time - otp_time

                remaining_time = max(0, 300 - int(elapsed))

                if elapsed > 300 :

                    error = 'OTP expired Request a Newone'

                elif db_otp== input_otp :
                    
                    request.session.pop('otp_time')

                    phone =request.session.get('phone')
                    # edutha phonenumber nne tick cheyunnu

                    user.phone = phone

                    user.phone_verified = True

                    user.save()

                    request.session.pop('phone') 

                    return redirect('profile')
                
                else :

                    error = 'Invalid OTP'

        data = {'form':form,'remaining_time':remaining_time,'error':error}

        return render(request,self.template,context=data)
    
@method_decorator(permitted_user_roles('user'),name='dispatch')   
class ChangePasswordOTPView(View):

    template = 'authentication/password-otp.html'

    form_class = OTPForm

    def get(self,request,*args,**kwargs):

        form = self.form_class()

        otp = generate_otp()

        user = request.user

        otp_obj,created = OTP.objects.get_or_create(profile=user)

        otp_obj.email_otp = otp

        otp_obj.save()
   
        recipient = user.email

        template = 'emails/password-otp-email.html'

        subject = 'Cineflix :OTP for change password'

        context = {'user':f'{user.first_name} {user.last_name}','otp':otp}

        thread =threading.Thread(target=send_email,args=(recipient,template,subject,context))

        thread.start()

        request.session['otp_time'] = timezone.now().timestamp()
        # sessions storage--time
        # cookies okke dwld cheyth vechal namaku server kaaallum easy annu ivde kanikan.web browerill saaved img und

        remaining_time = 300

        data = {'form':form,'remaining_time':remaining_time}

        return render (request,self.template,context=data)


    def post(self,request,*args,**kwargs):

        form=self.form_class(request.POST)

        if form.is_valid():

            user=request.user

            db_otp=user.otp.email_otp

            input_otp=form.cleaned_data.get('otp')

            otp_time = request.session.get('otp_time')  

            current_time = timezone.now().timestamp()

            if otp_time :

                elapsed = current_time - otp_time

                remaining_time = max(0, 300 - int(elapsed))

                if elapsed > 300 :

                    error = 'OTP expired Request a Newone'

                elif db_otp == input_otp :

                    request.session.pop('otp_time')

                    user.otp.email_otp_verified=True

                    user.otp.save()

                    return redirect('change-password')
                
                else :

                    error = 'Invalid OTP'

        data={'form':form,'remaining_time':remaining_time,'error':error}

        return render(request,self.template,context=data)
    
@method_decorator(permitted_user_roles('user'),name='dispatch')   

class ChangePasswordView(View):

    template = 'authentication/change-password.html'

    form_class = ChangePasswordForm

    def get(self,request,*args,**kwargs):

        user = request.user

        if user.otp.email_otp_verified:

            form = self.form_class()

            data = {'form':form}

            return render(request,self.template,context=data)
        
        else:

            return redirect(request,self.template,context=data)
    
    def post(self,request,*args,**kwargs):
        
        form = self.form_class(request.POST)

        if form.is_valid():

            user = request.user

            password = form.cleaned_data.get('new_password')
            # new password kittan

            user.password = make_password(password)
            # make password use cheythath password hash cheyyanannu

            user.save()

            return redirect('login')
        
        data = {'form':form}

        return render(request,self.template,context=data)






