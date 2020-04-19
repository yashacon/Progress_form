from django.db import models

import os

def get_upload_path(instance, filename):
    fileName, fileExtension = os.path.splitext(filename)
    return os.path.join(
      "user_%s" % instance.Name,"user_{0}.{1}" .format(instance.Name,fileExtension))
def next_upload_path(instance, filename):
    fileName, fileExtension = os.path.splitext(filename)
    return os.path.join(
      "user_%s's Next plan" % instance.Name,"user_{0}.{1}" .format(instance.Name,fileExtension))

Report_choice=(
    ("Daily","Daily"),
    ("Weekly","Weekly"),
    ("Monthly","Monthly"),

)
Team_Lead=(
    ("Raktima Mitra","Raktima Mitra"),
    ("Akansha","Akansha"),
    ("Amitesh Ranjan","Amitesh Ranjan"),
    ("Shekhar","Shekhar"),
    ("Ajeet","Ajeet"),
    ("Sheetal","Sheetal"),
    ("Kanika","Kanika"),
)
class Report(models.Model):
    Name=models.CharField(blank=False,max_length=20)
    date=models.DateField('Date',blank=False)
    reports=models.CharField(choices=Report_choice,default='Daily',max_length=10)
    TL=models.CharField(choices=Team_Lead,default='Kanika',max_length=20)
    No_hours=models.IntegerField(blank=False)
    progress=models.CharField(blank=False,max_length=200)
    Dtoday=models.FileField(upload_to=get_upload_path,blank=True)
    concern=models.CharField(max_length=200,blank=True)
    Nextplan=models.CharField(max_length=200,blank=True)
    Dnextp=models.FileField(upload_to=next_upload_path,blank=True)
    def __str__(self):
        return self.Name