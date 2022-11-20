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


def Banco():
    global conexao, cursor
  
    conexao = sqlite3.connect('banco.db')
    cursor = conexao.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS `usuario` (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, usuario TEXT, email TEXT, senha TEXT)')
    

def Login():
    screen_login = Tk()
    screen_login.title('ENTRANDO...')
    screen_login.configure(bg = '#0B2161')
    screen_login.geometry('700x500+500+500') 
    
    window_login = Label(screen_login, text = 'Login', bg = '#85AEF2', fg = '#0B2161', font = ('Times New Roman', 20, 'bold'))
    window_login.pack(ipadx = 30, ipady = 30, padx = 1, pady = 1, side = 'top', fill = X, expand = False)
    
    label_email = Label(screen_login, text = 'Email', bg = '#0B2161', fg = 'white', font = ('Times New Roman', 12))
    label_email.place(x = 100, y = 140)
    label_senha = Label(screen_login, text = 'Senha', bg = '#0B2161', fg = 'white', font = ('Times New Roman', 12))
    label_senha.place(x = 100, y = 200)
  
    entry_email = Entry(screen_login, justify = CENTER)
    entry_email.place(x = 105, y = 170)
    entry_senha = Entry(screen_login, justify = CENTER)
    entry_senha.place(x = 105, y = 230)

    novoEmail = entry_email.get()
    novaSenha = entry_senha.get()
    email.append(novoEmail)
    senha.append(novaSenha)  
  
    def bt_click_entrar():
        screen_login.destroy()
        Menu()

    if entry_email.get() == '' or entry_senha.get() == '':
       tkinter.messagebox.showinfo(title = 'Atenção!', message = 'Preencha todos os campos!')

    else:
        Banco()
        cursor.execute('INSERT INTO `usuario` (email, senha) VALUES(?, ?)', str(entry_email.get()), int(entry_senha.get()))
        conexao.commit()
        cursor.close()
        conexao.close()
        tkinter.messagebox.showinfo(title = 'Sucesso!', message = 'Login realizado!') 

    bt_entrar = Button(screen_login, text = 'ENTRAR', bg = '#85AEF2', font = ('Arial', 10, 'bold'), command = bt_click_entrar)
    bt_entrar.place(x = 110, y = 280) 
    
    screen_login.mainloop()


def Cadastro():
    screen_cadastro = Tk()
    screen_cadastro.title('ENTRANDO...')
    screen_cadastro.configure(bg = '#0B2161')
    screen_cadastro.geometry('700x500+500+500')
    
    window_cadastro = Label(screen_cadastro, text = 'Cadastro', bg = '#85AEF2', fg = '#0B2161', font = ('Times New Roman', 20, 'bold'))
    window_cadastro.pack(ipadx = 30, ipady = 30, padx = 1, pady = 1, side = 'top', fill = X, expand = False)
    
    label_usuario = Label(screen_cadastro, text = 'User',  bg = '#0B2161', fg = 'white', font = ('Times New Roman', 12))
    label_usuario.place(x = 100, y = 140)
    label_email = Label(screen_cadastro, text = 'Email', bg = '#0B2161', fg = 'white',  font = ('Times New Roman', 12))
    label_email.place(x = 100, y = 200)  
    label_senha = Label(screen_cadastro, text = 'Senha', bg = '#0B2161', fg = 'white',  font = ('Times New Roman', 12))
    label_senha.place(x = 100, y = 260)  
  
    entry_usuario = Entry(screen_cadastro, justify = CENTER)
    entry_usuario.place(x = 105, y = 165)
    entry_email = Entry(screen_cadastro, justify = CENTER)
    entry_email.place(x = 105, y = 225)
    entry_senha = Entry(screen_cadastro, justify = CENTER)
    entry_senha.place(x = 105, y = 285)
  
    novoUsuario = entry_usuario.get()
    novoEmail = entry_email.get()
    novaSenha = entry_senha.get()
    usuario.append(novoUsuario)
    email.append(novoEmail)
    senha.append(novaSenha)

    def bt_click_criar():
        screen_cadastro.destroy()
        Menu()

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

    screen_cadastro.mainloop()
