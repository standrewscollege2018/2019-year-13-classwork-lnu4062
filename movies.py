""" This program shows how to populate a listbox with the names of objects. It also allows the user
to select multiple items, then when a button is clicked it displays the name of the selected item(s).
It also displays a total price by adding prices of all items selected. """

from tkinter import *
from tkinter import messagebox

class Movie():
    """ Objects in this class have two attributes, name and price. """
    
    def __init__(self, name, theatre, price):
        """ Set up the new object with a name and price. Also add the thetare to the movie list and tickets/seats total"""
        
        self._name = name
        self._price = price
        self._theatre = theatre
        if theatre == "Mann Theatre":
            self._tickets = 80
            mann_movies.append(self)
        elif theatre == "Academy":
            self._tickets = 120
            academy_movies.append(self)
        elif theatre == "Green Fern":
            self._tickets = 200
            green_movies.append(self)             
        

    def get_name(self):
        """ Returns the name of the movie. """
        
        return self._name
    
    def get_price(self):
        """ Returns the price of the price. """
        
        return self._price
    """ Returns name of tickets"""            
    def get_tickets(self):
        
        return self._tickets
    
    def sell_tickets(self):
        
        self._tickets -= quantity.get()
    
def update_order():
    """ This function gets the selected movies, retrieves their prices and adds them to the total cost and the quannitiy for mann theatre movies."""

    global selected_movie
    
    
    for i in mann_listbox.curselection():
        total_cost.set(mann_movies[i].get_price()*quantity.get())
        order.set(mann_movies[i].get_name() + "\n")
        selected_movie = mann_movies[i]

        """ This function gets the selected movies, retrieves their prices and adds them to the total cost and the quannitiy for academy movies."""
    
    for i in academy_listbox.curselection():
        total_cost.set(academy_movies[i].get_price()*quantity.get())
        order.set(academy_movies[i].get_name() + "\n") 
        selected_movie = academy_movies[i]
    
        """ This function gets the selected movies, retrieves their prices and adds them to the total cost and the quannitiy for green fern movies."""

    
    for i in green_listbox.curselection():
        total_cost.set(green_movies[i].get_price()*quantity.get())
        order.set(green_movies[i].get_name() + "\n")    
        selected_movie = green_movies[i]


def reset_order():
    """ This function is called by the reset_btn, and resets total_cost to zero, and clears the order label.
    It uses a Tkinter messagebox to check whether the user actually wants to do this. """
    
    if messagebox.askyesno("Warning!", "Are you sure you want to clear the order?"):
        total_cost.set(0)
        order.set(0)
        quantity.set(0)

def confirm_order():
    """ This function is called by the confrim_btn, and confrims total_cost to user input, and clears the order label.
    It uses a Tkinter messagebox to check whether the user actually wants to do this. """
    
    if messagebox.askyesno("Alert!", "Are you sure you want to confirm?"):
        total_cost.set("")
        selected_movie.sell_tickets()
        order.set(0)
        quantity.set(0)
        update_listbox()

def update_listbox():
    
    """ update tickets/seats for man theatre"""
    mann_listbox.delete(0, END)
    # loop through the list of movie objects and get each name, inserting into the listbox
    for m in mann_movies:
        detail = m.get_name() + " $" + str(m.get_price()) + "  Seats:" + str(m.get_tickets())
        mann_listbox.insert(END, detail)    
     
    # update order for academy      
    green_listbox.delete(0, END)
    # loop through the list of movie objects and get each name, inserting into the listbox
    for m in green_movies:
        detail = m.get_name() + " $" + str(m.get_price()) + "  Seats:" + str(m.get_tickets())
        green_listbox.insert(END, detail)
    
    # update order for academy  
    academy_listbox.delete(0, END)    
    # loop through the list of movie objects and get each name, inserting into the listbox
    for m in academy_movies:
        detail = m.get_name() + " $" + str(m.get_price()) + "  Seats:" + str(m.get_tickets())
        academy_listbox.insert(END, detail)
   
root = Tk()
root.geometry('500x300')
  
# list to store all pizza objects
mann_movies = []
academy_movies = []
green_movies = []

# Create the movies objects
Movie("Shrek", "Mann Theatre", 10)
Movie("Matrix", "Mann Theatre", 10)
Movie("Sherk 2", "Academy", 10)
Movie("Matrix", "Academy", 10)
Movie("Star Trek", "Mann Theatre", 10)
Movie("Star Trek", "Academy", 10)
Movie("Shrek", "Green Fern", 10)    
Movie("Matrix", "Green Fern", 10)
Movie("Star Trek", "Green Fern", 10)

############ Mann Theatre ###################
mann_lbl = Label(root, text="Mann Theatre").grid(row=0, column=0)
# Set up our listbox. Make sure you put the .grid() on a new line
mann_listbox = Listbox(root, selectmode=SINGLE)
mann_listbox.grid(column=0, row=1)

############ Academy ################
academy_lbl = Label(root, text="Academy").grid(row=0, column=1)
# Set up our listbox. Make sure you put the .grid() on a new line
academy_listbox = Listbox(root, selectmode=SINGLE)
academy_listbox.grid(column=1, row=1)
   
############ Green Fern  ################
green_lbl = Label(root, text="Green Fern").grid(row=0, column=2)
# Set up our listbox. Make sure you put the .grid() on a new line
green_listbox = Listbox(root, selectmode=SINGLE)
green_listbox.grid(column=2, row=1)
    
# button to update the order
select_btn = Button(root, text="Select", command=update_order).grid(row=3, column=4)

# Confirm to reset the order
confirm_btn = Button(root, text="Confirm order", command=confirm_order).grid(row=7, column=3)

# entry field
quantity = IntVar()
quantity_ordered = Entry(root, textvariable=quantity).grid()
# Label to display the total cost of the order
total_cost = IntVar()
total_cost.set(0)
cost_lbl = Label(root, textvariable=total_cost).grid(row=5)

# Label to display the summary of the order
order = StringVar()
order_lbl = Label(root, textvariable=order).grid(row=5, column=1, sticky=N)

# Button to reset the order
reset_btn = Button(root, text="Reset order", command=reset_order).grid(row=3, column=3)

update_listbox()

root.mainloop()
