from django.db import models

# Create your models here.
PREFIX ={
    ('Mr','Mr'),
    ('Mrs','Mrs'),
    ('Ms','Ms'),
    ('Miss','Miss'),
}


class Profile(models.Model):
    prefix = models.CharField(max_length=50, choices=PREFIX)
    first_name = models.CharField(max_length=50,default='',blank=True,null=False)
    last_name = models.CharField(max_length=50,default='',blank=True)
    email= models.CharField(max_length=50,default='',blank=True)
    user_name=models.CharField(max_length=50,default='',blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.first_name