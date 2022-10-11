from django.db import models


# билеты
class Tickets(models.Model):
    number_ticket = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    hall = models.IntegerField()
    row = models.IntegerField
    place = models.IntegerField
    sales = models.IntegerField
    pass


# цены
class Price(models.Model):
    date = models.DateField()
    time = models.TimeField
    category = models.TextField()
    price = models.FloatField()
    pass


# категории мест
class PlaceCategories(models.Model):
    place_categories = models.TextField()
    pass


# места и ряды
class SeatsRows(models.Model):
    hall = models.IntegerField()
    row = models.IntegerField()
    place = models.IntegerField()
    category = models.TextField()
    pass


# залы
class Halls(models.Model):
    room_code = models.IntegerField()
    hall_name = models.TextField()
    pass


# фильмы
class Movies(models.Model):
    movie_code = models.IntegerField()
    movie_title = models.TextField()
    production = models.TextField()
    year_issue = models.DateField()
    genre = models.TextField()
    duration = models.DurationField()
    pass


# сеансы
class Sessions(models.Model):
    date = models.DateField()
    time = models.TimeField()
    hall = models.IntegerField()
    movie = models.TextField()
    pass


# страны
class Countries(models.Model):
    countries = models.TextField()
    pass


# жанры
class Genres(models.Model):
    genres = models.TextField()
    pass
