from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .models import Member


def members(request):
    mymembers = Member.objects.all().values()

    template = loader.get_template('all_members.html')

    context = {
        'mymembers': mymembers,
    }

    return HttpResponse(template.render(context, request))


def details(request, id):
    mymember = Member.objects.get(id=id)

    template = loader.get_template('details.html')

    context = {
        'mymember': mymember,
    }

    return HttpResponse(template.render(context, request))


def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())


# REGISTRATION
def register(request):

    if request.method == "POST":

        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirmpassword = request.POST.get("confirmpassword")

        # Check passwords
        if password != confirmpassword:
            return render(request, "register.html", {
                "error": "Passwords do not match"
            })

        # Check email
        if User.objects.filter(username=email).exists():
            return render(request, "register.html", {
                "error": "Email already registered"
            })

        # Create user
        User.objects.create_user(
            username=email,
            first_name=firstname,
            last_name=lastname,
            email=email,
            password=password
        )

        # Go to login
        return redirect("login")

    return render(request, "register.html")


# LOGIN
def user_login(request):

    if request.method == "POST":

        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=email,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect("admin_details")

        else:

            return render(request, "login.html", {
                "error": "Invalid email or password"
            })

    return render(request, "login.html")


# ADMIN DETAILS
@login_required
def admin_details(request):

    return render(request, "admin_details.html")


# FORGOT PASSWORD
def forgot_password(request):

    return render(request, "forgot_password.html")