import tkinter as tk

window = tk.Tk()

frame1 = tk.Frame(master=window, width=100, height=100, bg="red")
frame1.pack(fill=tk.X) #riempie tutta la finestra con l'oggetto, quindi ignora width

frame2 = tk.Frame(master=window, width=50, height=50, bg="yellow")
frame2.pack(side=tk.RIGHT, fill=tk.Y)

frame3 = tk.Frame(master=window, width=25, height=25, bg="blue")
frame3.pack(fill=tk.BOTH, expand=True)

window.mainloop()