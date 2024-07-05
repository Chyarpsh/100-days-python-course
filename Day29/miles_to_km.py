from tkinter import *

def calculate():
    miles = float(miles_input.get)
    km: float = miles * 1.689
    kilometer_label.config(text = f"{km})


window = Tk()
window.title("Miles to Km Converter")
window.config(padx=50, pady=50)

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0, row=1)

km_before_calculation = Label(text="0")
km_before_calculation.grid(column=1, row=2)

button = Button(text="Calculate" , command = calculate)
button.grid(column=1, row=1)





window.mainloop()
