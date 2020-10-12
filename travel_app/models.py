from django.db import models

# Create your models here.

class Travel(models.Model):

    MEAN_OF_TRANSPORT = [(plane ,"plane"), (railway, "railway"), (car, "car"), (bus, "bus"), (other, "other")]

    trip_title = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255, null=True, blank=True)      #czy te blanki to już tutaj, jak potem będę tworzyć ModelForms w form.py?
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    mean_of_transport = models.CharField(max_length=20, choices=MEAN_OF_TRANSPORT, default="other")
    travelers = models.ManyToManyField("User", on_delete=models.CASCADE, related_name="Travelers", null=True, blank=True)
    trip_plan = models.OneToOneField("Plan", on_delete=models.CASCADE, null=True, blank=True)
    comments = models.TextField(null=True, blank=True)
    budget = models.IntegerField(null=True, blank=True)

class Plan(models.Model):
    plan_title = models.CharField(max_length=25)
    task = models.CharField(max_length=25)
    description = models.TextField()

class Travel_Journal(models.Model):
    journal_title = models.CharField(max_length=50)
    places = models.TextField()
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    best_moments = models.TextField()
    best_pictures = models.ImageField()
    travelers = models.ManyToManyField("User", on_delete=models.CASCADE, related_name="Travelers", null=True,
                                       blank=True)

class City(models.Model):
    city_name = models.CharField(max_length=50)
    tourist_info_adress = models.CharField(max_length=255)
    places_worth_visiting = models.TextField()
    best_restuarnts = models.TextField()
    # * map z googlemaps.
    # * weather = models.CharField(max_length=100) lub z api


class Blog(models.Model):
    author = models.ForeignKey("User", on_delete=models.SET_NULL) #chciałam SET_DEFAULT, ale nie bardzo wiem jak ustawić wartość np. author unknown, jęlsi autor już nie jest userem.

class Post(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, realted_name="Blog")
    post_title = models.CharField(max_length=50)
    date_of_creation = models.DateTimeField(auto_now=True)
    post_image = models.ImageField()




