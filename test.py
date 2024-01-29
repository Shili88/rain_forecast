import requests
from datetime import datetime, timedelta

def get_weather_info (searched_date: str, latitude: str, longitude: str):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude, 
        "daily": "precipitation_sum", 
        "timezone": "Europe/London",
        "start_date": searched_date, 
        "end_date": searched_date
    }
    response = requests.get(url, params=params)
    if not response.ok:
        print(f"Error {response.status_code} while fetching from the api: {response.text}")
    return response.json()

if __name__ == "__main__":
    print("Runing code...")
    #London for tests
    lat = 51.509865
    long = -0.118092
    # Date info
    date = input("Enter the date with this format YYYY-mm-dd  (or press the 'Enter' for the next day): ")
    if not date: 
        date = datetime.now().date() + timedelta(days=1)
    print(f"Date: {date}")

    resp = get_weather_info(searched_date=date, latitude=lat, longitude=long)

    print(resp)