from tkinter import *
import tkinter.messagebox
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
from usuario import *
from agendamento import *


def Menu():
  screen_menu = Tk()
  screen_menu.title('CALENDÁRIO')
  screen_menu.configure(bg = '#0B2161')
  screen_menu.geometry('700x500+500+500')
  
  tela_menu = PhotoImage(file = 'images/tela_menu.png')
  label_menu = Label(image = tela_menu)
  label_menu.pack(side = RIGHT)

  def bt_click1():
    screen_menu.destroy()
    Criar_Evento()

  bt_criar = Button(screen_menu, text = 'CRIAR', bg = '#C8E0EB', fg = '#020360', font = ('Arial', 20, 'bold'), command = bt_click1, borderwidth = 0)
  bt_criar.place(x = 210, y = 200)    
      
  def bt_click2():
    screen_menu.destroy()
    Acessar_Evento()

  bt_acessar = Button(screen_menu, text = 'ACESSAR', bg = '#C8E0EB', fg = '#020360', font = ('Arial', 20, 'bold'), command = bt_click2, borderwidth = 0)
  bt_acessar.place(x = 190, y = 285)

  def bt_click3():
    screen_menu.destroy()
    Encerrar()

  bt_encerrar = Button(screen_menu, text = 'SAIR', bg = '#85AEF2', fg = 'black', font = ('Arial', 17, 'bold'), command = bt_click3)
  bt_encerrar.place(x = 230, y = 360)
  
  screen_menu.mainloop()
  