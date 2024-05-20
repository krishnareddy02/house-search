from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.conf import settings


# Create your views here.
def index(request):
    # if request.session['user'] !=None:
    #     return render(request,'index.html')
    # else:
    #     return redirect(login_page)
    return render(request,'index.html')

def home(request):
    return render(request,'home.html')

def registration(request):
    return render(request,'registration.html')

def login_page(request):
    return render(request,'login.html')

# def admin_login(request):
#     return render(request,'admin.html')

def books_data(request):
    return render(request,'books_data.html')

def book_details(request):
    if request.method=='POST':
        details=house_details(
            name=request.POST['name'],
            bedroom=request.POST['bedroom'],
            description=request.POST['description'],
            price=request.POST['price'],
            email=request.session['user']
        )
        details.save()
        print("book data is recorded")
        return render(request,'books_data.html')
@api_view(['GET','POST'])
def admin(request):
        data=house_details.objects.all()
        author_details={
             'data':data
        }
        return render(request,'admin_page.html',context=author_details)

def login(request):
    if request.method=='POST':
        email_test=request.POST['email1']
        password=request.POST['password']

        if register.objects.filter(email=email_test).exists() and register.objects.filter(email=email_test).values('password').first()['password']==password:
            request.session['user']=email_test
            print("successful login")
            return render(request,'books_data.html')
        else:
            print("Invalid credientials")
            return render(request,'login.html')
    return render(request,'login.html')

def logout(request):
    if request.session['user']:
        request.session['user']=None
        print(request.session['user'])
        print("successful logout")
        return render(request,'login.html')

# @login_required(login_url='login')
@api_view(['GET','POST'])
def home_page(request):
    if request.method=='POST':
        # city1=request.POST['city']
        # cty=city1.upper()
        # a=cty[:3]
        # count=books_1.objects.filter(city=city1).count()
        # if count!=0:
        #     count+=1
        # else:
        #     count=1
        # unique_code="AR"+a+str(count)
        # print(unique_code)
            
        # if register.objects.filter(email=request.POST['email']).exists():
        #     print("Already account created")
        #     return render(request,'index.html')
        # else:
        #     print("created")
        #     user=register(
        #             # user_id=request.session['user'],
        #             name=request.POST['name'],
        #             last_name=request.POST['last_name'],
        #             phone=request.POST['contact_details'],
        #             email=request.POST['email'],
        #             # profile_image=request.FILES['profile_image'],
        #             password=request.POST['password']
        #         )
        #     user.save() 
        return render(request,'')

def seller_data(request):
    print(request.session['user'])
    obj=house_details.objects.filter(email=request.session['user']).all()
    data1={
            'serializer':obj
        }
    return render(request,'images.html',context=data1)


def delete(request,id):
    data = house_details.objects.filter(id=id)
    data.delete()
    return redirect(seller_data)

def email(request,id):
    details = get_object_or_404(house_details, id=id)

    # Prepare email content
    # message = f"name: {details.name}\nbedroom: {details.bedroom}\ndescription: {details.description}\nPrice: {details.price}"
    message = EmailMultiAlternatives(
    body = f"name: {details.name}\nbedroom: {details.bedroom}\ndescription: {details.description}\nPrice: {details.price}",
    from_email = settings.EMAIL_HOST_USER  ,
    to= [request.session['user']]
        )

    message.send()
    return redirect(admin)

