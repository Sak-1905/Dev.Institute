from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Card,User
from django.http import HttpResponse
import requests

# Create your views here.

def cards(request):
    #display all cards
    pass


def display_card(request):
    #display one card
    pass

def user_profile(request):
    #display user profile
    pass

def buy_card(request):
    #buy card
    pass

def sell_card(request):
    #sell card
    pass

def populate(request):
    #populate database
    api_url = "https://hp-api.onrender.com/api/characters"  # Replace with the API URL

    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            print(len(data))
            for item in data:
                #print(item)
                if 'id' in item and 'name' in item and 'species' in item and 'house' in item and 'image' in item and 'dateOfBirth' in item and 'patronus' in item:
                    if item['dateOfBirth'] == None:
                        item['dateOfBirth'] = 'Unknown'
                        
                    model_instance = Card(
                        id=item['id'],
                        name_character=item['name'],
                        species=item['species'],
                        house=item['house'],
                        image_url=item['image'],
                        date_of_birth=item['dateOfBirth'],
                        patronus=item['patronus']
                    )
                    model_instance.save()
            # print(data[0])
            print("Data populated successfully!")
        else:
            print("Failed to fetch data from the API.")
    except requests.exceptions.RequestException as e:
        print("Error while making API request:", e)

    return HttpResponse("Running")