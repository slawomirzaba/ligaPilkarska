from django import forms
from main.models import *


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
