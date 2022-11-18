from tkinter import *
from usuario import *


def Menu():
  
  principal = Tk()
  principal.title('Planner')
  principal.configure(background = '#045FB4')
  principal.geometry('700x700+500+500')

  
  label6 = Label(text = 'MENU', background = '#1E90FF')
  label6.place(x = '310', y = '20')
  label6_1 = Label(text = '1 - Criar evento', background = '#1E90FF')
  label6_1.place(x = '280', y = '60')
  label6_2 = Label(text = '2 - Acesssar evento', background = '#1E90FF' )
  label6_2.place(x = '280', y = '80')
  label6_3 = Label(text = '3 - Sair', background = '#1E90FF')
  label6_3.place(x = '280', y = '100')

  
  entrada1 = Entry()
  entrada1.place(x = '280', y = '125')

  
  botao1 = Button(principal, command = bt_click, text = 'LOGIN')
  botao1.place(x = '286', y = '90')

  
  # = Button (command = lambda: [screen.destroy(),novatela()])
  #botao1.place(x = '286', y = '90')
  

def novatela():
  
  principal = Tk()
  principal.title('Planner')
  principal.configure(background = '#1E90FF')
  principal.geometry('700x700+500+500')


  #while opcao == 1 or opcao == 2 or opcao == 3:
  #  if opcao == 1:
  #    print('aaaaa')
    #if opcao == 2:
    #if opcao == 3:
