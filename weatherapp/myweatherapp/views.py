import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
from dotenv import load_dotenv
import os

# Load environment variables at the start of the application
load_dotenv()

def home(request):
    # Simply render the home template
    return render(request, 'home.html')

def fetch_data_from_api(request):
    load_dotenv()  # Load environment variables from the .env file
    city = request.GET.get('city')  # Get the city from the search query
    weather_data = None
    status_code = None
    error_message = None

    if city:
        api_key = os.getenv('WEATHER_API_KEY')  # Fetch API key from .env
        if not api_key:
            error_message = "API key is missing"
        else:
            api_url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city},UG?key={api_key}"
            try:
                response = requests.get(api_url)
                status_code = response.status_code

                if response.status_code == 200:
                    weather_data = response.json()
                    if weather_data and 'days' in weather_data and len(weather_data['days']) > 0:
                        last_day = weather_data['days'][-1] 
                else:
                    error_message = f"Failed to fetch data. Status code: {response.status_code}"
                    print(error_message)  # Debugging: Print any errors related to the API call

            except requests.exceptions.RequestException as e:
                error_message = f"An error occurred: {str(e)}"
                print(error_message)  # Debugging: Print if there's an exception

    context = {
        'weather_data': weather_data,
        'status_code': status_code,
        'city': city,
        'error_message': error_message,
        'last_day': last_day,
    }

    return render(request, 'home.html', context)

