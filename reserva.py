import tkinter as tk
from tkinter import ttk, PhotoImage
from PIL import Image, ImageTk

# cores
cor_preta = "#f0f3f5" 
cor_branca = "#f3ffff"
cor_verde = "#3fb5a3" 
valr = "#38576b" 
letr = "#403d3d" 

def login_admin():
    print("Administrador")
    

def login_usuario():
    print("Usuário Comum")

# tela de login
def criar_tela_login():
    tela_login = tk.Tk()
    tela_login.title('Tela de Login')
    tela_login.geometry('600x400')
    tela_login.configure(background=cor_verde)
    tela_login.resizable(width=False, height=False)

    
    titulo = tk.Label(tela_login, text="Reserva de materiais (IME)", font=('Arial', 18), bg=cor_verde, fg=letr)
    titulo.pack(pady=20)
    
    img1 = Image.open("C:/Users/jvmor/OneDrive/Área de Trabalho/proje_reserva_materiais_CA/MorelPeixoto_EstoqueCA/simbolo_eb.png")
    img1 = img1.resize((100, 120), Image.Resampling.LANCZOS) 
    imagem1 = ImageTk.PhotoImage(img1) 
    
    img2 = Image.open("C:/Users/jvmor/OneDrive/Área de Trabalho/proje_reserva_materiais_CA/MorelPeixoto_EstoqueCA/simbolo_ime.png")
    img2 = img2.resize((100, 120), Image.Resampling.LANCZOS) 
    imagem2 = ImageTk.PhotoImage(img2)
    
    img_label1 = tk.Label(tela_login, image=imagem1, bg=cor_verde)
    img_label1.place(x=0, y=0)

    img_label2 = tk.Label(tela_login, image=imagem2, bg=cor_verde)
    img_label2.place(x=500, y=0)

    # entradas de e-mail e senha
    label_usuario = tk.Label(tela_login, text="E-Mail", bg=cor_verde, fg=letr, font=('Arial', 12))
    label_usuario.pack(pady=5)
    entrada_usuario = tk.Entry(tela_login, width=30)
    entrada_usuario.pack(pady=5)

    label_senha = tk.Label(tela_login, text="Senha", bg=cor_verde, fg=letr, font=('Arial', 12))
    label_senha.pack(pady=5)
    entrada_senha = tk.Entry(tela_login, show="*", width=30)
    entrada_senha.pack(pady=5)

    # botão de adm e usuário comum
    botao_admin = ttk.Button(tela_login, text="Login como Admin", command=login_admin)
    botao_admin.pack(pady=10)

    botao_usuario = ttk.Button(tela_login, text="Login como Usuário Comum", command=login_usuario)
    botao_usuario.pack(pady=10)

    tela_login.mainloop()

# tela de login
criar_tela_login()
