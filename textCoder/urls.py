from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^login/',views.login, name='login'),
    url(r'^register/',views.register, name='register'),
    url(r'^cleaner/',views.cleaner, name='cleaner'),
    url(r'^logout/',views.logout, name='logout'),
    url(r'^coder/', views.index, name='coder'),
    url(r'^textcode/', views.textCode, name='textCoder')
]