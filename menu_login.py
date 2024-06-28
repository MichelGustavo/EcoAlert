import pickle
import os


def carregar_elementos():
    with open('usuarios.pickle', 'rb') as documento:
        lista_usuarios = pickle.load(documento)
        return lista_usuarios


def login():
    escolha = input("Login por email ou por telefone: ")
    senha = input('Senha: ')
    lista = carregar_elementos()
    for i in lista:
        if (i[1] == escolha or i[3] == escolha) and i[2] == senha:
            print('> Entrada aceita')
            return True
    else:
        print("Usuário ou senha inválidos")
        return False
    

def criar_arquivo():
    if not os.path.isfile('./usuarios.pickle'):
        with open('usuarios.pickle', 'wb') as documento:
            pickle.dump([], documento)


def adicionar_elemento():
    nome = input('Insira seu nome: ')
    email = input('Insira seu email: ')
    senha = input('Insira sua senha: ')
    telefone = input('Insira seu n° de telefone: ')
    
    lista_usuarios = salvar_e_exibir_elementos()
    lista_usuarios.append([nome, email, senha, telefone])

    with open('usuarios.pickle', 'wb') as documento:
        pickle.dump(lista_usuarios, documento)
   

def salvar_e_exibir_elementos():
    with open('usuarios.pickle', 'rb') as documento:
        lista_usuarios = pickle.load(documento)
    return lista_usuarios


def menu_login():
    criar_arquivo()
    while True:

        print('Escolha a ação: ')
        print('1. Cadastro')
        print('2. Login')
        print('3. Fechar Programa')

        acao = input('> ')

        match acao:
            case '1':
                adicionar_elemento()
            case '2':
                if login(): 
                    break
            case '3':
                raise
            case _:
                print("Opção inválida")


if __name__ == "__main__":
    menu_login()