from django.db import models

class User(models.Model):
    name=models.CharField(max_length=100)
    id=models.IntegerField(primary_key=True,auto_created=True)
    date_of_birth=models.DateField()
    
    
class Todo(models.Model):
    CHOICES = [
        ("L","LOW"),
        ("M","MEDIUM"),
        ("H","HIGH"),
    ]
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    desc=models.CharField(max_length=100)
    user=models.ForeignKey(User,on_delete=models.CASCADE) # if user is deleted, corresponding todo also gets deleted
    priority=models.CharField(max_length=1,choices=CHOICES)   #retrieved by object.get_priority_display()
    
            
# Create your models here.
