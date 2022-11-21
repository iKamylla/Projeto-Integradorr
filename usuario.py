from tkinter import *
import tkinter.messagebox
import sqlite3
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
from calendario import *


global usuario, email, senha
usuario = []
email = []
senha = []


#def Banco():
#    global conexao, cursor
  
#    conexao = sqlite3.connect('banco.db')
#    cursor = conexao.cursor()
#    cursor.execute('CREATE TABLE IF NOT EXISTS `usuario` (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, usuario TEXT, email TEXT, senha TEXT)')

class Banco():
      global conexao, cursor
  
      def __init__(self):
          self.conexao = sqlite3.connect('banco.db')
          self.createTable()
      
      def createTable():
          c = self.conexao.cursor()
          c.execute('''create table if not exists usuarios (idusuario integer primary key autoincrement, usuario text, email text, senha text)''')
          self.conexao.commit()
          c.close()
          

def Login():
    screen_login = Tk()
    screen_login.title('ENTRANDO...')
    screen_login.configure(bg = '#0B2161')
    screen_login.geometry('700x500+500+500') 

    tela_login = PhotoImage(file = 'tela_login.png')
    label_login = Label(image = tela_login)
    label_login.pack(side = RIGHT)
  
    entry_email = Entry(screen_login, justify = CENTER)
    entry_email.place(x = 260, y = 210)
    entry_senha = Entry(screen_login, justify = CENTER)
    entry_senha.place(x = 260, y = 310)
    entry_senha['show'] = '*'

    novoEmail = entry_email.get()
    novaSenha = entry_senha.get()
    email.append(novoEmail)
    senha.append(novaSenha)  
  
    def bt_click_entrar():
        screen_login.destroy()
        Menu()

    def bt_click_voltar():
        screen_login.destroy()
        Iniciar()

    if entry_email.get() == '' or entry_senha.get() == '':
       tkinter.messagebox.showinfo(title = 'Atenção!', message = 'Preencha todos os campos!')

    else:
        Banco()
        cursor.execute('INSERT INTO `usuario` (email, senha) VALUES(?, ?)', str(entry_email.get()), float(entry_senha.get()))
        conexao.commit()
        cursor.close()
        conexao.close()
        tkinter.messagebox.showinfo(title = 'Sucesso!', message = 'Login realizado!') 

    bt_entrar = Button(screen_login, text = 'ENTRAR', bg = '#85AEF2', font = ('Arial', 10, 'bold'), command = bt_click_entrar)
    bt_entrar.place(x = 300, y = 360) 
    bt_voltar = Button(screen_login, text = 'VOLTAR', bg = '#85AEF2', font = ('Arial', 10, 'bold'), command = bt_click_voltar)
    bt_voltar.place(x = 300, y = 400) 
    
    screen_login.mainloop()


def Cadastro():
    screen_cadastro = Tk()
    screen_cadastro.title('ENTRANDO...')
    screen_cadastro.configure(bg = '#0B2161')
    screen_cadastro.geometry('700x500+500+500')

    tela_cadastro = PhotoImage(file = 'tela_cadastro.png')
    label_cadastro = Label(image = tela_cadastro)
    label_cadastro.pack(side = RIGHT)
  
    entry_usuario = Entry(screen_cadastro, justify = CENTER)
    entry_usuario.place(x = 105, y = 165)
    entry_email = Entry(screen_cadastro, justify = CENTER)
    entry_email.place(x = 105, y = 225)
    entry_senha = Entry(screen_cadastro, justify = CENTER)
    entry_senha.place(x = 105, y = 285)
    entry_senha['show'] = '*'
  
    novoUsuario = entry_usuario.get()
    novoEmail = entry_email.get()
    novaSenha = entry_senha.get()
    usuario.append(novoUsuario)
    email.append(novoEmail)
    senha.append(novaSenha)

    def bt_click_criar():
        screen_cadastro.destroy()
        Menu()
      
    def bt_click_voltar():
      screen_cadastro.destroy()
      Iniciar()

    if entry_usuario.get() == '' or entry_email.get() == '' or entry_senha.get() == '':
       tkinter.messagebox.showinfo(title = 'Atenção!', message = 'Preencha todos os campos!')

    else:
        Banco()
        cursor.execute('INSERT INTO `usuario` (usuario, email, senha) VALUES(?, ?, ?)', str(entry_usuario.get()), str(entry_email.get()), float(entry_senha.get()))
        conexao.commit()
        cursor.close()
        conexao.close()
        tkinter.messagebox.showinfo(title = 'Sucesso!', message = 'Cadastro realizado!') 

    bt_criar = Button(screen_cadastro, text = 'CRIAR', bg = '#85AEF2', font = ('Arial', 10, 'bold'), command = bt_click_criar)
    bt_criar.place(x = 105, y = 330)
    bt_voltar = Button(screen_cadastro, text = 'VOLTAR', bg = '#85AEF2', font = ('Arial', 10, 'bold'), command = bt_click_voltar)
    bt_voltar.place(x = 105, y = 360)

    screen_cadastro.mainloop()
