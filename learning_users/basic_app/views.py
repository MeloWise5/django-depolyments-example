from django.shortcuts import render
from basic_app.forms import UserProfileForm,UserForm,UserLoginForm

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request,'basic_app/index.html')

@login_required
def special(request):
    return render(request,'basic_app/special.html',{})

#decorator allows us to only run this function if the user is logged in.
@login_required
def user_logout(request):
    #log the user log
    logout(request)
    #redirect them back to the home page
    return HttpResponseRedirect(reverse('index'))

def register(request):
    #has someone been registered
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            #save the user information to the database.
            user = user_form.save()
            #HASING the passowrd
            user.set_password(user.password)
            #now saved the hashed PasswordInput
            user.save()

            profile = profile_form.save(commit=False)

            profile.user = user
            #profile_pic is the form field
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profoile_pic']
            profile.save()

            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        #set up the form.
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,'basic_app/registration.html',{'user_form':user_form,
                                                        'profile_form':profile_form,
                                                        'registered':registered})
def user_login(request):
    user_login_form = UserLoginForm()
    #if user has pressed login
    if request.method == 'POST':
                                    #username comes from the form name='username' attribute
        username = request.POST.get('username')
        password = request.POST.get('password')
        #authenticate username
        user = authenticate(username=username,password=password)

        #if we have a username
        if user:
            #check to see if the account is active
            if user.is_active:
                #log the active user in
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Account not active!')
        else:
            print('someone tried to login and failed')
            print('Username: {} and password: {}'.format(username,password))
            return HttpResponse('Invalid login details supplied!')

    return render(request,'basic_app/login.html',{'user_login_form':user_login_form})
