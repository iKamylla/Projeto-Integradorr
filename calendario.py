from tkinter import *
from usuario import *
from agendamento import *


def Menu():
    screen_menu = Tk()
    screen_menu.title('CALENDÁRIO')
    screen_menu.configure(bg = '#0B2161')
    screen_menu.geometry('700x500+500+500')
     
    window_menu = Label(screen_menu, text = 'MENU', bg = '#85AEF2', fg = '#0B0B3B', font = ('Times New Roman', 20, 'bold'))
    window_menu.pack(ipadx = 30, ipady = 30, padx = 1, pady = 1, side = 'top', fill = X, expand = False)
        
    label_criar_even = Label(screen_menu, text = '1 - Criar evento', bg = '#0B2161', fg = 'white', font = ('Times New Roman', 12))
    label_criar_even.place(x = 100, y = 150)
    label_acessar_even = Label(screen_menu, text = '2 - Acesssar evento', bg = '#0B2161', fg = 'white', font = ('Times New Roman', 12))
    label_acessar_even.place(x = 100, y = 210)
    label_encerrar = Label(screen_menu, text = '3 - Encerrar sessão', bg = '#0B2161', fg = 'white', font = ('Times New Roman', 12))
    label_encerrar.place(x = 100, y = 270)

    def bt_click_criar():
        screen_menu.destroy()
        Criar_Evento()

    bt_criar_even = Button(screen_menu, text = 'CRIAR', bg = '#85AEF2', fg = 'black', font = ('Arial', 10, 'bold'), command = Criar_Evento)
    bt_criar_even.place(x = 350, y = 150)    
      
    def bt_click_acessar():
        screen_menu.destroy()
        Acessar_Evento()

    bt_acessar_even = Button(screen_menu, text = 'ACESSAR', bg = '#85AEF2', fg = 'black', font = ('Arial', 10, 'bold'), command = Acessar_Evento)
    bt_acessar_even.place(x = 350, y = 210)

    def bt_click_sair():
        screen_menu.destroy()
        Encerrar()

    bt_encerrar = Button(screen_menu, text = 'SAIR', bg = '#85AEF2', fg = 'black', font = ('Arial', 10, 'bold'), command = Encerrar)
    bt_encerrar.place(x = 350, y = 270)

    screen_menu.mainloop()
  