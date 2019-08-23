from django.db import models

# Create your models here.
from django.db import models


class UserRec(models.Model):
    email = models.CharField(primary_key=True, max_length=255)
    password = models.CharField(max_length=16)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    
    class Meta:
        managed = False
        db_table = 'user_rec'


class AdminRec(models.Model):
    email = models.OneToOneField(UserRec, models.DO_NOTHING, db_column='email', primary_key=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'admin_rec'


class SingerRec(models.Model):
    email = models.OneToOneField(UserRec, models.DO_NOTHING, db_column='email', primary_key=True, max_length=255)
    
    class Meta:
        managed = False
        db_table = 'singer_rec'


class FileRec(models.Model):
    name = models.CharField(primary_key=True, max_length=200)
    location = models.CharField(max_length=255)
    size = models.PositiveIntegerField()
    format = models.CharField(max_length=10)
    date_added = models.DateField()
    file_type = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'file_rec'


class AccessRec(models.Model):
    user_email = models.OneToOneField('UserRec', models.DO_NOTHING, db_column='user_email', primary_key=True, max_length=255)
    file_name = models.ForeignKey('FileRec', models.DO_NOTHING, db_column='file_name')
    access_stamp = models.DateTimeField()
    query_type = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'access_rec'
        unique_together = (('user_email', 'file_name', 'access_stamp'),)


class Verification(models.Model):
    code = models.CharField(primary_key=True, max_length=10)
    in_use = models.BooleanField()
    user_type = models.CharField(max_length=6, db_column='user_type')
    class Meta:
        managed = False
        db_table = 'verification'

