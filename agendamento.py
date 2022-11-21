from tkinter import *
import tkinter.messagebox
import sqlite3
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
from calendario import *
from usuario import *


global titulo, data, horario
titulo = []
data = []
horario = []


def Criar_Evento():
    screen_criar = Tk()
    screen_criar.title('AGENDAMENTO')
    screen_criar.configure(bg = '#0B2161')
    screen_criar.geometry('700x500+500+500')
     
    window_criar = Label(screen_criar, text = 'Criar Evento', bg = '#85AEF2', fg = '#0B0B3B', font = ('Times New Roman', 20, 'bold'))
    window_criar.pack(ipadx = 30, ipady = 30, padx = 1, pady = 1, side = 'top', fill = X, expand = False)
    
    label_titulo = Label(screen_criar, text = 'Título', bg = '#0B2161', fg = 'white', font = ('Times New Roman', 12))
    label_titulo.place(x = 100, y = 135)
    label_data = Label(screen_criar, text = 'Data', bg = '#0B2161', fg = 'white', font = ('Times New Roman', 12))
    label_data.place(x = 100, y = 195)  
    label_horario = Label(screen_criar, text = 'Horário', bg = '#0B2161', fg = 'white', font = ('Times New Roman', 12))
    label_horario.place(x = 100, y = 255)

    entry_titulo = Entry(screen_criar, justify = CENTER)
    entry_titulo.place(x = 105, y = 160)    
    entry_data = Entry(screen_criar, justify = CENTER)
    entry_data.place(x = 105, y = 220) 
    entry_horario = Entry(screen_criar, justify = CENTER)
    entry_horario.place(x = 105, y = 280) 

    novoTitulo = entry_titulo.get()
    novaData = entry_data.get()
    novoHorario = entry_horario.get()
    titulo.append(novoTitulo)
    data.append(novaData)
    horario.append(novoHorario)
  
    def bt_click_criar():
      screen_criar.destroy()
      Menu()

    #if entry_titulo.get() == '' or entry_data.get() == '' or entry_horario.get() == '':
    #   tkinter.messagebox.showinfo(title = 'Atenção!', message = 'Preencha todos os campos!')

    #else:
    #    Banco()
    #    cursor.execute('INSERT INTO `usuario` (titulo, data, horario) VALUES(?, ?, ?)', str(entry_titulo.get()), float(entry_data.get()), float(entry_horario.get())
    #    conexao.commit()
    #    cursor.close()
    #    conexao.close()
    #    tkinter.messagebox.showinfo(title = 'Sucesso!', message = 'Evento criado!')       

    bt_criar = Button(screen_criar, text = 'CRIAR', bg = '#85AEF2', fg = 'black', font = ('Arial', 10, 'bold'), command = bt_click_criar)
    bt_criar.place(x = 105, y = 330)
  
    screen_criar.mainloop()
  

def Acessar_Evento():
    print('a')



def Encerrar():
    exit()
  