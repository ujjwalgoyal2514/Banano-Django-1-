
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages  # Import the messages module
from .forms import SignUpForm, UserProfileForm, LoginForm
from .models import UserProfile
from django.contrib.auth import logout

def welcome(request):
    return render(request, 'myapp/welcome.html')


def signup(request):
    if request.method == 'POST':
        user_form = SignUpForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            # Set usertype from the form data
            usertype = user_form.cleaned_data['usertype']
            profile.usertype = usertype
            profile.save()

            return redirect('login')
    else:
        user_form = SignUpForm()
        profile_form = UserProfileForm()

    return render(request, 'myapp/signup.html', {'user_form': user_form, 'profile_form': profile_form})




def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            usertype = form.cleaned_data['usertype']

            user = authenticate(request, username=username, password=password)

            if user is not None and hasattr(user, 'userprofile') and user.userprofile.usertype == usertype:
                login(request, user)
                if usertype == 'patient':
                    return redirect('patient_profile')
                elif usertype == 'doctor':
                    return redirect('doctor_profile')
            else:
                # Display an error message
                messages.error(request, 'Invalid login credentials. Please try again.')

    else:
        form = LoginForm()

    return render(request, 'myapp/login.html', {'form': form})



def patient_profile(request):
    profile = UserProfile.objects.get(user=request.user)
    return render(request, 'myapp/patient_profile.html', {'profile': profile})

def doctor_profile(request):
    profile = UserProfile.objects.get(user=request.user)
    return render(request, 'myapp/doctor_profile.html', {'profile': profile})

def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login')
