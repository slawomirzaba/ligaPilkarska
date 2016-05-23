from __future__ import unicode_literals
from django.db import models

class Club(models.Model):
    id = models.AutoField(primary_key = True, unique = True)
    name = models.CharField(max_length = 45, unique = True)
    creation_date = models.DateField()
    location = models.CharField(max_length = 45)

class Game(models.Model):
    id = models.AutoField(primary_key = True, unique = True)
    date = models.DateTimeField(null = True)
    host = models.ForeignKey(Club, related_name='host')
    guest = models.ForeignKey(Club, related_name='guest')
    number_of_queue = models.IntegerField()

class Person(models.Model):
    id = models.AutoField(primary_key = True, unique = True)
    name = models.CharField(max_length = 45)
    surname = models.CharField(max_length = 45)
    date_of_birth = models.DateField()
    club = models.ForeignKey(Club, null = True)

class Types_of_event(models.Model):
    id = models.AutoField(primary_key = True, unique = True)
    type = models.CharField(max_length = 45, unique = True)

class Event(models.Model):
    id = models.AutoField(primary_key = True, unique = True)
    minute = models.IntegerField()
    game = models.ForeignKey(Game)
    person = models.ForeignKey(Person)
    type = models.ForeignKey(Types_of_event)

class Transfer(models.Model):
    id = models.AutoField(primary_key = True, unique = True)
    quota = models.FloatField(null = True)
    date = models.DateField()
    new_club = models.ForeignKey(Club, related_name='new_club', null = True)
    old_club = models.ForeignKey(Club, related_name='old_club', null = True)
    player = models.ForeignKey(Person)

class Subcategorys_of_work(models.Model):
    id = models.AutoField(primary_key = True, unique = True)
    subcategory = models.CharField(max_length = 45, unique = True)

class Types_of_work(models.Model):
    id = models.AutoField(primary_key = True, unique = True)
    type = models.CharField(max_length = 45, null = True, unique = True)
    subcategory = models.ForeignKey(Subcategorys_of_work, null = True)

class Persons_history(models.Model):
    id = models.AutoField(primary_key = True, unique = True)
    start = models.DateField()
    end = models.DateField(null = True)
    person = models.ForeignKey(Person)
    type_of_work = models.ForeignKey(Types_of_work)

class Roles_in_game(models.Model):
    id = models.AutoField(primary_key = True, unique = True)
    role = models.CharField(max_length = 45, null = True, unique = True)

class Member_of_game(models.Model):
    id = models.AutoField(primary_key = True, unique = True)
    member = models.ForeignKey(Person)
    games = models.ManyToManyField(Game)
    roles = models.ManyToManyField(Roles_in_game)
