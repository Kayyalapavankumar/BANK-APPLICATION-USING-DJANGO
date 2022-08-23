from django import forms

class RegistrationForm(forms.Form):
    username=forms.CharField(max_length=50)
    password = forms.CharField(max_length=50,widget=forms.PasswordInput)
    pin = forms.CharField(max_length=50,widget=forms.PasswordInput)

class LoginForm(forms.Form):
    username=forms.CharField(max_length=50)
    password = forms.CharField(max_length=50,widget=forms.PasswordInput)

class DepositForm(forms.Form):
    depositamount=forms.IntegerField()
    mobile=forms.CharField(max_length=10)

class WithdrawForm(forms.Form):
    withdrawamount=forms.IntegerField()
    mobile=forms.CharField(max_length=10)

class PinForm(forms.Form):
    pin=forms.CharField(max_length=50,widget=forms.PasswordInput)

class PinChange(forms.Form):
    newpin=forms.CharField(max_length=50,widget=forms.PasswordInput)
