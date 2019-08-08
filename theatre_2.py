""" This program shows how to populate a listbox with the names of objects. It also allows the user
to select multiple items, then when a button is clicked it displays the name of the selected item(s).
It also displays a total price by adding prices of all items selected. """

from tkinter import *
from tkinter import messagebox

class Movie():
    """ Objects in this class have two attributes, name and price. """
    
    def __init__(self, name, theatre, price):
        """ Set up the new object with a name and price. Also add the pizza to the movie list. """
        
        self._name = name
        self._price = price
        self._theatre = theatre
        if theatre == "Mann Theatre":
            self._tickets = 80
            mann_movies.append(self)
        elif theatre == "Academy":
            self._tickets = 120
            academy_movies.append(self)

    def get_name(self):
        """ Returns the name of the movie. """
        
        return self._name
    
    def get_price(self):
        """ Returns the price of the movie. """
        
        return self._price
    
    

def update_order():
    """ This function gets the selected pizzas, retrieves their prices and adds them to the total cost."""
    
    for i in listbox.curselection():
        total_cost.set(total_cost.get() + pizzas[i].get_price())
        order.set(order.get() + pizzas[i].get_name() + "\n")

def reset_order():
    """ This function is called by the reset_btn, and resets total_cost to zero, and clears the order label.
    It uses a Tkinter messagebox to check whether the user actually wants to do this. """
    
    if messagebox.askyesno("Warning!", "Are you sure you want to clear the order?"):
        total_cost.set(0)
        order.set("")

root = Tk()
root.geometry('300x300')

    
# list to store all pizza objects
mann_movies = []
academy_movies = []

# Create the pizza objects
Movie("Shrek", "Mann Theatre", 10)
Movie("Matrix", "Mann Theatre", 10)


############ Mann Theatre ###################
mann_lbl = Label(root, text="Mann Theatre").grid(row=0, column=0)
# Set up our listbox. Make sure you put the .grid() on a new line
mann_listbox = Listbox(root, selectmode=SINGLE)
mann_listbox.grid(column=0, row=1)

# loop through the list of movie objects and get each name, inserting into the listbox
for m in mann_movies:
    mann_listbox.insert(END, m.get_name())



############ Academy ################
acad_lbl = Label(root, text="Academy").grid(row=0, column=1)
# Set up our listbox. Make sure you put the .grid() on a new line
acadmey_listbox = Listbox(root, selectmode=SINGLE)
acadmey_listbox.grid(column=1, row=1)

# loop through the list of movie objects and get each name, inserting into the listbox
for m in academy_movies:
    academy_listbox.insert(END, m.get_name())



# button to update the order
select_btn = Button(root, text="Select", command=update_order).grid()

# Label to display the total cost of the order
total_cost = IntVar()
total_cost.set(0)
cost_lbl = Label(root, textvariable=total_cost).grid()

# Label to display the summary of the order
order = StringVar()
order_lbl = Label(root, textvariable=order).grid(row=0, column=1, sticky=N)

# Button to reset the order
reset_btn = Button(root, text="Reset order", command=reset_order).grid(row=3, column=0)

root.mainloop()