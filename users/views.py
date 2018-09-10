from django.shortcuts import render,redirect
#from django.contrib.auth.forms import UserCreationForm# doesnt save the users
from django.contrib import messages
# Create your views here
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm

from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid() :# checks for passwords and if user already existed,
            form.save()# automatically hash the passwords and saves the form
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}!')#flash messages are temporary they appear only once on reload they disappear
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form': form})

@login_required# decorators add functionality to an existing function
def  profile(request):
if request.method == 'POST':    
    u_form = UserUpdateForm(instance =request.user)
    p_form = ProfileUpdateForm(instance = request.user.profile)

    context = {
    'u_form':u_form,
    'p_form':p_form
    }



    return render(request,'users/profile.html',context)
#message.debug
#message.info
#message.success
#message.warning
#message.error
