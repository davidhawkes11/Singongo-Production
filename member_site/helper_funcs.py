from .models import FileRec
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordResetForm
import os
import time
import datetime

def walk_dir(dir_path):
    counter = 0
    print(dir_path)
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            f_name = file.split('.')[0]
            file_path = os.path.join(root, file)
            f_size = os.path.getsize(file_path)
            datetime_mod = time.gmtime(os.path.getmtime(file_path))
            day = datetime_mod.tm_mday
            year = datetime_mod.tm_year
            month = datetime_mod.tm_mon
            date_mod = datetime.datetime(year, month, day)
            file_format = file.split('.')[1]
            print(file_format)
            f_type = ''
            valid = True
            if file_format == 'pdf':
                f_type = 'doc'
            elif file_format == 'mp3' or file_format == 'm4a':
                f_type = 'audio'
            elif file_format == 'mp4' or file_format == 'MOV':
                f_type = 'video'
            elif file_format == 'jpg':
                f_type = 'img'
            else:
                valid = False
            if valid:
                new_file = FileRec(name=f_name, location=str(file_path), size=f_size, format=file_format, date_added=date_mod, file_type=f_type)
                new_file.save()
            counter += 1
    print('Saved {} files.'.format(counter))

def create_users(file_name):
    email_file = open(file_name, 'r')
    emails = email_file.readlines()
    for email in emails:
        if email.__contains__('@') and email.__contains__('.'):
            user = User.objects.create_user(username=email, password='orange&black', email=email)
            user.save();
            password_reset = PasswordResetForm({'email':email})
            password_reset.save();
        else:
            print("Invalid email " + email)
