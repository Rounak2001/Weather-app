from django.shortcuts import render
from django.contrib import messages
import requests
import datetime


def home(request):
   
    if 'city' in request.POST:
         city = request.POST['city']
    else:
         city = 'indore'     
    
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=b3653968a3a919a88a199712d75d3db5'
    PARAMS = {'units':'metric'}

    

    try:
          
          data = requests.get(url,params=PARAMS).json()
          description = data['weather'][0]['description']
          icon = data['weather'][0]['icon']
          temp = data['main']['temp']
          day = datetime.date.today()

          return render(request,'weatherapp/index.html' , {'description':description , 'icon':icon ,'temp':temp , 'day':day , 'city':city , 'exception_occurred':False})
    
    except KeyError:
          exception_occurred = True
          messages.error(request,'Entered data is not available to API')   
        
          day = datetime.date.today()

          return render(request,'weatherapp/index.html' ,{'description':'clear sky', 'icon':'01d'  ,'temp':25 , 'day':day , 'city':'Lucknow' , 'exception_occurred':exception_occurred } )
               
    
    