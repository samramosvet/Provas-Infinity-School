# Provas-Infinity-School

# [PTBD-A11] - Criar uma aplicação em python para armazenar informações de um usuário da aplicação, que deve ter nome, email, senha e data de criação daquele usuário.
# Este usuário deve ser armazenado no banco. Crie funcionalidades para um adm poder editar os dados do usuário, remover e listar todos usuários existentes.
#
# A PROVA SÓ SERA CORRIGIDA ATRAVEZ DO LINK DO GITHUB COM A RESOLUÇÃO DA QUESTÃO!

import pymysql.cursors
from datetime import datetime

class Clientes:
    def __init__(self):
        self.conexao = pymysql.connect(host='localhost',
                                       user='root',
                                       password='',
                                       database='clientes',
                                       port=3308,
                                       cursorclass=pymysql.cursors.DictCursor)

    def listarClientes(self):
        with self.conexao.cursor() as cursor:
            sql = "SELECT * FROM usuarios"
            cursor.execute(sql)
            resultado = cursor.fetchall()

            for usuario in resultado:
                print('Código: ', usuario["cod_user"])
                print('Nome: ', usuario["nome_user"])
                print('E-mail: ', usuario["email_user"])
                print('Senha: ', usuario["senha_user"])
                print('Data ', usuario["data_user"])
                print('\n')

    def listarClientes2(self):
        with self.conexao.cursor() as cursor:
            sql = "SELECT * FROM usuarios WHERE cod_user > 1"
            cursor.execute(sql)
            resultado = cursor.fetchall()

            for usuario in resultado:
                print('Código: ', usuario["cod_user"])
                print('Nome: ', usuario["nome_user"])
                print('E-mail: ', usuario["email_user"])
                print('Senha: ********')
                print('Data ', usuario["data_user"])
                print('\n')

    def inserirClientes(self, usuario):
        with self.conexao.cursor() as cursor:
            sql = "INSERT INTO usuarios (nome_user, email_user, senha_user, data_user) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (usuario.nome_user, usuario.email_user, usuario.senha_user, usuario.data_user))
            self.conexao.commit()

    def atualizarCLientes(self, usuario):
        with self.conexao.cursor() as cursor:
            sql = "UPDATE usuarios SET nome_user = %s, email_user = %s, senha_user = %s WHERE cod_user = %s"
            cursor.execute(sql, (usuario.nome_user, usuario.email_user, usuario.senha_user, usuario.data_user))

            self.conexao.commit()

    def excluirClientes(self, nome_user):
        with self.conexao.cursor() as cursor:
            sql = "DELETE FROM usuarios WHERE nome_user = %s"
            cursor.execute(sql, (nome_user,))
            self.conexao.commit()

class Usuario:
    def __init__(self, nome_user, email_user, senha_user, data_user):
        self.nome_user = nome_user
        self.email_user = email_user
        self.senha_user = senha_user
        self.data_user = data_user


clientes = Clientes()
opcao = 0

print('-----------ENTRADA------------')
login = input('Qual o seu login? ')
senha = input('Qual a sua senha? ')

# CRIANDO CONEXÃO COM O BD MYSQL
conexao = pymysql.connect(host='localhost',
                                   user='root',
                                   password='',
                                   database='clientes',
                                   port=3308,
                                   cursorclass=pymysql.cursors.DictCursor)

with conexao.cursor() as cursor:
    sql = "SELECT * FROM usuarios WHERE nome_user = 'root'"
    cursor.execute(sql)
    resultado = cursor.fetchall()

    for usuario in resultado:
        usuario_root = usuario["nome_user"]
        senha_root = usuario["senha_user"]


# VERIFICANDO AS CREDENCIAIS DO USER
# SE FOR O ROOT UMA VERSÃO COMPLETA DO MENU SERÁ APRESENTADA
if login == usuario_root and senha == senha_root:
    while opcao != 4:
        print('-----------MENU------------')
        print('1 - Listar Usuários')
        print('2 - Adicionar Usuário')
        print('3 - Excluir Usuário')
        print('4 - Sair')
        print('---------------------------')
        opcao = int(input('Qual a opção desejada? '))

        if opcao == 1:
            print('\n')
            clientes.listarClientes()

        elif opcao == 2:
            nome_user = input('Qual o nome do usuário? ')
            email_user = input('Qual o e-mail do usuário? ')
            senha_user = input('Qual a senha do usuário? ')
            data_user = str(datetime.now().strftime("%d/%m/%Y"))
            usuario = Usuario(nome_user, email_user, senha_user, data_user)

            clientes.inserirClientes(usuario)

            print(f'Cliente {nome_user} Cadastrado com Sucesso!!!')

        elif opcao == 3:
            nome_user = input('Qual o nome do usuário que deseja excluir? ')
            clientes.excluirClientes(nome_user)
            print(f'Usuário {nome_user} excluído com sucesso!!! ')

        elif opcao == 4:
            print('Desligando....')
            break

# SE NÃO FOR O ROOT UMA VERSÃO RESTRITA DO MENU SERÁ APRESENTADA
else:
    while opcao != 3:
        print('-----------MENU------------')
        print('1 - Listar Usuários')
        print('2 - Adicionar Usuário')
        print('3 - Sair')
        print('---------------------------')
        opcao = int(input('Qual a opção desejada? '))

        if opcao == 1:
            print('\n')
            print('--------USUÁRIOS---------')
            clientes.listarClientes2()

        elif opcao == 2:
            nome_user = input('Qual o nome do usuário? ')
            email_user = input('Qual o e-mail do usuário? ')
            senha_user = input('Qual a senha do usuário? ')
            data_user = str(datetime.now().strftime("%d/%m/%Y"))
            usuario = Usuario(nome_user, email_user, senha_user, data_user)

            clientes.inserirClientes(usuario)

            print(f'Cliente {nome_user} Cadastrado com Sucesso!!!')

        elif opcao == 3:
            print('Desligando....')
            break
