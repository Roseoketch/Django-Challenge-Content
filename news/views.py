from django.shortcuts import render
from django.http import HttpResponse

import datetime as dt

# Create your views here.
def welcome(request):
  return HttpResponse('welcome to the Moringa tribune')


  def news_of_day(request):
    date = da.date.today()
    html =f'''
      <html>
        <body>
          <h1>{date.day}-{date.month}-{date.year}</h1>

        </body>
      </html>
           '''
    return HttpResponse(html)