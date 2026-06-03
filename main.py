import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, date, timedelta

# root = tk.Tk()
# root.title("My App")

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
mainbg= '#EAEAF6' #main bg color 
cardbg= '#FFFFFF' #color for the card (white)

mainaccent= '#233D78' #the main accent color ()
secaccent= '4CFEF5' #secondary accent color ()

maintext= '#214174'#main text color for the headings, etc. ()
mutedtext= '#6B7280' #for text not in use, or secondary texts ()

errorcolor= '#DC2626' #to highlight errors (red)
successcolor= '#2CA25F'#''to show success messages (green)

neutralbtn= '#7D8CC3'#color for any neutral btns like calculate btn?... 
btn1color= '#EA4F93' #will add as per no of buttons, similar scheme for main and accent colors
btn2color= '#14A9BF'
btn3color= '#F5BF17'

bordercolor= '#999999'

wfont= ('Segoe UI',10) #font for normal writing
hfont= ('Segoe UI',22,'bold') #font for heading
bfont= ('Segoe UI',11,'bold') #font for buttons

#creating main window
win=tk.Tk()
win.title('Deadline Calculator')
win.minsize(width=600, height=600)
win.configure(bg=mainbg) 

#title frame 
tframe=tk.Frame(win,bg=mainbg)
tframe.pack(padx=5,pady=15)
tlabel= tk.Label(tframe, text='Deadline Tracker', font=hfont,fg=mainaccent, bg=mainbg)
tlabel.pack()

#card frame
cframe=tk.Frame(win, bg=cardbg, padx=25,pady=25)
cframe.pack(padx=20, pady=10)

#event name field
lb1=tk.Label(cframe, text="Event Name: ", bg=cardbg, fg=maintext, font=wfont)
lb1.grid(row=0, column=0, sticky='w',pady=5)
eventname=tk.Entry(cframe,font=wfont,relief='flat',highlightthickness=1,highlightbackground=bordercolor)
eventname.grid(row=0,column=1,pady=5)

#event date field
lb2=tk.Label(cframe,text='Event Date(DD/MM/YYYY): ',bg=cardbg,fg=mainaccent,font=wfont)
lb2.grid(row=1,column=0,sticky='w',pady=5)
eventdate=tk.Entry(cframe,font=wfont,relief='flat',highlightthickness=1,highlightbackground=bordercolor)
eventdate.grid(row=1,column=1,pady=5)

#deadline type field
lb3=tk.Label(cframe,text='Deadline Type: ',font=wfont,bg=cardbg,fg=maintext)
lb3.grid(row=2,column=0,pady=5)

d_type={'Complaint filing': 30, 'Response filing': 30, 'Notice issuing':7} #dict using type:no od days required
dtypeSelect=tk.StringVar()
dropdown= ttk.Combobox(cframe,textvariable=dtypeSelect,values=list(d_type.keys())+['Other'],)
dropdown.grid(row=2,column=1,pady=5)

#others option in deadline type field
otherdl=tk.Label(cframe,text='Specify type: ',font=wfont,bg=cardbg,fg=maintext) #otherdeadlinelabel
cd_type=tk.StringVar()
otherde= tk.Entry(cframe,font=wfont,text=cd_type, relief='flat',highlightthickness=1, highlightbackground=bordercolor) #otherdeadlineentry

#function to show or remove the 'other' field: only shown if chosen in the dropdown menu
def ddtypechange(event=None):
    if dtypeSelect.get()=='Other':
        otherdl.grid(row=3,column=0,sticky='w',padx=20, pady=5)
        otherde.grid(row=3,column=1,pady=5)
    else:
        otherdl.grid_remove()
        otherde.grid_remove()

dropdown.bind("<<ComboboxSelected>>",ddtypechange)

#custom deadline date field
lb4=tk.Label(cframe,text='Deadline date (DD/MM/YYYY): ',font=wfont,bg=cardbg,fg=maintext)
lb4.grid(row=4,column=0,sticky='w',pady=5)
deadlinedate=tk.Entry(cframe,font=wfont,text=cd_type,relief='flat',highlightthickness=1,highlightbackground=bordercolor)
deadlinedate.grid(row=4,column=1,pady=5)

#btn frame
btnframe= tk.Frame(win,bg=mainbg)
btnframe.pack(pady=10)

status = tk.StringVar()

#first btn: calc deadline
dateofdeadline= tk.StringVar()

def cal_deadline():
    try:
        ed=datetime.strptime(eventdate.get(),"%d/%m/%Y").date()
        #case 1: user manually entered the deadline
        if dtypeSelect.get()=='': #others option not selected
            final_date= datetime.strptime(deadlinedate.get(),"%d/%m/%Y").date()
            if final_date<ed:
                status.set('Error: Deadline is before event date')
                statusl.configure(fg=errorcolor)
                return
            else:
                days_left= (final_date-ed).days
                status.set(f"Number of day(s) left = {days_left}")
                statusl.configure(fg=successcolor)
                dateofdeadline.set(final_date.strftime('%d/%m/%Y'))
        #case 2:
        else:
            if dtypeSelect.get() in d_type:
                n_days= d_type.get(dtypeSelect.get(),0)
                final_date= ed+ timedelta(days=n_days)
                formatted= final_date.strftime('%d/%m/%Y')
                status.set(f"Date of Deadline is: {formatted}")
                statusl.configure(fg=successcolor)
                dateofdeadline.set(formatted)
            elif dtypeSelect.get()=='Other':
                if not otherde or not cd_type.get().strip():
                    f_date.set('Enter custom type and date')
                    statusl.configure(fg=errorcolor)
                    return
                final_date=datetime.strptime(deadlinedate.get(),"%d/%m/%Y").date()
                if final_date<ed:
                    status.set("Error: Deadline is before the event date.")
                    statusl.configure(fg=errorcolor)
                else:
                    days_left= (final_date-ed).days
                    status.set(f"Number of day(s) = {days_left}")
                    statusl.configure(fg=successcolor)
                    dateofdeadline.set(final_date.strftime("%d/%m/%Y"))
            else:
                status.set('Select a deadline type or enter a date')
                statusl.configure(fg=errorcolor)
    except ValueError:
        status.set('Invalid date input!')
        statusl.configure(fg=errorcolor)

calbtn= tk.Button(btnframe,text='Calculate',command=cal_deadline,font=bfont, bg=neutralbtn,fg='white',relief='flat')
calbtn.pack(pady=5)

#btn 2: clear
def clear_func():
    eventname.delete(0,tk.END)
    eventdate.delete(0,tk.END)
    dtypeSelect.set('')
    deadlinedate.delete(0,tk.END)
    dropdown.configure(state='readonly')
    otherde.grid_remove()
    otherdl.grid_remove()
    status.set('')

clearbtn= tk.Button(btnframe,text='Clear', command=clear_func, font=bfont,relief='flat',bg=btn1color,fg='white')
clearbtn.pack(pady=15)

#new btn frame for grid option for secondary buttons
btnframe2= tk.Frame(win, bg=mainbg)
btnframe2.pack(pady=5)

#save btn
saved_events=[]
def save_event():
    if eventdate.get()=='':
        status.set("Please calculate before saving!")
        statusl.configure(fg=errorcolor)
    else:
        d_remain= (datetime.strptime(dateofdeadline.get(),"%d/%m/%Y").date() - date.today()).days
        event_data={'event_name':eventname.get(),'event_date':eventdate.get(),'deadline_type':dtypeSelect.get(),'final_deadline':dateofdeadline.get(),'days_till':d_remain,
        'notes':'','done':False}
        saved_events.append(event_data)
        clear_func()
        status.set('Event saved successfully')
        statusl.configure(fg=successcolor)

savebtn= tk.Button(btnframe2,text='Save Event', command=save_event,font=bfont,bg=btn2color,fg='white',relief='flat')
savebtn.grid(row=0,column=0,padx=10)

statusl= tk.Label(btnframe2,textvariable=status,font=wfont,bg=mainbg,wraplength=500)
statusl.grid(row=1,column=0,columnspan=2,pady=15)

win.mainloop()