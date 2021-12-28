import tkinter as tk
import tkinter.ttk as ttk
import model

airports = model.get_all_airports()
cities = model.get_cities()
countries = model.get_countries()

def search():
    city = city_box.get()
    if airports_listbox.size() > 0:
        airports_listbox.delete(0, tk.END)
    airports_in_city = []
    for a in airports:
        if a.city == city:
            airports_in_city.append(a)
    for a in range(0, len(airports_in_city)):
        airports_listbox.insert(a, airports_in_city[a])


def set_basic_view():
    city_label = tk.Label(app, text="Choose City")
    city_label.pack()
    city_box = ttk.Combobox(app, values=cities)
    city_box.pack()

    search_btn = tk.Button(app, text="Search Airports", width=12, command=search)
    search_btn.pack()

    airports_listbox = tk.Listbox(width=50)
    airports_listbox.pack()

    return city_box, airports_listbox


app = tk.Tk()
app.title('Airports')
app.geometry("500x300")

view_elements = set_basic_view()
city_box = view_elements[0]
airports_listbox = view_elements[1]

app.mainloop()
