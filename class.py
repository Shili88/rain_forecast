class weather_forecast: 
    def __init__(self):
        self.weather = {}
    
    def __setitem__(self, date, get_weather_info):
        self.weather[date] = get_weather_info

    def __getitem__(self, date):
        return self.weather[date]

    def __iter__(self):
        for date, get_weather_info in self.weather:
            yield date, get_weather_info

    def items(self):
        for date, get_weather_info in self.weather.items():
            yield date, get_weather_info