from django.contrib import admin
from django.urls import path, include 

from frontend.views import index, about, keys, borrow, history 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', index, name='index'),
    path('keys/', keys, name='keys'),
    path('borrow/', borrow, name='borrow'),
    path('history/', history, name='history'),
    path('about/', about, name='about'),
]

handler404 = 'frontend.views.handler404'