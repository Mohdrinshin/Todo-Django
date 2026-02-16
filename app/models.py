from django.db import models

from django.contrib.auth.models import User


class TaskModel(models.Model):

    taskname = models.CharField(max_length=100 , unique=True)

    created_date = models.DateField(auto_now_add=True)

    due_date = models.DateField()

    description = models.TextField(null=True , blank=True) #optional 

    category = [('work','work'),
                ('personal','personal'),
                ('urgent','urgent')]
    
    task_category = models.CharField(max_length=100,choices=category, default='work')
    
    completed_status = models.BooleanField(default=False)

    user_id = models.ForeignKey(User,on_delete=models.CASCADE) # better variable name user aanu use_id alla 

    def __str__(self):
        return self.taskname


class OtpModel(models.Model):

    otp = models.IntegerField()

    user_id = models.ForeignKey(User,on_delete=models.CASCADE)

    created_at =models.DateField(auto_now_add=True) 
