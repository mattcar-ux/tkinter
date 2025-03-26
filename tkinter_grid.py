import tkinter as tk

window = tk.Tk()

window.columnconfigure(1, weight=1, minsize=100)
window.rowconfigure(1, weight=1, minsize=100)

# per vedere il gestore di geometria - GRID

frame1_1 = tk.Frame(master=window, borderwidth=15, relief=tk.GROOVE)
frame1_1.grid(row=1, column=1)
label1_1 = tk.Label(master=frame1_1, text="riga 1, colonna 1", font="Helvetica 15 italic")
label1_1.pack()

frame1_2 = tk.Frame(master=window, borderwidth=15, relief=tk.GROOVE)
frame1_2.grid(row=1, column=2)
label1_2 = tk.Label(master=frame1_2, text="riga 1, colonna 2", font="Helvetica 15 bold")
label1_2.pack()

frame2_1 = tk.Frame(master=window, borderwidth=15, relief=tk.GROOVE)
frame2_1.grid(row=2, column=1)
label2_1 = tk.Label(master=frame2_1, text="riga 1, colonna 3")
label2_1.pack()

pulsante_1 = tk.Button( # widget
                text="----BUTTON----",
                font=("Courier", 20),
                background="black", # anche bg
                foreground="white", # anche fg
                width=20, # caratteri di larghezza
                height=3, # righe di altezza
                master=frame1_1 
                )

pulsante_1.pack()

pulsante_2 = tk.Button( # widget
                text="----PULSANTE----",
                font=("Courier", 20),
                background="black", # anche bg
                foreground="white", # anche fg
                width=20, # caratteri di larghezza
                height=3, # righe di altezza
                master=frame1_2,
                relief=tk.RAISED,
                borderwidth=10
                )

pulsante_2.pack()

window.mainloop()