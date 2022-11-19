from tkinter import *
from calendario import *

global usuarios, emails, senhas
usuarios = []
emails = []
senhas = []

def Login():
  principal.destroy()
  
  tela_login = Tk()
  tela_login.title('EFETUAR LOGIN')
  tela_login.configure(background = '#0B2161')
  tela_login.geometry('700x500+500+500') 
  
  label_login = Label(tela_login, text = 'LOGIN', 
                      bg = '#85AEF2', fg = '#0B2161', font = ('Times New Roman', 20))
  label_login.place(x = 296, y = 20)

  label1 = Label(tela_login, text = 'Email', bg = '#0B2161')
  label1.place(x = 300, y = 65)
  
  entrada1 = Entry(tela_login, justify = CENTER)
  entrada1.place(x = 240, y = 85)

  label2 = Label(tela_login, text = 'Senha', bg = '#0B2161')
  label2.place(x = 300, y = 125)
  
  entrada2 = Entry(tela_login, justify = CENTER)
  entrada2.place(x = 240, y = 145)
  # ta faltando def bt_click pra login \\ pra ver se email e senha tao corretos
  botao_entrar = Button(tela_login, command = bt_click3, text = 'ENTRAR')
  botao_entrar.place(x = 285, y = 185)
  
def CriarConta():
  criarConta = Tk()
  criarConta.title('CADASTRE-SE')
  criarConta.configure(background = '#0B2161')
  criarConta.geometry('700x500+500+500')
  
  label_cadastro = Label(criarConta, text = 'Cadastro', 
                         bg = '#85AEF2', fg = '#0B2161', font = ('Times New Roman', 20, 'bold'))
  label_cadastro.pack(ipadx = 30, ipady = 30, padx = 1, pady = 1, 
                      side = 'top', fill = X, expand = False)
  
  label1 = Label(criarConta, text = 'User', 
                 bg = '#0B2161', fg = 'white', font = ('Times New Roman', 12))
  label1.place(x = 100, y = 140)
  
  entrada1 = Entry(criarConta, justify = CENTER)
  entrada1.place(x = 105, y = 165)
  
  label2 = Label(criarConta, text = 'Email', 
                 bg = '#0B2161', fg = 'white', font = ('Times New Roman', 12))
  label2.place(x = 100, y = 200)
  
  entrada2 = Entry(criarConta, justify = CENTER)
  entrada2.place(x = 105, y = 225)

  label3 = Label(criarConta, text = 'Senha', 
                 bg = '#0B2161', fg = 'white',  font = ('Times New Roman', 12))
  label3.place(x = 100, y = 260)
  
  entrada3 = Entry(criarConta, justify = CENTER)
  entrada3.place(x = 105, y = 285)
  
  # por aqui ainda precisa de condição se o usuario colocou todas as infos
  def bt_clickCriarConta():
    novoUsuario = entrada1.get()
    novoEmail = entrada2.get()
    novaSenha = entrada3.get()
    
    usuarios.append(novoUsuario)
    emails.append(novoEmail)
    senhas.append(novaSenha)

    criarConta.destroy()
  
  botao_criar = Button(criarConta, command = bt_clickCriarConta, text = 'CRIAR', 
                       bg = '#85AEF2', font = ('Arial', 10, 'bold'))
  botao_criar.place(x = 105, y = 330)
  
  criarConta.mainloop()
  Menu()
