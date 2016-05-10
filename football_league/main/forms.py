from django import forms
from main.models import *

class customMultipleGamesChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
         return "{0} : {1} - {2}".format(obj.number_of_queue, obj.host.name, obj.guest.name)

class customMultipleRolesChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
         return obj.role

class CustomClubChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
         return obj.name

class CustomEventTypeChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
         return obj.type

class CustomPersonChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
         return obj.name + " " + obj.surname

class CustomGameChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
         return "{0} : {1} - {2}".format(obj.number_of_queue, obj.host.name, obj.guest.name)

class PersonForm(forms.ModelForm):
    club = CustomClubChoiceField(queryset=Club.objects.all())

    class Meta:
        model = Person
        fields = '__all__'

class GameForm(forms.ModelForm):
    host = CustomClubChoiceField(queryset=Club.objects.all())
    guest = CustomClubChoiceField(queryset=Club.objects.all())

    class Meta:
        model = Game
        fields = '__all__'

class EventForm(forms.ModelForm):
    type = CustomEventTypeChoiceField(queryset=Types_of_event.objects.all())
    person = CustomPersonChoiceField(queryset=Person.objects.all())
    game = CustomGameChoiceField(queryset=Game.objects.all())
    class Meta:
        model = Event
        fields = '__all__'

class Member_of_gameForm(forms.ModelForm):
    member = CustomPersonChoiceField(queryset=Person.objects.all())
    games = customMultipleGamesChoiceField(queryset=Game.objects.all(), widget=forms.CheckboxSelectMultiple)
    roles = customMultipleRolesChoiceField(queryset=Roles_in_game.objects.all(), widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Member_of_game
        fields = '__all__'
