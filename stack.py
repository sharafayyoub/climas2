import random

class CityWeather:
    def __init__(self, city, min_temp, max_temp, is_sunny, is_raining, date, season):
        self.city = city
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.is_sunny = is_sunny
        self.is_raining = is_raining
        self.date = date
        self.season = season

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if not self.is_empty() else None

    def peek(self):
        return self.items[-1] if not self.is_empty() else None

    def is_empty(self):
        return len(self.items) == 0

    def get_items(self):
        return self.items[:]

city_weather_stack = Stack()

# Datos de ejemplo
cities = [
    "Madrid", "Barcelona", "Valencia", "Sevilla", "Zaragoza",
    "Málaga", "Murcia", "Palma", "Bilbao", "Alicante"
]

seasons = ["Primavera", "Verano", "Otoño", "Invierno"]

for city in cities:
    city_weather_stack.push(CityWeather(
        city=city,
        min_temp=random.randint(0, 14),
        max_temp=random.randint(15, 29),
        is_sunny=random.choice([True, False]),
        is_raining=random.choice([True, False]),
        date=f"{random.randint(1, 28)}/{random.randint(1, 12)}/2023",
        season=random.choice(seasons)
    ))
