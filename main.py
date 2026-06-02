import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, date, timedata

#color scheme
'''
yellow = #fce168
pink= #f29db4
light purple= #d9b3ff
pink barbie= #ff66b3
dark yellow = #ffd11a
lighter purple= #9999ff
dark purple (border or text)= #4d0099, #400080
cerulean = #1a8cff
sea green neon =#00e6e6
blue neonish = #0080ff
lightest purple accent = #e0ccff
'''
mainbg= '#c7a8f5' #main bg color 
cardbg= '#FFFFFF' #color for the card (white)

mainaccent= '#0d228c' #the main accent color ()
secaccent= '' #secondary accent color ()

maintext= '#000080'#main text color for the headings, etc. ()
mutedtext= '' #for text not in use, or secondary texts ()

errorcolor= '#ff1a1a' #to highlight errors (red)
successcolor= '#47d147'#''to show success messages (green)

neutralbtn= #color for any neutral btns like calculate btn?... 
btn1color= '#f54da6' #will add as per no of buttons, similar scheme for main and accent colors
btn2color= '##ffcb0f'
btn3color= '#f54da6'

bordercolor= '#4d0099'

#creating main window
win=tk.Tk()
win.title('Deadline Calculator')
win.minsize(width=600, height=600)
win.configure(bg=mainbg) 

