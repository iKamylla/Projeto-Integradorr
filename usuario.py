from tkinter import *
import tkinter.messagebox
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
from calendario import *
from conexao import *


#Iniciar
conexao = iniciar_conexao()

tabela_user = 'CREATE TABLE IF NOT EXISTS usuarios(nome, email, senha)'
criar_tabela(conexao, tabela_user)


def Iniciar():
    screen_iniciar = Tk()
    screen_iniciar.title('BEM VINDO(A) AO PLANNER')
    screen_iniciar.configure(bg = '#0B2161')
    screen_iniciar.geometry('700x500+200+200') 
    
    tela_iniciar = PhotoImage(file = 'images/tela_iniciar.png')
    label_iniciar = Label(image = tela_iniciar)
    label_iniciar.pack(side = RIGHT)

    def bt_click_login():
        screen_iniciar.destroy()
        Login()

    bt_login = Button(screen_iniciar, text = 'LOGIN', bg = '#C8E0EB', font = ('Arial', 13, 'bold'), command = bt_click_login, borderwidth = 0)
    bt_login.place(x = 300, y = 255)

    def bt_click_cadastro():
        screen_iniciar.destroy()
        Cadastro()
      
    bt_cadastro = Button(screen_iniciar, text = 'CADASTRO', bg = '#C8E0EB', font = ('Arial', 13, 'bold'), command = bt_click_cadastro, borderwidth =0)
    bt_cadastro.place(x = 290, y = 365)
  
    screen_iniciar.mainloop()


def Login():
    screen_login = Tk()
    screen_login.title('ENTRANDO...')
    screen_login.configure(bg = '#0B2161')
    screen_login.geometry('700x500+500+500') 

    tela_login = PhotoImage(file = 'images/tela_login.png')
    label_login = Label(image = tela_login)
    label_login.pack(side = RIGHT)
  
    entry_email = Entry(screen_login, justify = CENTER)
    entry_email.place(x = 260, y = 210)
    entry_senha = Entry(screen_login, justify = CENTER)
    entry_senha.place(x = 260, y = 310)
    entry_senha['show'] = '*'

      
    def bt_click_entrar():
        novoEmail = entry_email.get()
        novaSenha = entry_senha.get()

        global confirmEmail, confirmSenha
        confirmEmail = False
        confirmSenha = False
      
        conexao = iniciar_conexao()

        buscar = 'SELECT * FROM usuarios'
        aux = buscando_dados(conexao, buscar)

        print(aux)
        for index in range(len(aux)):
          for busca in range(3):
            lista = aux[index]
        
            if novaSenha == lista[busca]:
               confirmEmail = True

        for index in range(len(aux)):
          for busca in range(3):
              lista = aux[index]
        
              if novoEmail == lista[busca]:
                 confirmSenha = True

        if confirmEmail == True and confirmSenha == True:
           screen_login.destroy()
           Menu()
        Login()

    def bt_click_voltar():
        screen_login.destroy()
        Iniciar()
        
    if entry_email.get() == '' or entry_senha.get() == '':
       tkinter.messagebox.showinfo(title = 'Atenção!', message = 'Preencha todos os campos!')

    bt_entrar = Button(screen_login, text = 'ENTRAR', bg = '#85AEF2', font = ('Arial', 10, 'bold'), command = bt_click_entrar)
    bt_entrar.place(x = 240, y = 360) 
    bt_voltar = Button(screen_login, text = 'VOLTAR', bg = '#85AEF2', font = ('Arial', 10, 'bold'), command = bt_click_voltar)
    bt_voltar.place(x = 350, y = 360) 
    
    screen_login.mainloop()


def Cadastro():
    screen_cadastro = Tk()
    screen_cadastro.title('ENTRANDO...')
    screen_cadastro.configure(bg = '#0B2161')
    screen_cadastro.geometry('700x500+500+500')

    tela_cadastro = PhotoImage(file = 'images/tela_cadastro.png')
    label_cadastro = Label(image = tela_cadastro)
    label_cadastro.pack(side = RIGHT)
  
    entry_usuario = Entry(screen_cadastro, justify = CENTER)
    entry_usuario.place(x = 260, y = 215)
    entry_email = Entry(screen_cadastro, justify = CENTER)
    entry_email.place(x = 260, y = 285)
    entry_senha = Entry(screen_cadastro, justify = CENTER)
    entry_senha.place(x = 260, y = 360)
    entry_senha['show'] = '*'
  

    def bt_click_criar():
      novoUsuario = entry_usuario.get()
      novoEmail = entry_email.get()
      novaSenha = entry_senha.get()
      conexao = iniciar_conexao()
      inserir = "INSERT INTO usuarios(nome, email, senha) VALUES ('" + (novoUsuario) + "', '" + (novoEmail) + "', '" + (novaSenha)+ "')"
      inserir_usuario(conexao, inserir)
      destruir()

    def destruir():
        screen_cadastro.destroy()
        Iniciar()
      
    def bt_click_voltar():
        screen_cadastro.destroy()
        Iniciar()

    if entry_usuario.get() == '' or entry_email.get() == '' or entry_senha.get() == '':
       tkinter.messagebox.showinfo(title = 'Atenção!', message = 'Preencha todos os campos!') 

    bt_criar = Button(screen_cadastro, text = 'CRIAR', bg = '#85AEF2', font = ('Arial', 10, 'bold'), command = bt_click_criar)
    bt_criar.place(x = 250, y = 390)
    bt_voltar = Button(screen_cadastro, text = 'VOLTAR', bg = '#85AEF2', font = ('Arial', 10, 'bold'), command = bt_click_voltar)
    bt_voltar.place(x = 340, y = 390)

    screen_cadastro.mainloop()

  
Iniciar()
