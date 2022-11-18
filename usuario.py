from tkinter import *
from usuario import *

global usuarios, emails, senhas
usuarios = []
emails = []
senhas = []

def Login():
  principal.destroy()

  tela_login = Tk()
  tela_login.title('EFETUAR LOGIN')
  tela_login.configure(background = '#1E90FF')
  tela_login.geometry('700x500+500+500') 

  label2 = Label(text = 'LOGIN', background = '#1E90FF')
  label2.place(x = '296', y = '20')

  label3 = Label(text = 'Email', background = '#1E90FF')
  label3.place(x = '300', y = '65')
  entrada1 = Entry(email)
  entrada1.place(x = '240', y = '85')

  label4 = Label(text = 'Senha', background = '#1E90FF')
  label4.place(x = '300', y = '125')
  entrada2 = Entry(senha)
  entrada2.place(x = '240', y = '145')

  botao3 = Button(tela_login, command = bt_click3, text = 'ENTRAR')
  botao3.place(x = '285', y = '185')
  
def CriarConta():
  criarConta = Tk()
  criarConta.title('CADASTRE-SE')
  criarConta.configure(background = '#1E90FF')
  criarConta.geometry('700x700+500+500')
  
  label2 = Label(criarConta,text = 'CRIAR CONTA', background = '#1E90FF')
  label2.place(x = '275', y = '20')
  
  label3 = Label(criarConta,text = 'Nome de usuário', background = '#1E90FF')
  label3.place(x = '267', y = '70')
  entrada1 = Entry(criarConta)
  entrada1.place(x = '240', y = '90')
  
  label4 = Label( criarConta,text = 'Email', background = '#1E90FF')
  label4.place(x = '300', y = '120')
  entrada2 = Entry(criarConta)
  entrada2.place(x = '240', y = '140')

  label5 = Label( criarConta, text = 'Senha', background = '#1E90FF')
  label5.place(x = '300', y = '170')
  entrada3 = Entry(criarConta)
  entrada3.place(x = '240', y = '190')
  
  def bt_click3():
    self.__nome = entrada1.get()
    self.__email = entrada2.get()
    self.__senha = entrada3.get()
    
    usuarios.append(self.__nome)
    email.append(self.__email)
    senha.append(self.__senha)
    
    criarConta.destroy()
  
  botao3 = Button(criarConta, command = bt_click3, text = 'CRIAR')
  botao3.place(x = '292', y = '230')

  criarConta.mainloop()

  Menu()
