import tkinter as tk 
 
from Exercicio01 import imprimirNumerosAnterioresPosteriores
from Exercicio02 import maiorNumeroDecimal
from Exercicio03 import menorNumeroDecimal
from Exercicio04 import diasVividos
from Exercicio05 import Exercicio05Main
from Exercicio06 import vendas

window = tk.Tk()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_height = 400
window_width = 600
x = (screen_width - window_width ) // 2
y = (screen_height - window_height ) // 2
#window.geometry(f"{window_width}x{window_height}+{x}+{y}")
buttons = []
functionList = [imprimirNumerosAnterioresPosteriores,maiorNumeroDecimal,menorNumeroDecimal,diasVividos,Exercicio05Main,vendas]




for i in range(0,6):
    button =tk.Button(window, text=f"Exercicio  {i + 1}",command=functionList[i])
    buttons.append(button)

for i, button in enumerate(buttons):

    button.place(relx=0.5, rely=(0.225 + 0.1 * i), anchor='center')
window.mainloop()