from tkinter import *
from datetime import date
from tkinter import  filedialog
from tkinter import messagebox
from PIL import Image,ImageTk
import os
import openpyxl,xlrd

from openpyxl import Workbook
import pathlib


def gerarArquivos():
    file = pathlib.Path('InformacoesEstudantes.xlsx')
    if file.exists():
        pass
    else:
        file = Workbook ()
        sheet = file.active
        sheet['A1'] = 'RA'
        sheet['B1'] = 'Nome'
        sheet['C1'] = 'CPF'
        sheet['D1'] = 'Curso'
        sheet["E1"] = 'Disciplina Ativa '
        file.save('InformacoesEstudantes.xlsx')








