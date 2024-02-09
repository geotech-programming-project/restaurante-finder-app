from django.db import models
import datetime
# Create your models here.
class Restaurant(models.Model):
    # Define choices for the name of universities
    university_choices = (
        ("UNL","Universidade Nova de Lisboa"),
        ("UM","University of Münster"),
        ("UJI","Universitat Jaume I"),
    )
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=30)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    latitude = models.FloatField()
    longtitude = models.FloatField()
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    university = models.CharField(max_length=4, choices = university_choices, blank=True)
    type_food = models.TextField(blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d', blank=False)
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    
    is_published = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name