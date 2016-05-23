from django.contrib import admin
from models import *
from main.forms import *

class ClubAdmin(admin.ModelAdmin):
    model = Club
    list_display = ['name']

class GameAdmin(admin.ModelAdmin):
    model = Game
    form = GameForm
    list_display = ['number_of_queue', 'get_host', 'get_guest']

    def get_host(self, obj):
        return obj.host.name
    def get_guest(self, obj):
        return obj.guest.name

class PersonAdmin(admin.ModelAdmin):
    model = Person
    form = PersonForm
    list_display = ['name', 'surname']

class Types_of_eventAdmin(admin.ModelAdmin):
    model = Types_of_event
    list_display = ['type']

class EventAdmin(admin.ModelAdmin):
    model = Event
    form = EventForm
    list_display = ['minute', 'get_person', 'get_type', 'get_game']

    def get_person(self, obj):
        return obj.person.name + " " + obj.person.surname
    def get_type(self, obj):
        return obj.type.type
    def get_game(self, obj):
        return "{0} : {1} - {2}".format(obj.game.number_of_queue, obj.game.host.name, obj.game.guest.name)

class Roles_in_gameAdmin(admin.ModelAdmin):
    model = Roles_in_game
    list_display = ['role']

class Member_of_gameAdmin(admin.ModelAdmin):
    model = Member_of_game
    form = Member_of_gameForm
    list_display = ['get_member']

    def get_member(self, obj):
        return obj.member.name + " " + obj.member.surname

admin.site.register(Club, ClubAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Types_of_event, Types_of_eventAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Transfer)
admin.site.register(Subcategorys_of_work)
admin.site.register(Types_of_work)
admin.site.register(Persons_history)
admin.site.register(Roles_in_game, Roles_in_gameAdmin)
admin.site.register(Member_of_game, Member_of_gameAdmin)
# Register your models here.
