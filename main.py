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
  
  label1 = Label(text = 'Planner Acadêmico', background = '#85AEF2', foreground = '#0B0B3B', font = ('Times New Roman', 20))
  label1.pack(ipadx = 30, ipady = 30, padx = 1, pady = 1, side = 'top', fill = X, expand = False)
  
  #img_logo = PhotoImage(file = 'logoAzuli.jpeg')
  #logo = Label(principal, image = img_logo).pack()
  #logo.pack(side = RIGHT)
  
  def bt_clickLogin(): # seria bom mostrar msg falando q o usuario nao tem conta ainda
    Login()
  
  def bt_clickCadastro():
    principal.destroy()
    CriarConta()

  label2 = Label(text = 'Entrar com uma conta existente', background = '#0B2161', foreground = 'white', font = ('Times New Roman', 12))
  label2.place(x = 30, y = 170)
  
  botao1 = Button(principal, command = bt_clickLogin, text = 'LOGIN')
  botao1.place(x = 35, y = 200)

  label3 = Label(text = 'Cadastrar-se', background = '#0B2161', foreground = 'white', font = ('Times New Roman', 12))
  label3.place(x = 30, y = 260)
  
  botao2 = Button(principal, command = bt_clickCadastro, text = 'CADASTRO')
  botao2.place(x = 35, y = 295)

  principal.mainloop()

Inicio()
