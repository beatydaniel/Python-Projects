from django.db import models


# Create your models here.

class djangoClasses(models.Model):  # creates a class
    title = models.CharField(max_length=100, default="", blank=True, null=False)
    course_number = models.IntegerField(blank=True, null=False)
    instructor_name = models.CharField(max_length=60, default="", blank=True, null=False)
    duration = models.FloatField(blank=True, null=False)

    def __str__(self):
        return self.title  # sets the title to be displayed in the database
