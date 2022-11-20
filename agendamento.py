from tkinter import *
import tkinter.messagebox
import sqlite3
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
from calendario import *
from usuario import *


def Criar_Evento():
    screen_criar = Tk()
    screen_criar.title('AGENDAMENTO')
    screen_criar.configure(bg = '#0B2161')
    screen_criar.geometry('700x500+500+500')
     
    window_criar = Label(screen_criar, text = 'Criar Evento', bg = '#85AEF2', fg = '#0B0B3B', font = ('Times New Roman', 20, 'bold'))
    window_criar.pack(ipadx = 30, ipady = 30, padx = 1, pady = 1, side = 'top', fill = X, expand = False)
    
    label_titulo = Label(screen_criar, text = 'Título', bg = '#0B2161', fg = 'white', font = ('Times New Roman', 12))
    label_titulo.place(x = 100, y = 140)
    label_data = Label(screen_criar, text = 'Data', bg = '#0B2161', fg = 'white', font = ('Times New Roman', 12))
    label_data.place(x = 100, y = 200)  
    label_horario = Label(screen_criar, text = 'Horário', bg = '#0B2161', fg = 'white', font = ('Times New Roman', 12))
    label_horario.place(x = 100, y = 260)


  
    screen_criar.mainloop()
  

def Acessar_Evento():
    print('a')



def Encerrar():
    exit()
  