from django.shortcuts import render, reverse, render_to_response, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
import datetime
from datetime import date, datetime
from django.template import RequestContext
from os import path
from .models import FileRec
from haystack.views import SearchView

# Create your views here.
'''
def index(request):
    return render(request, 'member_site/index.html')

def login(request):
    email_input = request.POST['email']
    password_input = request.POST['password']
    users = UserRec.objects.filter(pk=email_input, password=password_input)
    rec_counter = 0
    found = False
    for u in users:
        rec_counter +=1
    if rec_counter == 1: #only one result - check for admin or singer
        admin_count = AdminRec.objects.filter(pk=email_input).count()
        if admin_count == 1:#one admin user found
            print("admin")
            admin = AdminRec.objects.get(pk=email_input)
            request.session['logged_in_user'] = email_input
            found = True
        else:
            #check singer
            singer_count = SingerRec.objects.filter(pk=email_input).count()
            if singer_count == 1:
                print("singer")
                singer = SingerRec.objects.get(pk=email_input)
                request.session['logged_in_user'] = email_input
                found = True
    if found:
        return HttpResponseRedirect(reverse('member_site:home'))
    else:
        messages.error(request, 'Email and/or password incorrect')
        return HttpResponseRedirect(reverse('member_site:home'))


def sign_up(request):
    #refer to sign up page
    return render(request, 'member_site/signup.html')


def process_signup(request):
    #validation of fields transferred by POST
    fname = request.POST['first_name']
    lname = request.POST['last_name']
    email_input = request.POST['email']
    password_input = request.POST['password']
    password_confirmation = request.POST['password_confirm']
    verification_code = request.POST['verif_code']
    validateSuccess = True
    if fname == "":
        messages.error(request, 'First name cannot be empty')
        validateSuccess = False;
    if lname == "":
        messages.error(request, 'Last name cannot be empty')
        validateSuccess = False;
    if email_input == "":
        messages.error(request, 'Email cannot be empty')
        validateSuccess = False
    if password_input == "":
        messages.error(request, 'Password cannot be empty')
        validateSuccess = False;
    if password_confirmation == "":
        messages.error(request, 'Password confirmation cannot be empty')
        validateSuccess = False;
    if password_input != password_confirmation:
        messages.error(request, 'Passwords need to match')
        validateSuccess = False
    code_count = Verification.objects.filter(pk=verification_code, in_use=True).count()
    if code_count != 1:
        messages.error(request, 'Verification code invalid')
        validateSuccess = False
    #get existing users from db
    users = UserRec.objects.filter(pk=email_input)
    if len(users) != 0:
        messages.error(request, "That email address already exists. Please try logging in.")
        validateSuccess = False
    if not validateSuccess:
        return redirect('member_site:signup')

    #entering new user into db
    #check type through user_type from codes
    codes = Verification.objects.filter(pk=verification_code, in_use=True)
    user_types_dic = codes.values('user_type').distinct()
    user_type_to_create = user_types_dic.values()[0]
    new_user = UserRec(email=email_input, password=password_input, fname=fname, lname=lname)
    new_user.save()
    if user_type_to_create == 'admin':
        new_admin = AdminRec(email=new_user)
        new_admin.save()
    else:
        new_singer = SingerRec(email=new_user)
        new_singer.save()

    return HttpResponseRedirect(reverse('member_site:signup_success'))

def home(request):
    if request.user.is_authenticated:
        return render(request, 'member_site/home.html')
    else:
        return HttpResponseRedirect(reverse('login'))

def search(request):
    if request.user.is_authenticated:
        keyword_list = request.GET['keywords'].split()
        files = FileRec.objects.filter(name__icontains=keyword_list[0])
        for keyword in keyword_list[1:]:
            # find keyword in any part of the file's record
            files = files | FileRec.objects.filter(location__icontains=keyword)
        files.order_by('name')
        # return list of files to results view
        return render(request, 'member_site/results.html', {'search_results': files.values()})
    else:
        return HttpResponseRedirect(reverse('login'))
'''

def details(request, name_display):
    if request.user.is_authenticated:
        to_display = get_object_or_404(FileRec, name=name_display)
        print(to_display)
        # test resource - of exists at this location
        if path.exists('/var/www/singongo.com/singongo/static/' + to_display.location):
            return render(request, 'member_site/details.html', {'display_obj': to_display})
        else:
            return HttpResponse('File does not exist')
    else:
        return HttpResponseRedirect(reverse('member_site:index'))


'''
def logout(request):
    if 'logged_in_user' in request.session:
        #clear session
        del request.session['logged_in_user']
        return render(request, 'member_site/logout.html')
    else:
        return HttpResponseRedirect(reverse('member_site:index'))

def signup_success(request):
    return render(request, 'member_site/signup_success.html')
'''
