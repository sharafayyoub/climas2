from stack import city_weather_stack

def show_gui():
    cities = [data.city for data in city_weather_stack.get_items()]

    print("Bienvenido al sistema de clima.")
    print("Seleccione una ciudad para ver los datos:")

    for index, city in enumerate(cities, start=1):
        print(f"{index}. {city}")

    try:
        selected_index = int(input("Ingrese el número de la ciudad: ")) - 1
    except ValueError:
        print("Selección inválida.")
        return

    if 0 <= selected_index < len(cities):
        selected_city = city_weather_stack.get_items()[selected_index]
        print(f"Datos de {selected_city.city}:")
        print(f"Temperatura mínima: {selected_city.min_temp}°C")
        print(f"Temperatura máxima: {selected_city.max_temp}°C")
        print(f"Soleado: {'Sí' if selected_city.is_sunny else 'No'}")
        print(f"Lluvia: {'Sí' if selected_city.is_raining else 'No'}")
        print(f"Fecha: {selected_city.date}")
        print(f"Estación: {selected_city.season}")
    else:
        print("Selección inválida.")
