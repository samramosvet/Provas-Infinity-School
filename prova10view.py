import tkinter as tk
from tkinter import *
from tkinter import ttk
import pyodbc

# creates a Tk() object
#janela = Tk()

# sets the geometry of main
# root window
#master.geometry("200x200")

############## sistema ##############

def logar():
    dados_conexao = ("Driver={SQLite3 ODBC Driver};Server=localhost;Database=G:/Meu Drive/Python Exercícios Jupyter 2022/Pyodbc/magazine.db")
    conexao = pyodbc.connect(dados_conexao)
    cursor = conexao.cursor()

    cursor.execute(f'SELECT * FROM usuarios WHERE nome = "{nome_tela1.get()}" AND email = "{email_tela1.get()}"')
    valores = cursor.fetchall()
    for valor in valores:
        nome_login = valor[1]
        email_login = valor[3]
    try:
        if nome_login == 'root' and email_login == 'root@gmail.com':
            print('Login realizado com sucesso!')
            btn = Button(janela, text="Login Válido! Clique Aqui!", command=openNewWindow)
            btn.place(x = 570, y = 340, width = 200)
    except:
            print('Login ou E-mail inválidos!')
            btn = Button(janela, text="Login Inválido! Tente Novamente!")
            btn.place(x=570, y=340, width = 200)

    cursor.close()
    conexao.close()

############## janela ##############

janela = Tk()

janela.title('Magazine Loja - Login')
janela.geometry("786x465")
janela.configure(bg = "#ffffff")
canvas = Canvas(
    janela,
    bg = "#ffffff",
    height = 465,
    width = 786,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_tela1_img = PhotoImage(file = f"background_tela1.png")
background_tela1 = canvas.create_image(
    393.0, 232.5,
    image=background_tela1_img)

# botão enviar
enviar_tela1_img = PhotoImage(file = f"enviar_tela1.png")
botao_enviar_tela1 = Button(
    image = enviar_tela1_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = logar,
    relief = "flat")

botao_enviar_tela1.place(
    x = 336, y = 410,
    width = 113,
    height = 38)

# nome
nome_img_tela1 = PhotoImage(file = f"nome_img_tela1.png")
nome_bg_tela1 = canvas.create_image(
    393.0, 313.5,
    image = nome_img_tela1)

nome_tela1 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

nome_tela1.place(
    x = 255, y = 295,
    width = 276,
    height = 35)

# e-mail
email_img_tela1 = PhotoImage(file = f"email_img_tela1.png")
email_bg_tela1 = canvas.create_image(
    393.0, 381.5,
    image = email_img_tela1)

email_tela1 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

email_tela1.place(
    x = 255, y = 363,
    width = 276,
    height = 35)

# function to open a new window
# on a button click
def openNewWindow():
    # Toplevel object which will
    # be treated as a new window

    def listar_produtos_loja():
        dados_conexao = ("Driver={SQLite3 ODBC Driver};Server=localhost;Database=G:/Meu Drive/Python Exercícios Jupyter 2022/Pyodbc/magazine.db")
        conexao = pyodbc.connect(dados_conexao)
        cursor = conexao.cursor()

        cursor.execute(f'SELECT * FROM produtos')
        valores = cursor.fetchall()

        texto = ""
        for cod_prod, produto, preco, descricao, categoria in valores:
            texto = texto + f'''
            -------------------------
            Código Produto: {cod_prod}
            Produto: {produto}
            Preço: R$ {preco:.2f}
            Descrição: {descricao}
            Categoria: {categoria}
            '''

        # deletar tudo da caixa de texto
        caixa_texto.delete("1.0", END)
        # escrever na caixa de texto
        caixa_texto.insert("1.0", texto)

        cursor.close()
        conexao.close()

    def salvar_produto_carrinho():
        dados_conexao = ("Driver={SQLite3 ODBC Driver};Server=localhost;Database=G:/Meu Drive/Python Exercícios Jupyter 2022/Pyodbc/magazine.db")
        conexao = pyodbc.connect(dados_conexao)
        cursor = conexao.cursor()

        cursor.execute(f'SELECT * FROM produtos WHERE produto = "{produto.get()}"')
        valores = cursor.fetchall()
        for valor in valores:
            produto_carrinho = valor[1]
            preco_carrinho = valor[2]
            descricao_carrinho = valor[3]
            categoria_carrinho = valor[4]

        cursor.execute(f'''
            INSERT INTO carrinho (produto, preco, descricao, categoria)
            VALUES
            ("{produto_carrinho}", {preco_carrinho}, "{descricao_carrinho}", "{categoria_carrinho}")
            ''')
        cursor.commit()

        # deletar tudo da caixa de texto
        produto.delete(0, "end")
        preco.delete(0, "end")
        descricao.delete(0, "end")
        categoria.delete(0, "end")
        caixa_texto.delete('1.0', END)

        # escrever na caixa de texto
        caixa_texto.insert('1.0', f"{produto_carrinho} adicionado ao Carrinho com sucesso!")

        cursor.close()
        conexao.close()

    def listar_carrinho():
        dados_conexao = ("Driver={SQLite3 ODBC Driver};Server=localhost;Database=G:/Meu Drive/Python Exercícios Jupyter 2022/Pyodbc/magazine.db")
        conexao = pyodbc.connect(dados_conexao)
        cursor = conexao.cursor()

        cursor.execute(f'SELECT * FROM carrinho')
        valores = cursor.fetchall()

        if not valores:
            # deletar tudo da caixa de texto
            caixa_texto.delete('1.0', END)

            # escrever na caixa de texto
            caixa_texto.insert('1.0', "Carrinho de Compras Vazio!")

        else:
            cursor.execute(f'SELECT * FROM carrinho')
            valores = cursor.fetchall()

            texto = ""
            for cod_prod, produto, preco, descricao, categoria in valores:
                texto = texto + f'''
            -------------------------
            Código Produto: {cod_prod}
            Produto: {produto}
            Preço: R$ {preco:.2f}
            Descrição: {descricao}
            Categoria: {categoria}
            '''

            # deletar tudo da caixa de texto
            caixa_texto.delete("1.0", END)
            # escrever na caixa de texto
            caixa_texto.insert("1.0", texto)

            cursor.close()
            conexao.close()

    def deletar_produtos_carrinho():
        dados_conexao = ("Driver={SQLite3 ODBC Driver};Server=localhost;Database=G:/Meu Drive/Python Exercícios Jupyter 2022/Pyodbc/magazine.db")
        conexao = pyodbc.connect(dados_conexao)
        cursor = conexao.cursor()

        cursor.execute(f'''
        DELETE FROM carrinho 
        WHERE produto="{produto.get()}"
        ''')
        cursor.commit()

        # deletar tudo da caixa de texto
        caixa_texto.delete("1.0", END)

        # escrever na caixa de texto
        caixa_texto.insert("1.0", f"{produto.get()} deletado do Carrinho com sucesso!")
        produto.delete(0, "end")
        preco.delete(0, "end")
        descricao.delete(0, "end")
        categoria.delete(0, "end")

        cursor.close()
        conexao.close()

    ############## janela ##############
    #window = Tk()
    window = Toplevel(janela)

    window.title('Magazine Loja - Carrinho de Compras')
    window.geometry("618x476")
    window.configure(bg="#ffffff")
    canvas = Canvas(
        window,
        bg="#ffffff",
        height=476,
        width=618,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    canvas.place(x=0, y=0)

    background_tela2_img = PhotoImage(master=window, file=f"background_tela2.png")
    background = canvas.create_image(
        309.0, 238.0,
        image=background_tela2_img)

    # painel
    caixa_texto_img = PhotoImage(master=window, file=f"img_textBox0.png")
    caixa_texto_bg = canvas.create_image(
        307.0, 322.0,
        image=caixa_texto_img)

    caixa_texto = Text(
        window,
        bd=0,
        bg="#d9d9d9",
        highlightthickness=0)

    caixa_texto.place(
        x=37, y=258,
        width=540,
        height=126)

    # preço
    preco_img = PhotoImage(master=window, file=f"img_textBox1.png")
    preco_bg = canvas.create_image(
        447.5, 195.0,
        image=preco_img)

    preco = Entry(
        window,
        bd=0,
        bg="#d9d9d9",
        highlightthickness=0)

    preco.place(
        x=318, y=176,
        width=259,
        height=36)

    # descrição
    descricao_img = PhotoImage(master=window, file=f"img_textBox2.png")
    descricao_bg = canvas.create_image(
        447.5, 148.0,
        image=descricao_img)

    descricao = Entry(
        master=window,
        bd=0,
        bg="#d9d9d9",
        highlightthickness=0)

    descricao.place(
        x=318, y=129,
        width=259,
        height=36)

    # categoria
    categoria_img = PhotoImage(master=window, file=f"img_textBox3.png")
    categoria_bg = canvas.create_image(
        447.5, 101.0,
        image=categoria_img)

    categoria = Entry(
        master=window,
        bd=0,
        bg="#d9d9d9",
        highlightthickness=0)

    categoria.place(
        x=318, y=82,
        width=259,
        height=36)

    # produto
    produto_img = PhotoImage(master=window, file=f"img_textBox4.png")
    produto_bg = canvas.create_image(
        447.5, 54.0,
        image=produto_img)

    produto = Entry(
        master=window,
        bd=0,
        bg="#d9d9d9",
        highlightthickness=0)

    produto.place(
        x=318, y=35,
        width=259,
        height=36)

    # deletar
    #deletar = PhotoImage(master=window, file=f"deletar.png")
    deletar = Button(
        master=window,
        text='Deletar',
        command=deletar_produtos_carrinho)

    deletar.place(
        x=454, y=402,
        width=123,
        height=32)

    # listar_carrinho
    #listarcarrinho = PhotoImage(master=window, file=f"listarcarrinho.png")
    listarcarrinho = Button(
        master=window,
        text='Listar Carrinho',
        command=listar_carrinho)

    listarcarrinho.place(
        x=310, y=402,
        width=138,
        height=32)

    # listar_produtos_loja
    #listarprodutos = PhotoImage(master=window, file=f"listarprodutos.png")
    listarprodutos = Button(
        master=window,
        text='Listar Produtos',
        command=listar_produtos_loja)

    listarprodutos.place(
        x=166, y=402,
        width=138,
        height=32)

    # salvar_produto_carrinho
    #salvar = PhotoImage(master=window, file=f"salvar.png")
    salvar = Button(
        master=window,
        text='Salvar',
        command=salvar_produto_carrinho)

    salvar.place(
        x=37, y=402,
        width=123,
        height=32)

    window.resizable(False, False)
    window.mainloop()

# mainloop, runs infinitely
janela.resizable(False, False)
janela.mainloop()