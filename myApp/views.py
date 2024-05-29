from django.shortcuts import render
from django.http import HttpResponse  
from django.template import loader
from .models import UserDetail,Products
from django.contrib.auth.models import User
# Create your views here.
from django.shortcuts import redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate ,login,logout
from django.contrib.auth.decorators import login_required
User=get_user_model()



def sayHello(request):
    return HttpResponse("Hello Guys")

def homePage(request):
  products=Products.objects.all().values()
  
  context={
    "products":products,
  }
  template = loader.get_template('home_page.html')
  return HttpResponse(template.render(context,request))

def freeItem(request):
  products=Products.objects.all().values()
  template = loader.get_template('free.html')
  context={
    "products":products,
  }
 
  return HttpResponse(template.render(context,request))
     

def users(request):
  users=UserDetail.objects.all().values()
  template = loader.get_template('all_users.html')
  context={
     'users':users
  }
 
  return HttpResponse(template.render(context,request))

def details(request,id):
  current_prod=Products.objects.all().get(id=id)
  template = loader.get_template('product_detail.html')
  context={
     'current_prod':current_prod
  }
 
  return HttpResponse(template.render(context,request))

def account_details(request):
  if request.method=="POST" :
   update_username=request.POST.get('update_username')
   update_phone=request.POST.get('update_phone')
   
   print(type(update_username))
   
  #  if(not update_username  and not update_phone ):
  #      print("jj")
       
       
  #      pass
     
  #  elif( not update_phone  ):
  #     u=register.user
  #     print(update_username)
  #     u.username=update_username
  #     u.save()
  
    
  template = loader.get_template('account_page.html')
   
  print( (request.user.username))
  return HttpResponse(template.render({ },request))


def register(request):
 if request.method=="POST" :
   username=request.POST.get('username')
   email=request.POST.get('email')
   password=request.POST.get('password')
  
   user=User.objects.create(
   username=username,
   email=email,

  )

   user.set_password(password)
   user.save()

  
   
 template = loader.get_template('register.html')
 return HttpResponse(template.render(request=request))

def logout_page(request):
  logout(request)
  return redirect('/')


def login_page(request):
  if request.method=="POST" : 
   email=request.POST.get('email')
   password=request.POST.get('password')

   if not UserDetail.objects.filter(email=email).exists():
     return redirect('/login/')
   


   user=authenticate(request ,email=email ,password=password)

   if user is None:
     return redirect('/login/')
   else:
     login(request=request,user=user)
     return redirect('/')

  template = loader.get_template('login.html')
  return HttpResponse(template.render(request=request))
      

@login_required(login_url='/login')
def cart(request):
  cart=request.user.cart
  products=Products.objects.all().values()

  cart_item=[]
   
  for x in  cart:
       cart_item.append(products[x-1])   
       ########################################  x-1 is used above xth id is x-1 th product 

   
  template = loader.get_template('cart.html')
  context={
    "cart_items":cart_item, 
    
  }
  
  print( cart)
  return HttpResponse(template.render(context,request))
     

def sell(request):
  
  template = loader.get_template('sell.html')
 
  if request.method=="POST" :
    name=request.POST.get('product_name')
    price =request.POST.get('product-price')
    img=request.POST.get('product_img_url')
    description=request.POST.get('product-description')
    prod=Products.objects.create(
      product_name=  name,
      product_price= price,
    product_img_url= img,
    seller_detail=request.user.id,
    description=description

    )
    prod.save()
    print(prod.id)
    this_user=request.user
    this_user.for_sale.append(prod.id) 
    this_user.save()
    print(len(this_user.for_sale))

  sell_items=[]
  forsale=request.user.for_sale
  products=Products.objects.all().values() 
  for x in  forsale:
      sell_items.append(products[x-1])
  
  context={  
           'sell_items':sell_items
           }
    

   
 
  return HttpResponse(template.render(context,request))


def add_to_cart(request,id):
  u=request.user
   
  u.cart.append(id)
  u.save()
  return redirect('/account/cart')


def rem_from_cart(request,id):
  u=request.user
   
  u.cart.remove(id)
  u.save()
  return redirect('/account/cart')
  
   
 