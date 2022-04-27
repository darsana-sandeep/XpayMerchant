from django.contrib import auth, messages
from django.core.mail import message
from django.shortcuts import render, redirect

# Create your views here.
from . models import MerchantProfile


def register(request):
    if request.method == 'POST':
        shop = request.POST['shop']
        name = request.POST['name']
        proof = request.POST['proof']
        licence = request.POST['licence']
        gst = request.POST['gst']
        location = request.POST['location']
        address = request.POST['address']
        phone = request.POST['phone']
        altphone = request.POST['altphone']
        email = request.POST['email']
        business = request.POST['business']
        pwd = request.POST['pwd']
        repwd = request.POST['repwd']

        if pwd==repwd:
            if MerchantProfile.objects.filter(Email=email).exists():
                print("username taken")
            else:
                user = MerchantProfile(shop_name=shop,owner_name= name,proof=proof,licence=licence,gst=gst,location=location,address=address,phone=phone,alt_phone=altphone,Email=email,business_email=business,password=pwd)
                user.save()
                print("user created")
                return redirect(login)
        else:
            print("password is not matching")
        return redirect(register)
    return render(request,'Registration.html')

def login(request):
    if request.method == 'POST':
        try:
            email = request.POST['email']
            pwd = request.POST['pwd']

            users = MerchantProfile.objects.get(Email=email,password=pwd)
            request.session["email"]=users.Email
            current_user =request.session["email"]
            return render(request,'base.html',{'current_user':current_user})
        except MerchantProfile.DoesNotExist as e:
            print('invalid')
            return redirect(login)
    return render(request,'login.html')

def base(request):
    return render(request,'base.html')

def logout(request):
    try:
        del request.session['email']
    except:
        return redirect(login)
    return redirect(login)




