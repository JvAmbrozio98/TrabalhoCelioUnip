import tkinter as tk 
import subprocess
import os 
from Exercicio05 import Exercicio05Main


window = tk.Tk()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_height = 600
window_width = 900
x = (screen_width - window_width ) // 2
y = (screen_height - window_height ) // 2
window.geometry(f"{window_width}x{window_height}+{x}+{y}")
buttons = []


for i in range(1,7):
    button =tk.Button(window, text=f"Button {i}",command=Exercicio05Main)
    buttons.append(button)

for i, button in enumerate(buttons):

    button.place(relx=0.5, rely=(0.225 + 0.1 * i), anchor='center')
window.mainloop()