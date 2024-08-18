from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Tender
# Create your views here.
def home_view(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('tender_form')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')
    return render(request, 'login.html')
def tender1_view(request):
    return render(request, 'tender1.html')

def loginadmin_view(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        if username=='revanth':
            user=auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect('admin_page')
            else:
                messages.info(request,'Invalid Credentials')
                return redirect('loginadmin')
        else:
            messages.info(request, 'Invalid admin Username')
            return redirect('loginadmin')
    return render(request,'loginadmin.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email'] 
        password1 = request.POST['pass1']
        password2 = request.POST['pass2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                print('User created')
                return redirect('home')
        else:
            messages.info(request,'Password not matching....')
            return redirect('register')
    return render(request, 'register.html')
def view_tender(request):
    if request.method == 'POST':
        tender_id = request.POST.get('tender_id')
        username = request.POST.get('username')
        organization = request.POST.get('organization')
        num_tenders_done = request.POST.get('num_tenders_done')
        license_id = request.POST.get('license_id')
        license_photo=request.FILES.get('license_photo')
        bid_amount = request.POST.get('bid_amount')
        if tender_id and bid_amount:
            tender = Tender.objects.create(
                tender_id=tender_id,
                username=username,
                organization=organization,
                num_tenders_done=num_tenders_done,
                license_id=license_id,
                bid_amount=bid_amount
            )
            tender.save()
            messages.success(request, 'Tender data stored successfully!')
            return redirect('home')  
        else:
            messages.error(request, 'Failed to store tender data. Please fill in all required fields.')
            return redirect('tender_form')
    
    return render(request, 'tender_form.html')
def admin_page_view(request):
    item=Tender.objects.all()
    return render(request,'adminpage.html',{'item':item})
def delete_item_view(request,item_id):
    item=Tender.objects.get(id=item_id)
    item.delete()
    return redirect('admin_page')

def find_min_bid_tender(request):
    min_bid_tenders = Tender.objects.filter(bid_amount=Tender.objects.order_by('bid_amount').first().bid_amount)
    return render(request, 'find_min_bid_tender.html', {'min_bid_tenders': min_bid_tenders})
