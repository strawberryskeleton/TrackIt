import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, date, timedata

#color scheme
mainbg= '' #main bg color 
cardbg= '#FFFFFF' #color for the card (white)

mainaccent= #the main accent color ()
secaccent= #secondary accent color ()

maintext= #main text color for the headings, etc. ()
mutedtext= #for text not in use, or secondary texts ()

errorcolor= #to highlight errors (red)
successcolor= #to show success messages (green)

neutralbtn= #color for any neutral btns like calculate btn?... 
btn1color= #will add as per no of buttons, similar scheme for main and accent colors

bordercolor=

#creating main window
win=tk.Tk()
win.title('Deadline Calculator')
win.minsize(width=600, height=600)
win.configure(bg=mainbg) 