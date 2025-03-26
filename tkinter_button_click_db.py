import tkinter as tk
from delete_database import delete_DATABASE
from database_population import creare_DATABASE

window = tk.Tk()

window.columnconfigure(1, weight=2, minsize=100)
window.rowconfigure(1, weight=2, minsize=100)
window.columnconfigure(2, weight=1, minsize=100)
window.rowconfigure(2, weight=1, minsize=100)

def button_click_1_creare_DB():
    nome_database = entry_1_DB_nome.get()
    creare_DATABASE(nome_database)
    entry_1_DB_nome.delete(0, tk.END)
    lbl_db_creato["text"] = "DATABASE CREATO!"

def button_click_2_cancellare_DB():
    delete_DATABASE()

frame1_1 = tk.Frame(master=window, borderwidth=15, relief=tk.GROOVE)
frame1_1.grid(row=1, column=1)
label1_1 = tk.Label(master=frame1_1, text="CREA", font="Courier 15 bold")
label1_1.pack()

button_1 = tk.Button( # widget
                text="CREA DB",
                font=("Courier 25 bold"),
                background="black", # anche bg
                foreground="#53a8bd", # anche fg
                width=10, # caratteri di larghezza
                height=3, # righe di altezza
                master=frame1_1,
                relief=tk.RAISED,
                borderwidth=5,
                command=button_click_1_creare_DB
                )
button_1.pack()

entry_1_DB_nome = tk.Entry(
                            fg="white",
                            bg="black",
                            font="Courier 25 bold",
                            width=50,
                            master=frame1_1
                            )

lbl_db_creato = tk.Label(
                        text="",
                        fg="green",
                        font="Courier 25 bold",
                        master=frame1_1
                        )
entry_1_DB_nome.pack()
lbl_db_creato.pack()

frame1_2 = tk.Frame(master=window, borderwidth=15, relief=tk.GROOVE)
frame1_2.grid(row=1, column=2)
label1_2 = tk.Label(master=frame1_2, text="ELIMINA", font="Courier 15 bold")
label1_2.pack()

button_2 = tk.Button( # widget
                text="ELIMINA DB",
                font=("Courier 10 bold"),
                background="black", # anche bg
                foreground="#53a8bd", # anche fg
                width=10, # caratteri di larghezza
                height=3, # righe di altezza
                master=frame1_2,
                relief=tk.RAISED,
                borderwidth=5,
                command=button_click_2_cancellare_DB
                )
button_2.pack()

window.mainloop()