from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import logout

# Register View
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password1')
        confirm_password = request.POST.get('password2')

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already registered")
                return redirect('register')
            else:
                User.objects.create_user(username=username, email=email, password=password)
                messages.success(request, "Account created successfully!")
                return redirect('login')
        else:
            messages.error(request, "Passwords do not match")
            return redirect('register')
    return render(request, 'reg.html')


# Login View
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Invalid credentials")
            return redirect('login')
    return render(request, 'log.html')


# Logout View (Optional)
def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect('login')