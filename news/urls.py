from django.conf.urls import url
from news import views

# import datetime as dt

urlpatterns=[
    # url(r'^$', views.welcome, name = 'welcome'),
    url(r'^today/$', views.news_of_day, name = 'newsToday'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$', views.past_days_news, name = 'pastNews') 


]