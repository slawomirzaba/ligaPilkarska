from django.contrib import admin
from models import *

class ClubAdmin(admin.ModelAdmin):
    model = Club
    list_display = ['name']

class GameAdmin(admin.ModelAdmin):
    model = Game
    list_display = ['number_of_queue', 'host', 'guest']

class PersonAdmin(admin.ModelAdmin):
    model = Person
    list_display = ['name', 'surname']


admin.site.register(Club, ClubAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Types_of_event)
admin.site.register(Event)
admin.site.register(Transfer)
admin.site.register(Subcategorys_of_work)
admin.site.register(Types_of_work)
admin.site.register(Persons_history)
admin.site.register(Roles_in_game)
admin.site.register(Member_of_game)
# Register your models here.
