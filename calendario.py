from tkinter import *
from usuario import *

def Menu():
  tela_menu = Tk()
  tela_menu.title('MENU')
  tela_menu.configure(background = '#0B2161')
  tela_menu.geometry('700x500+500+500')

  label_menu = Label(tela_menu, text = 'MENU', background = '#85AEF2', foreground = '#0B0B3B', font = ('Times New Roman', 20))
  label_menu.pack(ipadx = 30, ipady = 30, padx = 1, pady = 1, side = 'top', fill = X, expand = False)
  
  label1 = Label(tela_menu, text = '1 - Criar evento', background = '#0B2161', foreground = 'white', font = ('Times New Roman', 12))
  label1.place(x = 100, y = 150)
  
  label2 = Label(tela_menu, text = '2 - Acesssar evento', background = '#0B2161', foreground = 'white', font = ('Times New Roman', 12))
  label2.place(x = 100, y = 210)
  
  label3 = Label(tela_menu, text = '3 - Encerrar sessão', background = '#0B2161', foreground = 'white', font = ('Times New Roman', 12))
  label3.place(x = 100, y = 270)
  
  # opção 1 vai pra criar evento \\ banco de dados
  def bt_clickOpcao1():
    tela_menu.destroy()
    print('a')
    
  botao_criar_evento = Button(tela_menu, command = bt_clickOpcao1, text = '1')
  botao_criar_evento.place(x = 350, y = 150)

  # opção 2 mostrar lista de eventos \\ banco de dados
  def bt_clickOpcao2():
    tela_menu.destroy()
    print('a')
    
  botao_criar_evento = Button(tela_menu, command = bt_clickOpcao2, text = '2')
  botao_criar_evento.place(x = 350, y = 210)

  # opção 3 encerra a sessão
  def bt_clickOpcao3():
    tela_menu.destroy()
    print('a')
    
  botao_criar_evento = Button(tela_menu, command = bt_clickOpcao3, text = '3')
  botao_criar_evento.place(x = 350, y = 270)

    
  # = Button(command = lambda: [screen.destroy(),novatela()])
  #botao_login.place(x = '286', y = '90')
  

#def NovaTela():
#  principal = Tk()
#  principal.title('Planner')
#  principal.configure(background = '#1E90FF')
#  principal.geometry('700x500+500+500')

  #while opcao == 1 or opcao == 2 or opcao == 3:
  #  if opcao == 1:
  #    print('aaaaa')
    #if opcao == 2:
    #if opcao == 3:
