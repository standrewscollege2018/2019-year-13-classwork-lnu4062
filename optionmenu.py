from tkinter import *




root = Tk()
root.geometry('300x200')

names = ["Angus", "Toby", "Liam", "Des"]

selected_name = StringVar()
selected_name.set(names[0])



name_menu = OptionMenu(root, selected_name, *names).grid()

root.mainloop()