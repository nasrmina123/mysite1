from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login , logout 
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.
def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
           
           # form = AuthenticationForm(request=request , data = request.POST)
            #if form.is_valid():
            #username = form.cleaned_data.get('username')
            #password = form.cleaned_data.get('password')
                
            username =  request.POST.get('username')
            password =  request.POST.get('password')

            user = authenticate(request, username=username , password=password)
            if user is not None :
                login(request,user)
                return redirect('/')

            user = authenticate(request, username = User.objects.get(email = username) , password=password)
            if user is not None :
                login(request,user)
                return redirect('/')
      
        #form = AuthenticationForm()
        #context = {'form':form}
        return render(request, 'accounts/login.html')
    else:
        return redirect('/')
    
@login_required   
def logout_view(request):
    logout(request)
    return redirect('/')


def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
    
            username =  request.POST.get('username')
            password1 =  request.POST.get('password1')
            email =  request.POST.get('email')
            
            myuser = User.objects.create_user(username = username,  password = password1 , email = email)
            myuser.save()

            
          #  form = UserCreationForm(request.POST)
           # if form.is_valid():
           #     print('user is valid')
           #     form.save()
    
                
            return redirect('/')     
        #form = UserCreationForm()
        #context = {'form':form}
        return render(request, 'accounts/signup.html')
    else: 
        return redirect('/') 
        
    
    
        
