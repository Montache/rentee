from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm


# Create your views here.


def SignupUser(request):
    page = 'signup'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form=CustomUserCreationForm()

    context = {'form': form, 'page': page}
    return render(request, 'Authentication/Signup.html', context)


# def SignupUser(request):
#     if request.method == 'POST':
#         form= CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             email=form.cleaned_data['email']
#             username=form.cleaned_data['username']
#             password1=form.cleaned_data['password1']
#             password2=form.cleaned_data['password2']
#             user=authenticate(email=email, username=username, password1=password1, password2=password2 )
#             login(request,user)
#             messages.success(request,('Signup successful'))
#             return redirect('home')
#     else:
#         form=CustomUserCreationForm()

#     return render(request, 'Authentication/Signup.html', {
#         'form':form,
#     })


def LoginUser(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ('There was an error with your login details, please try again!'))
            return redirect('login')
    else:
        return render(request, 'Authentication/Login.html')

def LogoutUser(request):
    logout(request)
    messages.success(request, ('You have logged out successfully'))
    return redirect('home')
