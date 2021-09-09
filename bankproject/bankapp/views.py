from django.shortcuts import render, redirect
from . models import AccountInfo
import datetime
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def index(request):
    return render(request, "index.html")

def createaccount(request):
    return render(request, "createaccount.html" )

def saveuser(request):
    acno=request.POST['acno']
    name=request.POST['name']
    gender=request.POST['gender']
    address=request.POST['address']
    dob=request.POST['dob']
    contactno=request.POST['contactno']
    emailaddress=request.POST['emailaddress']
    panno=request.POST['panno']
    aadharno=request.POST['aadharno']
    balance=request.POST['balance']
    openingdate=request.POST['openingdate']
    password=request.POST['password']
    # ORM (Object Relationship Mapping)
    acn=AccountInfo(acno=acno, name=name, gender=gender, address=address, dob=dob, contactno=contactno, emailaddress=emailaddress, panno=panno, aadharno=aadharno, balance=balance, openingdate=openingdate, password=password )
    acn.save()
    return redirect('index')

def login(request):
    return render(request, "login.html")

def logcode(request):
    acno=request.POST['acno']
    password=request.POST['password']
    op=request.POST['op']
    msg='Message ='
    try:
        obj=AccountInfo.objects.get(acno=acno, password=password)
        if obj is not None:
            if op=='deposit':
                request.session['acno']=obj.acno
                return render(request,"deposit.html")
            elif op=='withdraw':
                request.session['acno']=obj.acno
                return render(request,"withdrawamount.html")
            elif op=='enquiry':
                balance=obj.balance
                return render(request,"balanceenquiry.html", {'msg':'Current Balance = '+str(balance)})
    except ObjectDoesNotExist:
        msg=msg+" Invalid Details"
    return render(request, "login.html", {'msg': msg})

def depositamt(request):
    amt=int(request.POST['amt'])
    obj=AccountInfo.objects.get(acno=request.session['acno'])
    balance=obj.balance
    balance=balance+amt
    AccountInfo.objects.filter(pk=obj.acno).update(balance=balance)
    request.session['acno']=None
    return redirect('index')

def withdrawamt(request):
    amt = int(request.POST['amt'])
    obj = AccountInfo.objects.get(acno=request.session['acno'])
    balance = obj.balance
    if balance<amt:
        return render(request, "withdrawamount.html", {'msg':'Insufficient Balance'})
    balance = balance - amt
    AccountInfo.objects.filter(pk=obj.acno).update(balance=balance)
    request.session['acno'] = None
    return redirect('index')









