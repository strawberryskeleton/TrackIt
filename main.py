import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, date, timedelta

# root = tk.Tk()
# root.title("My App")

# color scheme
"""
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
"""
mainbg = "#EAEAF6"  # main bg color
cardbg = "#FFFFFF"  # color for the card (white)

mainaccent = "#233D78"  # the main accent color ()
secaccent = "4CFEF5"  # secondary accent color ()

maintext = "#214174"  # main text color for the headings, etc. ()
mutedtext = "#6B7280"  # for text not in use, or secondary texts ()

errorcolor = "#DC2626"  # to highlight errors (red)
successcolor = "#2CA25F"  #''to show success messages (green)

neutralbtn = "#7D8CC3"  # color for any neutral btns like calculate btn?...
btn1color = "#EA4F93"  # will add as per no of buttons, similar scheme for main and accent colors
btn2color = "#14A9BF"
btn3color = "#F5BF17"

bordercolor = "#999999"

wfont = ("Segoe UI", 10)  # font for normal writing
hfont = ("Segoe UI", 22, "bold")  # font for heading
bfont = ("Segoe UI", 11, "bold")  # font for buttons


# creating main window
win = tk.Tk()
win.title("Deadline Calculator")
win.minsize(width=600, height=600)
win.configure(bg=mainbg)

# title frame
tframe = tk.Frame(win, bg=mainbg)
tframe.pack(padx=5, pady=15)
tlabel = tk.Label(tframe, text="Deadline Tracker", font=hfont, fg=mainaccent, bg=mainbg)
tlabel.pack()

# card frame
cframe = tk.Frame(win, bg=cardbg, padx=25, pady=25)
cframe.pack(padx=20, pady=10)

# event name field
lb1 = tk.Label(cframe, text="Event Name: ", bg=cardbg, fg=maintext, font=wfont)
lb1.grid(row=0, column=0, sticky="w", pady=5)
eventname = tk.Entry(
    cframe,
    font=wfont,
    relief="flat",
    highlightthickness=1,
    highlightbackground=bordercolor,
)
eventname.grid(row=0, column=1, pady=5)

# event date field
lb2 = tk.Label(
    cframe, text="Event Date(DD/MM/YYYY): ", bg=cardbg, fg=maintext, font=wfont
)
lb2.grid(row=1, column=0, sticky="w", pady=5)
eventdate = tk.Entry(
    cframe,
    font=wfont,
    relief="flat",
    highlightthickness=1,
    highlightbackground=bordercolor,
)
eventdate.grid(row=1, column=1, pady=5)

# deadline type field
lb3 = tk.Label(cframe, text="Deadline Type:", font=wfont, bg=cardbg, fg=maintext)
lb3.grid(row=2, column=0, sticky="w", pady=5)

d_type = {
    "Complaint filing": 30,
    "Response filing": 30,
    "Notice issuing": 7,
}  # dict using type:no od days required
dtypeSelect = tk.StringVar()
dropdown = ttk.Combobox(
    cframe, textvariable=dtypeSelect, values=list(d_type.keys()) + ["Other"]
)
dropdown.grid(row=2, column=1, pady=5)

# others option in deadline type field
otherdl = tk.Label(
    cframe, text="Specify type:", font=wfont, bg=cardbg, fg=maintext
)  # otherdeadlinelabel
cd_type = tk.StringVar()
otherde = tk.Entry(
    cframe,
    font=wfont,
    textvariable=cd_type,
    relief="flat",
    highlightthickness=1,
    highlightbackground=bordercolor,
)  # other deadline entry


# function to show or remove the 'other' field: only shown if chosen in the dropdown menu
def ddtypechange(event=None):
    if dtypeSelect.get() == "Other":
        otherdl.grid(row=3, column=0, sticky="w", padx=20, pady=5)
        otherde.grid(row=3, column=1, pady=5)
    else:
        otherdl.grid_remove()
        otherde.grid_remove()


dropdown.bind("<<ComboboxSelected>>", ddtypechange)

# custom deadline date field
lb4 = tk.Label(
    cframe, text="Deadline date (DD/MM/YYYY): ", font=wfont, bg=cardbg, fg=maintext
)
lb4.grid(row=4, column=0, sticky="w", pady=5)
# deadlinedate_type = tk.StringVar()
deadlinedate = tk.Entry(
    cframe,
    font=wfont,
    # textvariable=deadlinedate_type,
    relief="flat",
    highlightthickness=1,
    highlightbackground=bordercolor,
)
deadlinedate.grid(row=4, column=1, pady=5)

# btn frame
btnframe = tk.Frame(win, bg=mainbg)
btnframe.pack(pady=10)

status = tk.StringVar()

# first btn: calc deadline
dateofdeadline = tk.StringVar()


def cal_deadline():
    try:
        ed = datetime.strptime(eventdate.get(), "%d/%m/%Y").date()
        # case 1: user manually entered the deadline
        if dtypeSelect.get() == "":  # others option not selected
            final_date = datetime.strptime(deadlinedate.get(), "%d/%m/%Y").date()
            if final_date < ed:
                status.set("Error: Deadline is before event date")
                statusl.configure(fg=errorcolor)
                return
            else:
                days_left = (final_date - ed).days
                status.set(f"Number of day(s) left = {days_left}")
                statusl.configure(fg=successcolor)
                dateofdeadline.set(final_date.strftime("%d/%m/%Y"))
        # case 2:
        else:
            if dtypeSelect.get() in d_type:
                n_days = d_type.get(dtypeSelect.get(), 0)
                final_date = ed + timedelta(days=n_days)
                formatted = final_date.strftime("%d/%m/%Y")
                status.set(f"Date of Deadline is: {formatted}")
                statusl.configure(fg=successcolor)
                dateofdeadline.set(final_date.strftime("%d/%m/%Y"))
            elif dtypeSelect.get() == "Other":
                if not otherde or not cd_type.get().strip():
                    status.set("Enter custom type and date")
                    statusl.configure(fg=errorcolor)
                    return
                final_date = datetime.strptime(deadlinedate.get(), "%d/%m/%Y").date()
                if final_date < ed:
                    status.set("Error: Deadline is before the event date.")
                    statusl.configure(fg=errorcolor)
                    return
                else:
                    days_left = (final_date - ed).days
                    status.set(f"Number of day(s) = {days_left}")
                    statusl.configure(fg=successcolor)
                    dateofdeadline.set(final_date.strftime("%d/%m/%Y"))
            else:
                status.set("Select a deadline type or enter a date")
                statusl.configure(fg=errorcolor)

    except ValueError:
        status.set("Invalid date input!")
        statusl.configure(fg=errorcolor)


calbtn = tk.Button(
    btnframe,
    text="Calculate",
    command=cal_deadline,
    font=bfont,
    bg=mainaccent,
    fg="white",
    relief="flat",
)
calbtn.pack(pady=5)


# btn 2: clear
def clear_func():
    eventname.delete(0, tk.END)
    eventdate.delete(0, tk.END)
    dtypeSelect.set("")
    cd_type.set("")
    deadlinedate.delete(0, tk.END)
    dropdown.configure(state="readonly")
    otherde.grid_remove()
    otherdl.grid_remove()
    status.set("")


clearbtn = tk.Button(
    btnframe,
    text="Clear",
    command=clear_func,
    font=bfont,
    relief="flat",
    bg=btn1color,
    fg="white",
)
clearbtn.pack(pady=15)

# new btn frame for grid option for secondary buttons
btnframe2 = tk.Frame(win, bg=mainbg)
btnframe2.pack(pady=5)

# save btn
saved_events = []


def save_event():
    if eventdate.get() == "":
        status.set("Please calculate before saving!")
        statusl.configure(fg=errorcolor)
    else:
        actual_deadline_type = dtypeSelect.get()
        if actual_deadline_type == "Other":
            actual_deadline_type = cd_type.get().strip() or "Other"

        d_remain = (
            datetime.strptime(dateofdeadline.get(), "%d/%m/%Y").date() - date.today()
        ).days
        event_data = {
            "event_name": eventname.get(),
            "event_date": eventdate.get(),
            "deadline_type": actual_deadline_type,
            "final_deadline": dateofdeadline.get(),
            "days_till": d_remain,
            "notes": "",
            "done": False,
        }
        saved_events.append(event_data)
        clear_func()
        status.set("Event saved successfully")
        statusl.configure(fg=successcolor)


savebtn = tk.Button(
    btnframe2,
    text="Save Event",
    command=save_event,
    font=bfont,
    bg=btn2color,
    fg="white",
    relief="flat",
)
savebtn.grid(row=0, column=0, padx=10)


# table view
# checkbox function
def toggle_checkbox(event, tree):
    row_id = tree.identify_row(event.y)
    col = tree.identify_column(event.x)

    if not row_id or col != "#1":
        return

    values = list(tree.item(row_id, "values"))
    current = values[0]

    new_state = "☑" if current == "☐" else "☐"
    values[0] = new_state

    tree.item(row_id, values=values)

    event_name = values[1]
    for ev in saved_events:
        if ev["event_name"] == event_name:
            ev["done"] = new_state == "☑"

            if ev["done"]:
                tree.item(row_id, tags="completed")
            else:
                days_remaining = ev.get("days_till", 0)
                if days_remaining < 0:
                    tag = "overdue"
                elif days_remaining <= 7:
                    tag = "urgent"
                elif days_remaining <= 14:
                    tag = "warning"
                elif days_remaining <= 21:
                    tag = "safe"
                else:
                    tag = ""
                tree.item(row_id, tags=(tag,))
                break
    tree.selection_remove(tree.selection())


# notes func
def open_notes(event_data):
    detail_win = tk.Toplevel()
    detail_win.title("Event Notes")
    detail_win.geometry("450x450")

    cdframe = tk.Frame(detail_win, bg=cardbg, padx=20, pady=20)
    cdframe.pack(fill="both", expand=True, padx=20, pady=20)
    titlel = tk.Label(
        cdframe,
        text="Event Notes",
        font=("Segoe UI", 16, "bold"),
        fg=mainaccent,
        bg=cardbg,
    )
    titlel.pack(anchor="w", pady=10)
    evlabel = tk.Label(
        cdframe,
        text=f"Event: {event_data['event_name']}",
        font=("Segoe UI", 11),
        fg=maintext,
        bg=cardbg,
    )
    evlabel.pack(anchor="w", pady=15)
    notesl = tk.Label(cdframe, text="Notes: ", font=bfont, fg=maintext, bg=cardbg)
    notesl.pack(anchor="w")

    # textbox for the notes
    nbox = tk.Text(
        cdframe, height=10, width=40, font=("Segoe UI", 10), wrap="word", borderwidth=2
    )
    nbox.pack(fill="both", expand=True, padx=10, pady=5)

    nbox.insert("1.0", event_data["notes"])  # loading existing data if any

    # saving the notes data
    def save_notes():
        event_data["notes"] = nbox.get("1.0", tk.END).strip()
        detail_win.destroy()  # close win after saving

    savenotesbtn = tk.Button(
        cdframe,
        text="Save Notes",
        command=save_notes,
        font=bfont,
        fg="white",
        bg=mainaccent,
        relief="flat",
    )
    savenotesbtn.pack(anchor="e", padx=10, pady=5)


# delete func
def delete_event(event_name, tree, row_id):
    global saved_events
    saved_events = [ev for ev in saved_events if ev["event_name"] != event_name]
    tree.delete(row_id)


# tree click handler function
def tree_click_handler(event, tree):
    row_id = tree.identify_row(event.y)
    col = tree.identify_column(event.x)

    if not row_id:  # ie clicking outside the rows, then no action
        return
    if col == "#1":  # checkbox
        toggle_checkbox(event, tree)
    if col == "#7":  # notes
        values = tree.item(row_id, "values")
        event_name = values[1]
        for ev in saved_events:
            if ev["event_name"] == event_name:
                open_notes(ev)
                break
        return
    if col == "#8":  # delete
        values = tree.item(row_id, "values")
        event_name = values[1]

        confirm = messagebox.askyesno("Delete Event", f"Delete Event '{event_name}'?")

        if confirm:
            delete_event(event_name, tree, row_id)
        return


# timeline view
def urgency_color(days_left):
    if days_left >= 14:
        return "#2CA25F"
    elif 7 <= days_left < 14:
        return "#F1B82D"
    elif 0 < days_left < 7:
        return "#DC2626"
    else:
        return "#E0E0E0"


def open_timeline():
    if not saved_events:
        messagebox.showinfo("Timeline", "No events to show on timeline.")
        return

    timeline_win = tk.Toplevel(win)
    timeline_win.title("Events Timeline")
    timeline_win.geometry("1150x600")
    timeline_win.configure(bg=mainbg)

    header = tk.Frame(timeline_win, bg=cardbg, padx=20, pady=15)
    header.pack(padx=20, pady=10, anchor="center")

    headl = tk.Label(
        header,
        text=f"Deadline Timeline ({len(saved_events)} events)",
        font=bfont,
        fg=mainaccent,
        bg=mainbg,
    )
    headl.pack(anchor="w")

    # prepare dates
    p_events = []

    for ev in saved_events:
        start = datetime.strptime(ev["event_date"], "%d/%m/%Y").date()
        end = datetime.strptime(ev["final_deadline"], "%d/%m/%Y").date()
        p_events.append((ev, start, end))

    start_date = min(e[1] for e in p_events)  # earliest date
    end_date = max(e[2] for e in p_events)  # latest date

    total_days = (end_date - start_date).days + 1
    px_per_day = 18
    left_margin = 220

    # creating canvas
    canvas = tk.Canvas(
        timeline_win, bg="white", height=450, width=1100, highlightthickness=0
    )
    canvas.pack(fill="both", expand=True, padx=20, pady=10)

    def x_from_date(d):
        return (d - start_date).days * px_per_day + left_margin

    y_scale = 50
    for i in range(0, total_days, 5):  # step 5 for every 5 days display
        d = start_date + timedelta(days=i)
        x = x_from_date(d)
        canvas.create_text(
            x, y_scale, text=d.strftime("%b %d"), fill=mutedtext, font=wfont
        )

    # creating Today line
    today = date.today()
    if start_date <= today <= end_date:
        x_today = x_from_date(today)
        canvas.create_line(x_today, y_scale + 10, x_today, 440, fill="red", dash=(4, 2))
        canvas.create_text(x_today, y_scale - 8, text="Today", fill="red", font=wfont)

    # adding each event
    row_h = 55
    bar_h = 22
    start_y = 90

    for i, (ev, s, e) in enumerate(p_events):
        y = start_y + i * row_h
        days_left = (e - today).days
        canvas.create_text(20, y, text=ev["event_name"], anchor="w", font=bfont)
        canvas.create_text(
            20,
            y + 16,
            text=f"{s:%d %b} → {e: %d %b}",
            anchor="w",
            fill=mutedtext,
            font=("Segoe UI", 9),
        )

        x1 = x_from_date(s)
        x2 = x_from_date(e)

        canvas.create_rectangle(
            x1,
            y - bar_h // 2,
            x2,
            y + bar_h // 2,
            fill=urgency_color(days_left),
            outline="",
        )
        canvas.create_text(
            x1 + 6,
            y,
            text=f"{days_left}d",
            anchor="w",
            fill="white",
            font=("Segoe UI", 9, "bold"),
        )


# funtion to show all events: table view
def show_events():
    if not saved_events:  # nothing is saved
        status.set("No events saved yet!")
        statusl.config(fg=errorcolor)
        return

    table_win = tk.Toplevel(win)  # independent window
    table_win.title("All Saved Events")
    table_win.geometry("800x450")

    columns = (
        "done",
        "event_name",
        "deadline_type",
        "event_date",
        "final_deadline",
        "days_till",
        "notes",
        "delete",
    )

    tree = ttk.Treeview(table_win, columns=columns, show="headings")
    tree.pack(fill="both", expand=True)

    tree.heading("done", text="✔")  # header row
    tree.column("done", width=40, anchor="center")  # column
    tree.heading("event_name", text="Event")
    tree.column("event_name", width=100, anchor="w")
    tree.heading("deadline_type", text="Type")
    tree.column("deadline_type", width=100, anchor="w")
    tree.heading("event_date", text="Event Date")
    tree.column("event_date", width=100, anchor="center")
    tree.heading("final_deadline", text="Deadline Date")
    tree.column("final_deadline", width=100, anchor="center")
    tree.heading("days_till", text="Day(s) till D-Day")
    tree.column("days_till", width=100, anchor="center")
    tree.heading("notes", text="Notes")
    tree.column("notes", width=100, anchor="center")
    tree.heading("delete", text="Delete")
    tree.column("delete", width=100, anchor="center")

    # traffic light system: configured as tags
    tree.tag_configure("overdue", background="#F2F2F2", foreground="#000000")
    tree.tag_configure("urgent", background="#FFC7CE", foreground="#9C0006")
    tree.tag_configure("warning", background="#FFEB9C", foreground="#9C5700")
    tree.tag_configure("safe", background="#C6EFCE", foreground="#006100")
    tree.tag_configure("completed", background="#E0E0E0", foreground="#777777")

    # assign tags
    for ev in saved_events:
        days_remaining = ev.get("days_till", 0)

        if ev["done"]:
            tag = "completed"
        elif days_remaining < 0:
            tag = "overdue"
        elif days_remaining <= 7:
            tag = "urgent"
        elif days_remaining <= 14:
            tag = "warning"
        elif days_remaining <= 21:
            tag = "safe"
        else:
            tag = ""

        # checking val for each row now
        check_symbol = "☑" if ev["done"] else "☐"

        values = (
            check_symbol,
            ev["event_name"],
            ev["deadline_type"],
            ev["event_date"],
            ev["final_deadline"],
            ev["days_till"],
            "📝",
            "🗑️",
        )
        tree.insert("", tk.END, values=values, tags=(tag,))

    status.set("Events shown in new window")
    statusl.configure(fg=successcolor)

    tree.bind("<ButtonRelease-1>", lambda e: tree_click_handler(e, tree))

    # new frame for timeline view
    footer = tk.Frame(table_win, bg=mainbg, pady=10)
    footer.pack(fill="x")

    timelinebtn = tk.Button(
        footer,
        text="View Timeline",
        command=open_timeline,
        font=bfont,
        bg=mainaccent,
        fg="white",
        relief="flat",
    )
    timelinebtn.pack()


allsaved = tk.Button(
    btnframe2,
    text="Show all",
    command=show_events,
    font=bfont,
    relief="flat",
    bg=btn3color,
    fg="white",
)
allsaved.grid(row=0, column=1, padx=10)


# msg display
statusl = tk.Label(
    btnframe2, textvariable=status, font=wfont, bg=mainbg, wraplength=500
)
statusl.grid(row=1, column=0, columnspan=2, pady=15)


win.mainloop()
