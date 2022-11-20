from tkinter import *
from usuario import *


global usuario, email, senha
usuario = []
email = []
senha = []


def Iniciar():
    screen_iniciar = Tk()
    screen_iniciar.title('BEM VINDO(A) AO PLANNER')
    screen_iniciar.configure(bg = '#0B2161')
    screen_iniciar.geometry('700x700+500+500') 
    
    window_iniciar = Label(screen_iniciar, text = 'Planner Acadêmico', bg = '#85AEF2', fg = '#0B0B3B', font = ('Times New Roman', 20, 'bold'))
    window_iniciar.pack(ipadx = 30, ipady = 30, padx = 1, pady = 1, side = 'top', fill = X, expand = False)
    
    label_login = Label(screen_iniciar, text = 'Entrar com uma conta existente', bg = '#0B2161', fg = 'white', font = ('Times New Roman', 12))
    label_login.place(x = 30, y = 140)
    label_cadastro = Label(screen_iniciar, text = 'Cadastrar-se', bg = '#0B2161', fg = 'white', font = ('Times New Roman', 12))
    label_cadastro.place(x = 30, y = 230)

    def bt_click_login():
        screen_iniciar.destroy()
        Login()

    bt_login = Button(screen_iniciar, text = 'LOGIN', bg = '#85AEF2', font = ('Arial', 10, 'bold'), command = bt_click_login)
    bt_login.place(x = 35, y = 170)

    def bt_click_cadastro():
        screen_iniciar.destroy()
        Cadastro()
      
    bt_cadastro = Button(screen_iniciar, text = 'CADASTRO', bg = '#85AEF2', font = ('Arial', 10, 'bold'), command = bt_click_cadastro)
    bt_cadastro.place(x = 35, y = 260)
  
    screen_iniciar.mainloop()
  
Iniciar()
