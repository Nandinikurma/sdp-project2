from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
   # path('admin/', admin.site.urls),
    path("hello2/",hello1),
    path('hello/',hello,name='hello'),
    path('',newhomepage,name='newhomepage'),
    path('card/',travelpackage,name='travelpackage'),
    path('print/',print_to_console,name='print_to_console'),
    path('p/',print1,name='print1'),
    path('ran1/', ran, name='ran'),
    path('ran/', random123, name='random123'),
    path('g/',getdate1,name='getdate1'),
    path('getdate/',get_date,name='get_date'),
    path('t/',timezfunc,name='timezfunc'),
    path('functioncall/',functioncall,name='functioncall'),
    path('registerloginfunction/',registerloginfunction,name='registerloginfunction'),
    path('Pie_chart/',pie_chart,name='Pie_chart'),
    path('Destination/', Destination, name='Destination'),
    path('weatherpagecall/', weatherpagecall, name='weatherpagecall'),
    path('weatherlogic/', weatherlogic, name='weatherlogic'),

]