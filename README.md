# Django-Challenge-Content

#### This is a project that helps to highlight the challenges faced by students when tackling Django content possible solutions.

###### For checking django version version after rnning the python3.6 shell, instead of using *django_get.version* use *django.VERSION*.

###### Instead of having two options on how to start django project we should have one with the dot at the end for good project structure alignment and to avoid confusing the students who might be new to coding or meeting django for the first time ie *django-admin startproject .* 

###### While importing views from the app(news) to urls in news *from . import views* instead of the dot(.) replace it with the name of the app (news) it should be *from news import views*

##### At the end of every topic as we start the development server, rem to add the URLS or paths which students should use to avoid them being confused

###### Add migration command after adding phone field to avoid getting programming error 

##### Making row image in article to have article_image = models.ImageField(upload_to = 'articles/', null=True, blank=True) for easier migration.

##### adding block condition to the article-image in the article file as showmn below
**{% if person.image %}
    *<img src="{{ person.image.url }}">*
{% endif %}**
 ### Add the following email configurations to settings.py
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'me@gmail.com'
EMAIL_HOST_PASSWORD = 'password'


*when adding class instances to model we should avoid use of plural since they are registered in databse in plural*