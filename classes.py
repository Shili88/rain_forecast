class WeatherForecast:
    def __init__(self, cache=None):
        if not cache:
            self.storage = {}
        else:
            self.storage = cache

    def __setitem__ (self, date, resp):
        self.storage[date] = resp

    def __getitem__ (self, date):
        return self.storage.get(date)
    
    def __iter__ (self):
        for date in self.storage:
            yield date

    def items(self):
        for date, resp in self.storage.items():
            yield date, resp