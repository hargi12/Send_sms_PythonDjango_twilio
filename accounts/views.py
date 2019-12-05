from twilio.rest import Client
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.models import User, auth
from .models import Profile
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
# Create your views here.

@login_required
@user_passes_test(lambda user: user.profile.user_level, login_url='main:rights')
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        user_level = request.POST['user_level']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('accounts:register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                return redirect('accounts:register')
            else:
                user = User.objects.create_user(
                    username=username, password=password1, email=email)
                profile = Profile.objects.create(user_level=user_level, user_id=user.id)
                user.save()
                profile.save()
                messages.info(request, 'User created successfully')
                return redirect('accounts:users')
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('accounts:register')

    return render(request, 'accounts/register.html')


@login_required
@user_passes_test(lambda user: user.profile.user_level, login_url='main:rights')
def users(request):
    userlist = User.objects.all()
    return render(request, 'accounts/users.html', {'users':userlist})

@login_required
def edit(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'accounts/edit.html', {'user':user})

def update_user(request, user_id):
    user = User.objects.filter(user_id=user_id)
    profile = Profile.objects.filter(user_id=user_id)
    password1 = request.POST['password1']
    password2 = request.POST['password2']
    user_level = request.POST['user_level']

    if password1 == password2:
        update_user = user.update(password=password1)
        update_profile = profile.update(user_level=user_level)

        update_user.save()
        update_profile.save()
        messages.info(request, 'User updated successfully')
        return redirect('accounts:users')
    else:
        messages.info(request, 'Passwords do not match')
        return redirect('accounts:users')

    

@login_required
def delete(request, user_id):
    #will use session dat for this
    pass

@user_passes_test(lambda user: user.is_authenticated, login_url='main:patients')
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('main:patients')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('accounts:login')

    return render(request, 'accounts/login.html')

def logout(request):
    auth.logout(request)
    return redirect('accounts:login')

def sendsms(request):
    # code to send sms
    # Your Account Sid and Auth Token from twilio.com/console
    # DANGER! This is insecure. See http://twil.io/secure
    
    # POST to db
    if request.method == "POST":
        patientname = request.POST['patientname']
        phonenumber = request.POST['phonenumber']
        patientmessage = request.POST['patientmessage']

        account_sid = 'ACe8ed5ccafe2c280d4148ef3971f6bdeb'
        auth_token = 'your authorization token goes here'
        client = Client(account_sid, auth_token)

        message = client.messages \
                        .create(
                            body= patientmessage,
                            from_='Twilio Assigned Phone Number goes here',
                            to= phonenumber
                        )
    return render(request, 'accounts/sendsms.html')

def patient(request):
    return render(request,'accounts/patient.html')
