from tkinter import *


def calculate():
    miles = float(miles_input.get())
    km = miles * 1.609
    value_before_calculation.config(text=f"{km}")


window = Tk()
window.title("Miles_to_Kilometer")
window.config(padx=50, pady=50)

#Label
is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)

value_before_calculation = Label(text="0")
value_before_calculation.grid(column=1, row=1)

#Button
button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

#Entry
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

window.mainloop()
