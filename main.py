from tkinter import *
from usuario import *


def Iniciar():
    screen_iniciar = Tk()
    screen_iniciar.title('BEM VINDO(A) AO PLANNER')
    screen_iniciar.configure(bg = '#0B2161')
    screen_iniciar.geometry('700x500+200+200') 
    
    tela_iniciar = PhotoImage(file = 'tela_iniciar.png')
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
      
    bt_cadastro = Button(screen_iniciar, text = 'CADASTRO', bg = '#C8E0EB', font = ('Arial', 13, 'bold'), command = bt_click_cadastro, borderwidth = 0)
    bt_cadastro.place(x = 290, y = 365)
  
    screen_iniciar.mainloop()
  
Iniciar()
