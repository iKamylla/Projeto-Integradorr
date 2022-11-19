from tkinter import *
from usuario import *

global usuarios, emails, senhas
usuarios = []
emails = []
senhas = []

def Inicio():
  principal = Tk()
  principal.title('BEM VINDO(A) AO PLANNER')
  principal.configure(background = '#0B2161')
  principal.geometry('700x700+500+500') 
  
  label1 = Label(text = 'Planner Acadêmico', 
                 bg = '#85AEF2', fg = '#0B0B3B', 
                 font = ('Times New Roman', 20, 'bold'))
  label1.pack(ipadx = 30, ipady = 30, padx = 1, pady = 1, 
              side = 'top', fill = X, expand = False)
  
  #img_logo = PhotoImage(file = 'logoAzuli.jpeg')
  #logo = Label(principal, image = img_logo).pack()
  #logo.pack(side = RIGHT)
  
  def bt_clickLogin(): # seria bom mostrar msg falando q o usuario nao tem conta ainda
    Login()
  
  def bt_clickCadastro():
    principal.destroy()
    CriarConta()

  label2 = Label(text = 'Entrar com uma conta existente', bg = '#0B2161', 
                 fg = 'white', font = ('Times New Roman', 12))
  label2.place(x = 30, y = 140)
  
  botao1 = Button(principal, command = bt_clickLogin, text = 'LOGIN', 
                  bg = '#85AEF2', font = ('Arial', 10, 'bold'))
  botao1.place(x = 35, y = 170)

  label3 = Label(text = 'Cadastrar-se', 
                 bg = '#0B2161', fg = 'white', 
                 font = ('Times New Roman', 12))
  label3.place(x = 30, y = 230)
  
  botao2 = Button(principal, command = bt_clickCadastro, text = 'CADASTRO', 
                  bg = '#85AEF2', font = ('Arial', 10, 'bold'))
  botao2.place(x = 35, y = 260)

  principal.mainloop()

Inicio()
