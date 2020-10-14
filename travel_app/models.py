from django.db import models
from accounts.models import Account
from travel_book.choices import COUNTRIES




class Plan(models.Model):
    plan_title = models.CharField(max_length=25)
    task = models.CharField(max_length=25)
    description = models.TextField()

    def __str__(self):
        return f'Plan: {self.plan_title}'

    def get_detail_url(self):
        return f'/UpdatePlanView/{self.id}'

    def del_url(self):
        return f'/DeletePlanView/{self.id}'

class Travel(models.Model):

    MEAN_OF_TRANSPORT = [("plane","plane"), ("railway", "railway"), ("car", "car"), ("bus", "bus"), ("other", "other")]

    trip_title = models.CharField(max_length=255, unique=True)
    country = models.CharField(choices=(COUNTRIES), max_length=2)
    city = models.CharField(max_length=255, null=True, blank=True)
    start_date = models.DateTimeField(null=True, blank=True, auto_now=False, auto_now_add=False)
    end_date = models.DateTimeField(null=True, blank=True, auto_now=False, auto_now_add=False)
    mean_of_transport = models.CharField(max_length=20, choices=MEAN_OF_TRANSPORT, default="other")
    travelers = models.ManyToManyField(Account, related_name="Travelers", blank=True) #, null= True
    trip_plan = models.OneToOneField(Plan, on_delete=models.CASCADE, null=True, blank=True)
    comments = models.TextField(null=True, blank=True)
    budget = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.trip_title

    def get_detail_url(self):
        return f'/UpdateTravelView/{self.id}'

    def del_url(self):
        return f'/DeleteTravelView/{self.id}'



# class Travel_Journal(models.Model):
#     # travel = models.OneToOneField(Travel, on_delete=models.CASCADE, null=True, blank=True)
#     journal_title = models.CharField(max_length=50)
#     places = models.TextField()
#     start_date = models.DateTimeField(null=True, blank=True)
#     end_date = models.DateTimeField(null=True, blank=True)
#     best_moments = models.TextField(default=None, null=True, blank=True)
#     best_pictures = models.ImageField(default=None, null=True, blank=True)
#     travelers_in_journal = models.ManyToManyField(Account, related_name="Travelers_in_journal",
#                                        blank=True) #on_delete=models.CASCADE,
#
#     def __str__(self):
#         return self.journal_title
#
#     def get_detail_url(self):
#         return f'/UpdateJournalView/{self.id}'
#
#     def del_url(self):
#         return f'/DeleteJournalView/{self.id}'
#
class City(models.Model):
    city_name = models.CharField(max_length=50, verbose_name="City to visit")
    tourist_info_adress = models.CharField(max_length=255, verbose_name="Tourist info details",  null=True, blank=True)
    places_worth_visiting = models.TextField(verbose_name="Places to visit", null=True, blank=True)
    restaurants = models.TextField(verbose_name="Restaurants", null=True, blank=True)
    # * map z googlemaps.
    # * weather = models.CharField(max_length=100) lub z api

    def __str__(self):
        return self.city_name

    def get_detail_url(self):
        return f'/UpdateCityView/{self.id}'

    def del_url(self):
        return f'/DeleteCityView/{self.id}'
#
#
#
class Blog(models.Model):
    author = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    post_title = models.CharField(max_length=50, verbose_name="Title")
    date_of_creation = models.DateTimeField(auto_now=True, verbose_name="Date")
    post_image = models.ImageField(verbose_name="Pictures", null=True, blank=True)
    text = models.TextField()


    def __str__(self):
        return f"""Title: {self.post_title}, \n
        published on: {self.date_of_creation} by {self.author}, \n
        {self.post_image} \n
        Text: n\
        {self.text}"""

    def get_detail_url(self):
        return f'/UpdateBlogView/{self.id}'

    def del_url(self):
        return f'/DeleteBlogView/{self.id}'

#
#
#
