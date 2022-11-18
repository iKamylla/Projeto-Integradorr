from tkinter import *
from usuario import *

global usuarios, emails, senhas
usuarios = []
emails = []
senhas = []

def Inicio():
  principal = Tk()
  principal.title('BEM VINDO(A) AO PLANNER')
  principal.configure(background = '#1E90FF')
  principal.geometry('700x500+500+500') 

  #img_logo = PhotoImage(file = 'logoAzuli.jpeg')
  #logo = Label(principal, image = img_logo).pack()
  #logo.pack(side = RIGHT)
  
  def bt_click():
    Login()
  
  def bt_click2():
    principal.destroy()
    CriarConta()

  botao1 = Button(principal, command = bt_click, text = 'LOGIN')
  botao1.place(x = '286', y = '90')

  botao2 = Button(principal, command = bt_click2, text = 'CRIAR CONTA')
  botao2.place(x = '266', y = '160')

  principal.mainloop()

Inicio()