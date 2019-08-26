from django.db import models

# Create your models here.
from django.db import models

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

