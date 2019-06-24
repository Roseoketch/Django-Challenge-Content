from django.conf.urls import url
from . import views

# import datetime as dt

urlpatterns=[
    url('^$', views.welcome,name = 'welcome'),
    url('^today/$',views.news_of_day,name='newsToday')

]