from django.shortcuts import render
from ATM.forms import RegistrationForm
from ATM.models import Customer
from ATM.forms import LoginForm
from ATM.forms import DepositForm
from ATM.forms import WithdrawForm
from ATM.forms import PinForm
from ATM.forms import PinChange
# Create your views here.

uname=""
pword=""
pin=""
newpin=""
def home(request):
    return render(request,'ATM/home.html')

def register(request):
    if(request.method=='POST'):
        form=RegistrationForm(request.POST)
        if(form.is_valid()):
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            pin=form.cleaned_data['pin']
            mdl=Customer(username=username,password=password,pin=pin,balance=0)
            mdl.save()
    else:
        form=RegistrationForm()

    return render(request,'ATM/register.html',{'form':form})

def online(request):
    global uname
    global pword
    uname=pword=""
    if(request.method=='POST'):
        fm=LoginForm(request.POST)
        if(fm.is_valid()):
            uname=uname+str(fm.cleaned_data['username'])
            pword=pword+str(fm.cleaned_data['password'])
    else:
        fm=LoginForm()
    return render(request,'ATM/login.html',{'form':fm,'user':uname,'pass':pword})

def login(request):
    global uname
    global pword

    customers=Customer.objects.all()
    for cust in customers:
        if(str(cust.username)==uname and str(cust.password)==pword):
           return render(request,'ATM/display.html',{'user':uname})
           break
    else:
           return render(request,'ATM/error.html',{'user':uname})

def back(request):
    return render(request,'ATM/home.html')

def pindeposit(request):
    global pin
    pin=""
    if(request.method=="POST"):
        form=PinForm(request.POST)
        if(form.is_valid()):
            pin1=form.cleaned_data['pin']

            pin=pin+str(pin1)
    else:
        form=PinForm()
    return render(request,"ATM/pindeposit.html",{'form':form,'pin':pin})

def deposit(request):
    status=""
    global uname
    global pword
    global pin
    if(request.method=="POST"):
        form=DepositForm(request.POST)
        if(form.is_valid()):
            amt=form.cleaned_data['depositamount']
            customers=Customer.objects.all()
            for cust in customers:
                global pin
                if(str(cust.pin)==pin):
                    cust.balance=cust.balance+int(amt)
                    cust.save()


    else:
        form=DepositForm()
    return render(request,'ATM/deposit.html',{'form':form})


def pinwithdraw(request):
    global pin
    pin=""
    if(request.method=="POST"):
        form=PinForm(request.POST)
        if(form.is_valid()):

            pin=pin+str(form.cleaned_data['pin'])
    else:
        form=PinForm()
    return render(request,"ATM/pinwithdraw.html",{'form':form})

def withdraw(request):
    global uname
    global pword
    global pin
    if(request.method=="POST"):
        form=WithdrawForm(request.POST)
        if(form.is_valid()):
            amt=form.cleaned_data['withdrawamount']
            customers=Customer.objects.all()
            for cust in customers:
                if(str(cust.pin)==pin):
                    cust.balance=cust.balance-int(amt)
                    cust.save()


    else:
        form=WithdrawForm()
    return render(request,'ATM/withdraw.html',{'form':form})


def pinbalance(request):
    global pin
    pin=""
    if(request.method=="POST"):
        form=PinForm(request.POST)
        if(form.is_valid()):
            pin=pin+str(form.cleaned_data['pin'])
    else:
        form=PinForm()
    return render(request,"ATM/pinbalance.html",{'form':form,'pin':pin})

def balance(request):
    global uname
    global pword
    global pin

    customers=Customer.objects.all()
    for cust in customers:
        global pin
        if(str(cust.pin)==pin):
            return render(request,'ATM/balance.html',{'user':uname,'balance':cust.balance})


def pinchange(request):
    global pin
    pin=""
    if(request.method=="POST"):
        form=PinForm(request.POST)
        if(form.is_valid()):
            pin=pin+str(form.cleaned_data['pin'])
    else:
        form=PinForm()
    return render(request,'ATM/pinchange.html',{'form':form})

def newpin(request):
    global pin
    global newpin
    newpin=""
    if(request.method=="POST"):
        form=PinChange(request.POST)
        if(form.is_valid()):
            newpin=newpin+str(form.cleaned_data['newpin'])
    else:
        form=PinChange()
    return render(request,'ATM/newpin.html',{'form':form})

def newpinchange(request):
    global newpin
    global pin
    customers=Customer.objects.all()
    for cust in customers:
        if(str(cust.pin)==pin):
            cust.pin=newpin
            cust.save()
            return render(request,'ATM/changed.html')

def successful_registration(request):
    return render(request,'ATM/success.html')

def successful_deposit(request):
    return render(request,'ATM/success_deposit.html')

def successful_withdraw(request):
    return render(request,'ATM/success_withdraw.html')

# Create your views here.
