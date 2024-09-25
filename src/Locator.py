from geopy.geocoders import Nominatim
from tkinter import messagebox 
from tkinter import *
 
def getinfo():
    geolocator = Nominatim(user_agent = "geoapiExercises")
    place = e.get()
    place_res.set(place)
    location = geolocator.geocode(place)
    res.set(location)
 
master = Tk()
master.title("Country Identifier")
master.configure(bg = 'silver')

place_res = StringVar();
res = StringVar(); 
Label(master, text = "Enter location:" ,
      bg = "silver").grid(row = 0, sticky = W)
Label(master, text = "Location:" ,
      bg = "silver").grid(row = 1, sticky = W)
Label(master, text = "Country address :" ,
      bg = "silver").grid(row = 2, sticky = W)
 
Label(master, text = "", textvariable = place_res,
      bg = "silver").grid(row = 1, column = 1, sticky = W)
Label(master, text = "", textvariable = res,
      bg = "silver").grid(row = 2, column = 1, sticky = W)
 
e = Entry(master)
e.grid(row = 0, column = 1)
 
b = Button(master, text = "Show", command = getinfo )
b.grid(row = 0, column = 2, columnspan = 2,
       rowspan = 2, padx = 5, pady = 5)
 
mainloop()
