import tkinter as tk
from stack import city_weather_stack

def show_gui():
    def show_city_data():
        try:
            selected_index = city_listbox.curselection()[0]
            selected_city = city_weather_stack.get_items()[selected_index]

            # Crear una nueva ventana para mostrar los datos
            new_window = tk.Toplevel(root)
            new_window.title(f"Datos de {selected_city.city}")

            tk.Label(new_window, text=f"Ciudad: {selected_city.city}").pack(pady=5)
            tk.Label(new_window, text=f"Temperatura mínima: {selected_city.min_temp}°C").pack(pady=5)
            tk.Label(new_window, text=f"Temperatura máxima: {selected_city.max_temp}°C").pack(pady=5)
            tk.Label(new_window, text=f"Soleado: {'Sí' if selected_city.is_sunny else 'No'}").pack(pady=5)
            tk.Label(new_window, text=f"Lluvia: {'Sí' if selected_city.is_raining else 'No'}").pack(pady=5)
            tk.Label(new_window, text=f"Fecha: {selected_city.date}").pack(pady=5)
            tk.Label(new_window, text=f"Estación: {selected_city.season}").pack(pady=5)

            tk.Button(new_window, text="Cerrar", command=new_window.destroy).pack(pady=10)
        except IndexError:
            tk.messagebox.showerror("Error", "Por favor, seleccione una ciudad.")

    root = tk.Tk()
    root.title("Sistema de Clima")

    tk.Label(root, text="Seleccione una ciudad para ver los datos:").pack(pady=10)

    city_listbox = tk.Listbox(root, height=10, width=30)
    city_listbox.pack(pady=10)

    for city in [data.city for data in city_weather_stack.get_items()]:
        city_listbox.insert(tk.END, city)

    tk.Button(root, text="Mostrar Datos", command=show_city_data).pack(pady=10)

    root.mainloop()
