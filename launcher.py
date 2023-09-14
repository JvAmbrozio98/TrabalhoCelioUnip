import tkinter as tk 
from PIL import Image, ImageTk
from Exercicio01 import imprimirNumerosAnterioresPosteriores
from Exercicio02 import maiorNumeroDecimal
from Exercicio03 import menorNumeroDecimal
from Exercicio04 import diasVividos
from Exercicio05 import Exercicio05Main
from Exercicio06 import vendas
from playsound import playsound

window = tk.Tk()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_height = 400
window_width = 600

img = ImageTk.PhotoImage(Image.open("celeio.jpg"))
panel = tk.Label(window, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")

img2 = ImageTk.PhotoImage(Image.open("baixados.png"))
panel2 = tk.Label(panel, image = img2)
panel2.pack(side="left")


buttons = []
functionList = [imprimirNumerosAnterioresPosteriores,maiorNumeroDecimal,menorNumeroDecimal,diasVividos,Exercicio05Main,vendas]

for i in range(0,6):
    button =tk.Button(window, text=f"Exercicio  {i + 1}",command=functionList[i],background="skyblue3")
    buttons.append(button)

for i, button in enumerate(buttons):
    button.place(relx=0.5, rely=(0.225 + 0.1 * i), anchor='center')


window.mainloop()