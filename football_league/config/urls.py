"""football_league URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from main.views.Home import Home
from main.views.Calendar import Calendar
from main.views.Tables_management import Tables_management
from main.views.Tables_management_clubs import Tables_management_clubs
from main.views.Tables_management_clubs_add import Tables_management_clubs_add
from main.views.Tables_management_clubs_edit import Tables_management_clubs_edit
from main.views.Tables_management_clubs_delete import Tables_management_clubs_delete
from main.views.Tables_management_games import Tables_management_games

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', Home.as_view(), name='home'),
    url(r'^table$', Home.as_view(), name='home'),
    url(r'^calendar$', Calendar.as_view(), name='calendar'),
    url(r'^tables_management$', Tables_management.as_view(), name='tables_management'),
    url(r'^tables_management_clubs$', Tables_management_clubs.as_view(), name='tables_management_clubs'),
    url(r'^tables_management_clubs_add', Tables_management_clubs_add.as_view(), name='tables_management_clubs_add'),
    url(r'^tables_management_clubs_edit/(?P<id>\d+)/$', Tables_management_clubs_edit.as_view(), name='tables_management_clubs_edit'),
    url(r'^tables_management_clubs_delete/(?P<id>\d+)/$', Tables_management_clubs_delete.as_view(), name='tables_management_clubs_delete'),
    url(r'^tables_management_games$', Tables_management_games.as_view(), name='tables_management_games'),

]
