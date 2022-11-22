from tkinter import *
import tkinter.messagebox
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
from calendario import *
from usuario import *
from conexao import *


global titulo, data, horario
titulo = []
data = []
horario = []


def Criar_Evento():
    screen_criar = Tk()
    screen_criar.title('AGENDAMENTO')
    screen_criar.configure(bg = '#0B2161')
    screen_criar.geometry('700x500+500+500')
    
    tela_criar_evento = PhotoImage(file = 'images/tela_criar_evento.png')
    label_criar_evento = Label(image = tela_criar_evento)
    label_criar_evento.pack(side = RIGHT)
    entry_titulo = Entry(screen_criar, justify = CENTER)
    entry_titulo.place(x = 130, y = 220)    
    entry_data = Entry(screen_criar, justify = CENTER)
    entry_data.place(x = 130, y = 280) 
    entry_horario = Entry(screen_criar, justify = CENTER)
    entry_horario.place(x = 130, y = 350) 
    
    def bt_click_criar():
        novoTitulo = entry_titulo.get()
        novaData = entry_data.get()
        novoHorario = entry_horario.get()
        titulo.append(novoTitulo)
        data.append(novaData)
        horario.append(novoHorario)
        conexao = iniciar_conexao()      
        inserir = "INSERT INTO usuarios(nome, email, senha) VALUES ('" + (novoTitulo) + "', '" + (novaData) + "', '" + (novoHorario)+ "')"
        inserir_evento(conexao, inserir)
        destruir()

    def destruir():
        screen_criar.destroy()
        Menu()
      
    def bt_click_voltar():
        screen_criar.destroy()
        Menu()

    if entry_titulo.get() == '' or entry_data.get() == '' or entry_horario.get() == '':
       tkinter.messagebox.showinfo(title = 'Atenção!', message = 'Preencha todos os campos!') 

    bt_criar = Button(screen_criar, text = 'CRIAR', bg = '#85AEF2', font = ('Arial', 10, 'bold'), command = bt_click_criar)
    bt_criar.place(x = 130, y = 390)
    bt_voltar = Button(screen_criar, text = 'VOLTAR', bg = '#85AEF2', font = ('Arial', 10, 'bold'), command = bt_click_voltar)
    bt_voltar.place(x = 220, y = 390)
    
    screen_criar.mainloop()
  

def Acessar_Evento():
    print('a')



def Encerrar():
    exit()
  