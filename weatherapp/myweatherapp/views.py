import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
import requests
# Create your views here.

def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())



def fetch_data_from_api(request):
    api_key = "L46CQ7A9SG3ZRC8PJBLUGVE8Q"
    api_url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Kampala,UG?key={api_key}" 
    
    
    # Make a GET request to the API
    response = requests.get(api_url)
    if response.status_code == 200:
        formatted_data = response.json() # Formatting the JSON response
    else:
        formatted_data = None  # Handle cases where the response is not 200
    
    context = {
        'status_code': response.status_code,
        'data': formatted_data
    }
    
    # Render a template with the context
    return render(request, 'home.html', context)


