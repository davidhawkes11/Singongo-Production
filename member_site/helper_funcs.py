from .models import FileRec
import os
import time
import datetime

def checkIsDigit(character):
    return character >= '0' and character <= '9'

def test_upload():
    new_file = FileRec(name='TestDoc', size=1000, format='pdf', date_added='2019-07-08', file_type='D')
    new_file.save()
    print('Success')

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
walk_dir('C://Users//Lloyd Warren//PycharmProjects//SingGongGo-Website//static//member_site')

