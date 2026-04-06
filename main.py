'''
Name -> "PinSight"
Description -> A tool for visualizing and analyzing bowling data
Start Date -> April 6th 2026 (4/6/2026)
Developer -> Chris Herriman Jr
'''

###############
### IMPORTS ###
###############
import sqlite3 as sqlite
import tkinter as tk
import pandas as pd
import matplotlib.pyplot as mp




####################
### Screen Setup ###
####################
screen = tk.Tk()
screen.geometry("1200x700")
screen.resizable(False, False)
screen.title("PinSight")   
background_color = "#e1e1e1"
screen.configure(bg=background_color)
text_font = ("Arial", 12)




def add_data():
    bowler_name_label = tk.Label(screen, text=("Bowler Name"), font=text_font, fg="#000000", bg=background_color)
    bowler_name_label.place(x=100, y=100)

add_data()

screen.mainloop()
