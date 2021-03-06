from django import forms
from django.utils import timezone
from main.models import *
from django.forms.extras.widgets import SelectDateWidget
from datetimewidget.widgets import DateTimeWidget

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
         return obj.surname + " " + obj.name

class CustomGameChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
         return "{0} : {1} - {2}".format(obj.number_of_queue, obj.host.name, obj.guest.name)

class PersonForm(forms.ModelForm):
    club = CustomClubChoiceField(queryset=Club.objects.order_by('name'))

    class Meta:
        model = Person
        fields = '__all__'

class GameForm(forms.ModelForm):
    host = CustomClubChoiceField(queryset=Club.objects.order_by('name'), label="Gospodarz")
    guest = CustomClubChoiceField(queryset=Club.objects.order_by('name'), label="Gosc")
    date = forms.DateTimeField(widget=DateTimeWidget(usel10n=True, bootstrap_version=3), label = "Data")
    number_of_queue = forms.IntegerField(label = "Numer kolejki")
    class Meta:
        model = Game
        fields = '__all__'

class EventForm(forms.ModelForm):
    type = CustomEventTypeChoiceField(queryset=Types_of_event.objects.all(), label="Typ")
    person = CustomPersonChoiceField(queryset=Person.objects.order_by('surname'), label="Osoba")
    game = CustomGameChoiceField(queryset=Game.objects.order_by('number_of_queue'), label="Mecz")
    class Meta:
        model = Event
        fields = '__all__'

class Member_of_gameForm(forms.ModelForm):
    member = CustomPersonChoiceField(queryset=Person.objects.order_by('surname'), label='Uczestnik')
    games = customMultipleGamesChoiceField(queryset=Game.objects.order_by('number_of_queue'), widget=forms.CheckboxSelectMultiple, label='Mecze')
    roles = customMultipleRolesChoiceField(queryset=Roles_in_game.objects.all(), widget=forms.CheckboxSelectMultiple, label='Role')
    class Meta:
        model = Member_of_game
        fields = '__all__'

class Member_of_game_edit_Form(forms.ModelForm):
    games = customMultipleGamesChoiceField(queryset=Game.objects.order_by('number_of_queue'), widget=forms.CheckboxSelectMultiple, label='Mecze')
    roles = customMultipleRolesChoiceField(queryset=Roles_in_game.objects.all(), widget=forms.CheckboxSelectMultiple, label='Role')
    class Meta:
        model = Member_of_game
        fields = ('games', 'roles')

class ClubForm(forms.ModelForm):
    name = forms.CharField(max_length=45, min_length=6, strip=True, label='Nazwa')
    creation_date = forms.DateField(input_formats=None, label='Data powstania',
                                    widget = SelectDateWidget(years=[y for y in range(1930,2017)]), initial=timezone.now())
    location = forms.CharField(max_length=45, min_length=6, strip=True, label='Miejscowosc')

    class Meta:
        model = Club
        fields = "__all__"
