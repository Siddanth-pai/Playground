from django.shortcuts import render,redirect
#from django.contrib.auth.forms import UserCreationForm# doesnt save the users
from django.contrib import messages
# Create your views here
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm,VideoForm,AudioForm
#from .models import Song
from django.contrib.auth.decorators import login_required
from .models import Video,Audio

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid() :# checks for passwords and if user already existed,
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}!')#flash messages are temporary they appear only once on reload they disappear
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form': form})


@login_required# decorators add functionality to an existing function
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)


def showaudio(request):
    lastaudio = Audio.objects.all()
    form = AudioForm(request.POST or None,request.FILES or None)
    if form.is_valid():
         form.save()


    context = {'lastaudio':lastaudio,'form':form}

    return render(request,'users/audi.html',context)


def showvideo(request):
    lastvideo = Video.objects.all()
    #videofile = lastvideo.videofile
    form = VideoForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()

    context = {'lastvideo':lastvideo,'form':form}

    return render(request,'users/videos.html',context)

#message.debug
#message.info
#message.success
#message.warning
#message.error
