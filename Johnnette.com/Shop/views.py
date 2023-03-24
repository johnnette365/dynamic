import imp
from itertools import product
from queue import Empty
import re
from unicodedata import category
import django
from urllib import request
from distutils.log import error
from multiprocessing import context
from django import views
from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from django.views import View
from numpy import empty, save
from Shop.models import Product, Address, OrderPlaced
from Shop.forms import RegistrationForm, LoginForm, PasswordChangeForm, CustomerAddressForm
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import JsonResponse
from django.core.mail import send_mail





def customerregistration(request):
    if request.method == "POST":
        signup = RegistrationForm(request.POST)
        if signup.is_valid() and signup.cleaned_data['password'] == signup.cleaned_data['confirm_password']:
            fname = signup.cleaned_data['first_name']
            sname = signup.cleaned_data['last_name']
            username = signup.cleaned_data['username']
            email = signup.cleaned_data['email']
            password = signup.cleaned_data['password']

            user = User.objects.create_user(username, email, password)
            user.first_name = fname
            user.last_name = sname
            user.save()
            messages.success(request,"Wecome to Johnnette")
            return redirect("/shop/login")
        elif signup.cleaned_data['password'] != signup.cleaned_data['confirm_password']:
            messages.error(request, "Password does not match")

    signup = RegistrationForm()
    context = {
        'signup':signup
    }
    return render (request, 'accounts/customerregistration.html', context)

def login(request):
    if request.method == "POST":
        login = LoginForm(request.POST)
        if login.is_valid():
            username = login.cleaned_data['username']
            password = login.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request,"Welcome To Johnnette")
                return redirect('/shop/profile')
            else: 
                messages.error(request, "Invalid Username Or Password")
    login = LoginForm()            
    context={
        "login":login
    }
    return render(request, 'accounts/login.html',context)

def LogOut(request):
    logout(request)
    messages.error(request,"You Are Logged Out")
    return redirect('/shop/login')


# @login_required(login_url="/login")
class ProfileView(View):
    def get(self, request):
        forms = CustomerAddressForm()
        context = {
            'forms':forms,
        }
        return render(request, 'app/profile.html',context)

    def post(self, request):
        if request.method == "POST":
            forms = CustomerAddressForm(request.POST)

            ['full_name', 'locality', 'mobile_number', 'address1', 'address2', 'landmark', 'city', 'state', 'pincode']
            
            if forms.is_valid():
                current_user = request.user
                full_name = forms.cleaned_data['full_name']
                locality = forms.cleaned_data['locality']
                mobile=forms.cleaned_data['mobile_number']
                address1=forms.cleaned_data['address1']
                address2=forms.cleaned_data['address2']
                landmark=forms.cleaned_data['landmark']
                state = forms.cleaned_data['state']
                city = forms.cleaned_data['city']
                pincode = forms.cleaned_data['pincode']

                address = Address(user=current_user, full_name=full_name, locality=locality, mobile_number=mobile, address1=address1, address2=address2, landmark=landmark, state=state, city=city, pincode=pincode)
                address.save()
                messages.success(request, "Congratulations !! Profile Updated Successfully.")
        
        forms = CustomerAddressForm()
        context = {
            'forms':forms
        }
        return render(request, 'app/profile.html',context)


@login_required(login_url="/shop/login")
def address(request):
    address = Address.objects.filter(user = request.user)
    context = {"address":address}
    return render(request, 'app/address.html', context)


@login_required(login_url="/shop/login")
def orders(request):
    op=OrderPlaced.objects.filter(user=request.user).order_by('-id')
    return render(request, 'app/orders.html', {"order_placed":op})


class ProductView(View):
    def get(self, request):
        totalitem = 0
        quantity = 0
        featured_product = Product.objects.filter(category='FEATURED')
        mens_product = Product.objects.filter(category='MEN')
        womens_product = Product.objects.filter(category='WOMEN')
        accessories = Product.objects.filter(category='ACCESSORIES')

        # if request.user.is_authenticated:
        #     totalitem=len(Cart.objects.filter(user=request.user))
        
        context={
        "featured":featured_product,
        "men":mens_product,
        "women":womens_product,
        "accessories":accessories,
        }
        return render(request, 'app/home.html',context)


def product_detail(request,pk):
    product = get_object_or_404(Product, id=pk)
    item_already_in_cart = False
    if request.user.is_authenticated:
        item_already_in_cart = Cart.objects.filter(Q(product=product.id) & Q(user=request.user)).exists()
    context = {
        'product':product,
        "item_already_in_cart":item_already_in_cart,
    }
    return render(request, 'app/productdetail.html', context)



from Shop.models import Cart
@login_required(login_url="/shop/login")
def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    buy_product_id = request.GET.get('buy_prod_id')
    
    if product_id:
        product = Product.objects.get(id=product_id)
        Cart(product=product, user=user).save()
        return redirect('/shop/cart')
    
    if buy_product_id:
        product = Product.objects.get(id=buy_product_id)
        Cart(product=product, user=user).save()
        return redirect('/shop/checkout')
    


@login_required(login_url="/shop/login")
def show_cart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user).order_by('-id')

        amount = 0.0
        totalamount = 0.0
        shipping_price = 70.0
        discount = 0.0
        selling_price = 0.0
        # Python - List Comprehension
        cart_product = [p for p in Cart.objects.all() if p.user == user]
        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity*p.product.actual_price)
                amount += tempamount

                temp_discount = (p.quantity*p.product.selling_price)
                selling_price += temp_discount

                if (selling_price >= 500):
                    shipping_price = 0.0
                else:
                    shipping_price = 70.00
                totalamount = selling_price+shipping_price
                discount = amount-selling_price
                save = int(discount-shipping_price)
        else:
            cart = None
            save = 0
            shipping_price = "0.0"

    context = {
        "carts":cart,
        "totalamount":totalamount,
        "amount":amount,
        "shipping_price":shipping_price,
        "discount":discount,
        "save":save
    }
    return render(request, 'app/addtocart.html',context)


@login_required(login_url="/shop/login")
def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        cart_item = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))

        cart_item.quantity += 1
        cart_item.save()
        
        amount = 0
        totalamount = 0
        shipping_price = 0
        discount = 0
        selling_price = 0
        # Python - List Comprehension
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity*p.product.actual_price)
            amount += tempamount
        
            temp_discount = (p.quantity*p.product.selling_price)
            selling_price += temp_discount

            if (selling_price >= 500 ):
                shipping_price = 0.0
            else:
                shipping_price += 70
                
                
                
            totalamount = selling_price+shipping_price
            discount = amount-selling_price
            save = int(discount-shipping_price)


        data = {
            "quantity":cart_item.quantity,
            "totalamount":totalamount,
            "amount":amount,
            "shipping_price":shipping_price,
            "discount":discount,
            "save":save
        }
        return JsonResponse(data)
    

@login_required(login_url="/shop/login")
def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        cart_item = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))

        cart_item.quantity -= 1
        if cart_item.quantity == 0:
            cart_item.quatity += 1
        cart_item.save()
        
        
        amount = 0
        totalamount = 0
        shipping_price = 0
        discount = 0
        selling_price = 0
        # Python - List Comprehension
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity*p.product.actual_price)
            amount += tempamount
        
            temp_discount = (p.quantity*p.product.selling_price)
            selling_price += temp_discount


            if (selling_price >= 500 ):
                shipping_price = 0
            else:
                shipping_price += 70
                            
                            
        totalamount = selling_price+shipping_price
        discount = amount-selling_price
        save = int(discount-shipping_price)


        data = {
            "quantity":cart_item.quantity,
            "totalamount":totalamount,
            "amount":amount,
            "shipping_price":shipping_price,
            "discount":discount,
            "save":save
        }
        return JsonResponse(data)


@login_required(login_url="/shop/login")
def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        cart_item = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        cart_item.delete()
        
        amount = 0
        totalamount = 0
        discount = 0
        selling_price = 0
    
        # Python - List Comprehension
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity*p.product.actual_price)
            amount += tempamount
        
            temp_discount = (p.quantity*p.product.selling_price)
            selling_price += temp_discount
                
        shipping_price = 0
        totalamount = selling_price+shipping_price
        discount = amount-selling_price
        save = int(discount-shipping_price)

        data = {
            "amount":amount,
            "discount":discount,
            "totalamount":totalamount,
            "shipping_price":shipping_price,
            "save":save
        }
        return JsonResponse(data)


@login_required(login_url="/shop/login")
def deliveryaddress(request):
    user=request.user
    add=Address.objects.filter(user=user)
    cart=Cart.objects.filter(user=user)
    
    if not cart:
        return redirect('/shop/cart')

    if request.method == "POST":
        forms = CustomerAddressForm(request.POST)
        # ['full_name', 'locality', 'mobile_number', 'address1', 'address2', 'landmark', 'city', 'state', 'pincode']
        if forms.is_valid():
            current_user = request.user
            full_name = forms.cleaned_data['full_name']
            locality = forms.cleaned_data['locality']
            mobile=forms.cleaned_data['mobile_number']
            email=forms.cleaned_data['email']
            house_no=forms.cleaned_data['house_no']
            area=forms.cleaned_data['area']
            landmark=forms.cleaned_data['landmark']
            state = forms.cleaned_data['state']
            city = forms.cleaned_data['city']
            pincode = forms.cleaned_data['pincode']
            home = forms.cleaned_data['home']
            office = forms.cleaned_data['office']
            address = Address(user=current_user, full_name=full_name, locality=locality, mobile_number=mobile, email=email, house_no=house_no, area=area, landmark=landmark, state=state, city=city, pincode=pincode, home=home, office=office)
            address.save()
            messages.success(request, "Congratulations !! Profile Updated Successfully.")
        
    forms = CustomerAddressForm()
    context = {
        'forms':forms,
        "add":add,
    }
    return render(request, 'app/deliveryaddress.html',context)



from django.conf import settings
import razorpay
from django.contrib.sites.shortcuts import get_current_site
@login_required(login_url="/shop/login")
def checkout(request):
    user=request.user
    custadd=request.GET.get('custid')
    add=Address.objects.filter(id=custadd)
    cart_items=Cart.objects.filter(user=user)

    if not add:
        messages.error(request, "Please Select At Least One Shipping Address")
        return redirect('/shop/deliveryaddress')

    amount = 0
    order=0
    totalamount = 0
    shipping_price = 0
    selling_price = 0
    cart_product = [p for p in Cart.objects.all() if p.user == request.user]
    if cart_product:
        for p in cart_product:
            tempamount = (p.quantity*p.product.actual_price)
            amount += tempamount
        
            temp_discount = (p.quantity*p.product.selling_price)
            selling_price += temp_discount
            
            totalamount = selling_price+shipping_price    
            p.address=custadd
            
            product_id = p.datetime_of_order.strftime('PDOJTPL%Y%m%dODR') + str(p.id)
            p.prod_id=product_id
        
        order_id = p.datetime_of_order.strftime('PAY2JTPL%Y%m%dODR') + str(p.id)
        
        for p in cart_product:
             p.order_id=order_id
            
        if product_id is not None:
            client = razorpay.Client(auth=(settings.KEY, settings.SECRET))
            data = {"amount": totalamount*100, "currency": "INR", "receipt": "order", "payment_capture":1}
            payment = client.order.create(data=data)  
            print(payment)

            payment_id = payment['id']

            for p in cart_product:
                p.razorpay_order_id = payment_id
                p.save()
            
        else:
            messages.error(request, "Order Id is Missing")
            return redirect('/shop/deliveryaddress')

        callback_url = 'http://'+ str(get_current_site(request))+"/shop/handlerequest/"
    context={
        "add":add,
        "totalamount":totalamount,
        "cart_items":cart_items,
        "payment":payment,
        "callback_url":callback_url,
    }
    return render(request, 'app/checkout.html',context)




from django.core.mail import EmailMultiAlternatives
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import get_template
@csrf_exempt
def handlerequest(request):
    razorpay_client = razorpay.Client(auth=(settings.KEY, settings.SECRET))
    if request.method == 'POST':
        try:
            razorpay_order_id = request.POST.get("razorpay_order_id")
            razorpay_payment_id = request.POST.get("razorpay_payment_id")
            razorpay_signature = request.POST.get("razorpay_signature")

            print(razorpay_order_id)
            print(razorpay_payment_id)
            print(razorpay_signature)
            
            params_dict={
                "razorpay_order_id":razorpay_order_id,
                "razorpay_payment_id":razorpay_payment_id,
                "razorpay_signature":razorpay_signature,
            }
            product = [p for p in Cart.objects.all() if p.user==request.user and p.razorpay_order_id==razorpay_order_id]
            for order_db in product:
                order_db.razorpay_payment_id=razorpay_payment_id
                order_db.razorpay_signature=razorpay_signature
                order_db.save()
            result=razorpay_client.utility.verify_payment_signature(params_dict)
            if result:
                return redirect("/shop/paymentdone")
            elif result==None:
                return redirect("/shop/paymentfailed")
        except:
            return HttpResponse("third 505 Not Found")
        
        

        
from datetime import datetime
def payment_done(request):
    user=request.user
    razorpay_client = razorpay.Client(auth=(settings.KEY, settings.SECRET))
    order_db = [p for p in Cart.objects.all() if p.user==request.user]
    
    mail_date = []
    mail_order_id = []
    mail_product_id = []
    mail_product_title = []
    mail_quantity = []
    mail_total_cost = []
    
    for order_db in order_db:
        address=Address.objects.get(id=order_db.address)
        payment_id=order_db.razorpay_payment_id
        payment = razorpay_client.payment.fetch(payment_id)
        # payment_method = payment['method']
        if payment['method']:
            payment_method = payment['method']
            print(payment_method)
        else:
            error = razorpay.errors.BadRequestError
            print(error)
        if payment['status'] == 'captured':
            OrderPlaced(order_id=order_db.order_id, prod_id=order_db.prod_id, user=user, address=address, razorpay_order_id=order_db.razorpay_order_id, product=order_db.product, quantity=order_db.quantity, total_amount=order_db.total_cost, payment_status=1, razorpay_payment_id=order_db.razorpay_payment_id, razorpay_signature=order_db.razorpay_signature).save()
            
            mail_date.append(order_db.datetime_of_order)
            mail_order_id.append(order_db.order_id)
            mail_product_id.append(order_db.prod_id)
            mail_product_title.append(order_db.product.product_title)
            mail_quantity.append(order_db.quantity)
            mail_total_cost.append(order_db.product.selling_price)
            
            order_db.delete()
        elif payment['status'] == 'authorized':
            OrderPlaced(order_id=order_db.order_id, prod_id=order_db.prod_id, user=user, address=address, razorpay_order_id=order_db.razorpay_order_id, product=order_db.product, quantity=order_db.quantity, total_amount=order_db.total_cost, payment_status=3, razorpay_payment_id=order_db.razorpay_payment_id, razorpay_signature=order_db.razorpay_signature).save()
            order_db.delete()

    all_datetime=mail_date[0]
    datetime_string=str(all_datetime)
    order_datetime=datetime.fromisoformat(datetime_string)
    order_date=order_datetime.date()
    total=0
    email=address.email
    house_no=address.house_no
    area=address.area
    city=address.city
    state=address.state
    pincode=address.pincode
    circle = "\u25E6"
    disc = "\u25CF"
    product_info = []
    for i in range(len(mail_product_title)):
        # info = f" {disc} {mail_product_id[i]} - {mail_product_title[i]} - {mail_quantity[i]} x Rs{mail_total_cost[i]:.2f} = Rs{mail_quantity[i]*mail_total_cost[i]:.2f}"
        info = f" {disc} {mail_product_title[i]} - {mail_quantity[i]} x Rs{mail_total_cost[i]:.2f} = Rs{mail_quantity[i]*mail_total_cost[i]:.2f}"
        total += mail_quantity[i]*mail_total_cost[i]
        product_info.append(info)

    template1 = f"Dear {address.full_name} \n\nThank you for your recent purchase from our store. We are pleased to confirm that your order has been received and is being processed. Below are the details of your order: \n\nOrder ID: {mail_order_id[0]}\nDate of Purchase: {order_date}\n\n"
    template2 = "Order Summary:\n{}"
    template3 = template2.format('\n'.join(product_info))
    template4 = f"\n {disc} Shipping: 70INR\n {disc} Taxes: Rs6.00\n {disc} Total: Rs{total}\n\nShipping Information:\n{address.full_name}\n{house_no}, {area}\n{city}, {state} {pincode}\nDelivery Method: Standard Shipping\nEstimated Delivery Date: March 30, 2023\n\nPayment Information:\nPayment Method: {payment_method}\nTotal Amount Paid: Rs{70+total}\n\nContact Information:\nIf you have any questions or concerns about your order, please do not hesitate to contact us at 1-800-123-4567 or support@johnnette.com.\n\nCancellation and Return Policy:\nYou can cancel your order within 24 hours of placing it. If you are not completely satisfied with your purchase, you can return it for a full refund within 07 days.\n\nThank you for choosing our store. We appreciate your business and hope to see you again soon.\n\nSincerely,\nJohnnetteStore Team."
    
    template5=template1+template3+template4

    send_mail(
        f'Order Confirmation: {mail_order_id[0]} from JTPL STORE',
        
        template5,

        'yk@johnnette.com',
        [f'{email}'],
        fail_silently=False,
    )
            
    return redirect("/shop/orders")



        
        
def payment_failed(request):
    user=request.user
    razorpay_client = razorpay.Client(auth=(settings.KEY, settings.SECRET))
    order_db = [p for p in Cart.objects.all() if p.user==request.user]
    for order_db in order_db:
        address=Address.objects.get(id=order_db.address)
        print(address.full_name)
        payment_id=order_db.razorpay_payment_id
        payment = razorpay_client.payment.fetch(payment_id)
        print("=========================", payment['status'])
        if payment['status'] == 'failed':
            OrderPlaced(order_id=order_db.order_id, prod_id=order_db.prod_id, user=user, address=address, razorpay_order_id=order_db.razorpay_order_id, product=order_db.product, quantity=order_db.quantity, total_amount=order_db.total_cost, payment_status=3, razorpay_payment_id=order_db.razorpay_payment_id, razorpay_signature=order_db.razorpay_signature).save()
            order_db.delete()
    return redirect("/shop/cart")
        
        
def handle_payment(request):
    pass































def mens(request, data = None):
    if data == None:
        coffee = Product.objects.filter(category="CO")
    elif data == 'below':
        coffee = Product.objects.filter(category = "CO").filter(selling_price__lt=1000)
    elif data == 'above':
        coffee = Product.objects.filter(category = "CO").filter(selling_price__gt=1000)
    context = {
        'coffee':coffee,
    }
    return render(request, "app/mens.html",context)

@login_required(login_url="/shop/login")
def buy_now(request):
    return render(request, 'app/buynow.html')

@login_required(login_url="/shop/login")
def mobile(request):
    return render(request, 'app/mobile.html')


def clothes(request, data = None):
    topwears = Product.objects.filter(category='TW')
    bottomwear = Product.objects.filter(category='BW')
    if data == "Top":
        topwears = Product.objects.filter(category="TW")
    elif data == "Bottom":
        bottomwear = Product.objects.filter(category="BW")
    elif data == "below":
        bottomwear = Product.objects.filter(category="BW").filter(selling_price__lt=1000) 
    elif data == "below":
        topwears = Product.objects.filter(category="BW").filter(selling_price__lt=1000) 
    elif data == "above":
        bottomwear = Product.objects.filter(category="BW").filter(selling_price__gt=1000) 
    elif data == "above":
        topwears = Product.objects.filter(category="BW").filter(selling_price__gt=1000) 
    context = {
        "topwears":topwears,
        "bottomwear":bottomwear,
    }
    return render(request, "app/clothes.html",context)

def shoes(request):
    shoes = Product.objects.filter(category='S')
    context = {
        "shoes":shoes,
    }
    return render(request, "app/shoes.html",context)
 
def beauty_product(request):
    beauty_product = Product.objects.filter(category='BEA')
    context = {
        "beauty_product":beauty_product,
    }
    return render(request, "app/beauty_products.html",context)

def grocery(request):
    grocery = Product.objects.filter(category='GRO')
    context = {
        "grocery":grocery,
    }
    return render(request, "app/grocery.html",context)

def accessories(request):
    accessory = Product.objects.filter(category='Acce')
    context = {
        'accessory':accessory,
    }
    return render(request, "app/accessories.html",context)