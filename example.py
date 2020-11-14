import requests, json
from datetime import datetime as dt

# Reference for Accuweather API Documentation
# https://developer.accuweather.com/apis

# Store your apikey for AccuWeather in a file for security
apiKey = open('apikey.txt','r').read()

# Search for a location. We need the location key to search for weather results
# Documentation for location key search
# https://developer.accuweather.com/accuweather-locations-api/apis/get/locations/v1/cities/search
locationText = input('Place to find: ')
payload = {'apikey': apiKey, 'q': locationText}

url = "http://dataservice.accuweather.com/locations/v1/cities/search"
response = requests.request("GET", url, params=payload)

# The actual url request
print('The url of the REST API Request')
print(response.request.url)
print()

# The full data response in json format
#print('The JSON data response')
#print(response.text)
#print()

# Get just the location key from the JSON response
print('Parsing out the location key (there may be more than one)')
jobj = json.loads(response.text)
locations = [(loc['Key'], loc['LocalizedName'], loc['AdministrativeArea']['ID'], loc['AdministrativeArea']['CountryID']) for loc in jobj]
for loc in locations:
    print(*loc, sep=', ')

# Only pull weather for one response... the location key is a 5+ digit code reported in prior output
# Documentation for 5-day forecast API
# https://developer.accuweather.com/accuweather-forecast-api/apis/get/forecasts/v1/daily/5day/%7BlocationKey%7D

# This is a new request
payload = {'apikey': apiKey}

key = input('Which location key do you want to use?')
# Request for details on the selected location key
url = 'http://dataservice.accuweather.com/locations/v1/' + key
response = requests.request('GET', url, params=payload)
loc = json.loads(response.text)
city, state, country = loc['LocalizedName'], loc['AdministrativeArea']['ID'], loc['AdministrativeArea']['CountryID']

# Five day forecast
url = 'http://dataservice.accuweather.com/forecasts/v1/daily/5day/' + key
response = requests.request('GET', url, params=payload)

# print the new request URL
print('5-day forecast URL for request')
print(response.request.url)
print()

# print the data retrieved
print('5-day forecast data')
jobj = json.loads(response.text)
print(json.dumps(jobj, indent=4))
print()

# parse the results... refer to the documentation for the meanings of the data
print('Forecast for', city, state, country)
for forecast in jobj['DailyForecasts']:
    forecast_date = dt.strptime(forecast['Date'][:10], '%Y-%m-%d')
    high = forecast['Temperature']['Maximum']
    low = forecast['Temperature']['Minimum']
    print(forecast_date, high['Value'], high['Unit'], low['Value'], low['Unit'])

