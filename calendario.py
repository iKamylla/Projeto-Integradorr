from tkinter import *
import tkinter.messagebox
import sqlite3
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
from usuario import *
from agendamento import *


def Menu():
    screen_menu = Tk()
    screen_menu.title('CALENDÁRIO')
    screen_menu.configure(bg = '#0B2161')
    screen_menu.geometry('700x500+500+500')
     
    window_menu = Label(screen_menu, text = 'Menu', bg = '#85AEF2', fg = '#0B0B3B', font = ('Times New Roman', 20, 'bold'))
    window_menu.pack(ipadx = 30, ipady = 30, padx = 1, pady = 1, side = 'top', fill = X, expand = False)
        
    label_criar = Label(screen_menu, text = '1 - Criar evento', bg = '#0B2161', fg = 'white', font = ('Times New Roman', 12))
    label_criar.place(x = 100, y = 150)
    label_acessar = Label(screen_menu, text = '2 - Acesssar evento', bg = '#0B2161', fg = 'white', font = ('Times New Roman', 12))
    label_acessar.place(x = 100, y = 210)
    label_encerrar = Label(screen_menu, text = '3 - Encerrar sessão', bg = '#0B2161', fg = 'white', font = ('Times New Roman', 12))
    label_encerrar.place(x = 100, y = 270)

    def bt_click1():
        screen_menu.destroy()
        Criar_Evento()

    bt_criar = Button(screen_menu, text = 'CRIAR', bg = '#85AEF2', fg = 'black', font = ('Arial', 10, 'bold'), command = bt_click1)
    bt_criar.place(x = 350, y = 150)    
      
    def bt_click2():
        screen_menu.destroy()
        Acessar_Evento()

    bt_acessar = Button(screen_menu, text = 'ACESSAR', bg = '#85AEF2', fg = 'black', font = ('Arial', 10, 'bold'), command = bt_click2)
    bt_acessar.place(x = 350, y = 210)

    def bt_click3():
        screen_menu.destroy()
        Encerrar()

    bt_encerrar = Button(screen_menu, text = 'SAIR', bg = '#85AEF2', fg = 'black', font = ('Arial', 10, 'bold'), command = bt_click3)
    bt_encerrar.place(x = 350, y = 270)
  
    screen_menu.mainloop()
  