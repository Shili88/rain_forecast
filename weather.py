import requests
from datetime import datetime, timedelta
import os 
import json

from classes import WeatherForecast
cache = WeatherForecast()

# Load cache 
def load_cache():
    cache_file_path = os.path.join("data", "cache.json")
    if not os.path.exists(cache_file_path):
        print("Cache not existing.....")
        cache = WeatherForecast()
        return cache
    with open (cache_file_path)as f:
        print("Loading cache.....")
        cache = WeatherForecast(cache = json.load(f))
        return cache
#save cache
def save_cache(cache):
    cache_file_path = os.path.join("data", "cache.json")
    with open(cache_file_path, "w")as f:
        json.dump(cache.storage, f)

def get_weather_info (searched_date: str, latitude: str, longitude: str, cache):
    if cache[searched_date]:
        print ("Date in the cache.")
        return cache[searched_date]
    url = "https://api.open-meteo.com/v1/forecast"
    # set params
    params = {
        "latitude": latitude,
        "longitude": longitude, 
        "daily": "precipitation_sum", 
        "timezone": "Europe/Dublin",
        "start_date": searched_date, 
        "end_date": searched_date
    }
    response = requests.get(url, params=params) 
    print(response.json())     
    # Issue prevent 
    if not response.ok:
        print(f"Error {response.status_code} while fetching from the api: {response.text}")
    rain = response.json()['daily']['precipitation_sum'][0]
    cache[searched_date] = rain
    save_cache(cache)
    return rain

if __name__ == "__main__":
    print("Runing code...")
    #Dublin for tests
    lat = 53.3331
    long = -6.2489
    # Date info
    date = input("Enter the date with this format YYYY-mm-dd  (or press the 'Enter' for the next day): ")
    if not date: 
        date = (datetime.now().date() + timedelta(days=1)).strftime("%Y-%m-%d")
    print(f"Date: {date}")

    #Fetch the data from API
    cache = load_cache()
    resp = get_weather_info(searched_date=date, latitude=lat, longitude=long, cache=cache)

    if resp > 0:
        print("It is raining day, prepare the umbrella...")
    elif resp == 0:
        print("No rain today. It's sunny day!!!")
    else:
        print("No data, do not know the forecast.")
    save_cache(cache)