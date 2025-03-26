import tkinter as tk

window = tk.Tk()

window.columnconfigure(1, weight=2, minsize=100)
window.rowconfigure(1, weight=2, minsize=100)
window.columnconfigure(2, weight=1, minsize=100)
window.rowconfigure(2, weight=1, minsize=100)

def button_click_1():
    if label1_1["text"] == "ORIGINALE":
        label1_1["text"] = "CAMBIATA"
    else:
        label1_1["text"] = "ORIGINALE"

def button_click_2():
    nuovo_testo = entry_1_2.get()
    label1_2["text"] = nuovo_testo
    entry_1_2.delete(0, tk.END)

frame1_1 = tk.Frame(master=window, borderwidth=15, relief=tk.GROOVE)
frame1_1.grid(row=1, column=1)
label1_1 = tk.Label(master=frame1_1, text="ORIGINALE", font="Courier 15 bold")
label1_1.pack()

button_1 = tk.Button( # widget
                text="----BUTTON----",
                font=("Courier 10 bold"),
                background="black", # anche bg
                foreground="#53a8bd", # anche fg
                width=10, # caratteri di larghezza
                height=3, # righe di altezza
                master=frame1_1,
                relief=tk.RAISED,
                borderwidth=5,
                command=button_click_1
                )
button_1.pack()

frame1_2 = tk.Frame(master=window, borderwidth=15, relief=tk.GROOVE)
frame1_2.grid(row=1, column=2)
label1_2 = tk.Label(master=frame1_2, text="INSERISCI QUALCOSA:", font="Courier 15 bold")
label1_2.pack()

entry_1_2 = tk.Entry( # entry widget, riga sext = tk.Text()ingola per prendere input da utente
                    fg="yellow",
                    bg="blue",
                    width=50,
                    master=frame1_2
                    )

entry_1_2.pack()

button_2 = tk.Button( # widget
                text="----BUTTON----",
                font=("Courier 10 bold"),
                background="black", # anche bg
                foreground="#53a8bd", # anche fg
                width=10, # caratteri di larghezza
                height=3, # righe di altezza
                master=frame1_2,
                relief=tk.RAISED,
                borderwidth=5,
                command=button_click_2
                )
button_2.pack()

label1_1["text"] = "CAMBIA"

window.mainloop()