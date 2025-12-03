from django import forms

from .models import Profile

from re import fullmatch
# regular exp vech valid anno ille enn nookum

class LoginForm(forms.Form):

    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','required':'required'}))

    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','required':'required'}))


class SignUpForm(forms.ModelForm):

    class Meta:

        model = Profile
        #eth model declare cheyth enn nooki vennom cheyan

        fields = ['first_name','last_name','email']

        widgets = {

            'first_name' : forms.TextInput(attrs={'class':'form-control'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
        }

    def clean(self):

        cleaned_data = super().clean()

        email = cleaned_data.get('email')

        if Profile.objects.filter(email=email).exists():
            # same email twice register cheythal kanikkan vendi

            self.add_error('email','This Email already registered! ')   

class AddPhoneForm(forms.Form):
    # ivde modelform edukkilla because model onnu create cheyan illa
    # kittuna phone no obj lott add cheythal matti

    phone = forms.CharField(max_length=14,widget=forms.TextInput(attrs={'class':'form-control'}))

    def clean(self):

        cleaned_data = super().clean()

        phone = cleaned_data.get('phone')

        # regular exp vech valid anno ille enn nookum
        pattern = '(\\+?91)?\\s?[6-9]\\d{9}'
        # ? represents optional

        valid = fullmatch(pattern,phone)

        if not valid:

            self.add_error('phone','invalid phone number')
            # error annakill kanikkan vendi

        if Profile.objects.filter(phone=phone).exists():
            # same phone number twice register cheythal kanikkan vendi

            self.add_error('phone','This Phone Number already registered! ')

class OTPForm(forms.Form):

    otp = forms.CharField(max_length=4,widget=forms.TextInput(attrs={'class':'form-control'}))

class ChangePasswordForm(forms.Form):

    new_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

    def clean(self):

        cleaned_data = super().clean()
        # new password and confirm password match aakunnundo enn nokkunne

        new_password = cleaned_data.get('new_password')

        confirm_password = cleaned_data.get('confirm_password')

        if new_password != confirm_password:

            self.add_error('confirm_password','Password does not match')           




        

        