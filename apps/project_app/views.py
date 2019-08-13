from django.shortcuts import render, redirect, HttpResponse

def dashboard(request):
    context= {
        "product" : product
    
    }
    return (request, 'dashboard.html', context)

def login(request):
    userlogin = User.objects.get(email=request.POST['loginEmail'])
        request.session['user_id'] = userlogin.id
        request.session['user_name'] = userlogin.first_name
        return redirect('/dashboard')
    
def register(request):
    User.objects.create(name=request.POST['name'],address=request.POST['address'],email=request.POST['email'],password=request.POST['password'])
        last_user = User.objects.last()
        request.session['user_id'] = last_user.id
        request.session['user_name'] = last_user.first_name
        return redirect('/dashboard')
    
def checkout(request):
    context= {
        
        "product" : product,
        "employee" : employee
    }
    return (request, 'checkout.html', context)

def reports(request):
    context = {
        
        "product" : product,
        "employee" : employee
        }
    return (request, 'reports.html', context)

def employee_list(request):
    context = {
        "employee" : employee
    
        
        
    }
    
    
    return (request, 'employee_list.html', context)

    
    

    