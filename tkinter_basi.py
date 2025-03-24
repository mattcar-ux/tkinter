import tkinter as tk
# import tkinter.ttk as 

window = tk.Tk()
window.title("TITOLO")

border_effects = {
                "flat":tk.FLAT,
                "sunken":tk.SUNKEN,
                "raised":tk.RAISED,
                "groove":tk.GROOVE,
                "ridge":tk.RIDGE
                }

frame_a = tk.Frame(relief=tk.FLAT, borderwidth=5)
frame_b = tk.Frame(relief=tk.RIDGE, borderwidth=5)
frame_a.pack(side=tk.LEFT)
frame_b.pack(side=tk.LEFT)

saluto_1 = tk.Label( # widget
                text="***Ciao a tutti***",
                font=("Courier", 20),
                background="black", # anche bg
                foreground="white", # anche fg
                master=frame_a # raggruppa widget dentro un frame
                # width=20, # caratteri di larghezza
                # height=3 # righe di altezza
                )

saluto_2 = tk.Label( # widget
                text="***Arrivederci***",
                font=("Courier", 20),
                background="black", # anche bg
                foreground="white", # anche fg
                master=frame_b
                # width=20, # caratteri di larghezza
                # height=3 # righe di altezza
                )

entry_1 = tk.Entry( # entry widget, riga sext = tk.Text()ingola per prendere input da utente
                    fg="yellow",
                    bg="blue",
                    width=50,
                    master=frame_a
                    )

pulsante_1 = tk.Button( # widget
                text="----BUTTON----",
                font=("Courier", 20),
                background="black", # anche bg
                foreground="white", # anche fg
                width=20, # caratteri di larghezza
                height=3, # righe di altezza
                master=frame_a 
                )

pulsante_2 = tk.Button( # widget
                text="----PULSANTE----",
                font=("Courier", 20),
                background="black", # anche bg
                foreground="white", # anche fg
                width=20, # caratteri di larghezza
                height=3, # righe di altezza
                master=frame_b,
                relief=tk.RAISED,
                borderwidth=10
                ) 

saluto_1.pack() # metto il saluto nella finestra
saluto_2.pack()
entry_1.pack() # metto nella finestra la riga di input
pulsante_1.pack(side=tk.LEFT) # metto il pulsante nella finestra, a sinistra
pulsante_2.pack(side=tk.LEFT)


window.mainloop() # esegue event loop, resta aperto finché non faccio qualcosa: aspetta input

