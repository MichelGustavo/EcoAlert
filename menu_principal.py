from tela_denuncia import tela_denuncia
from tela_acompanhar_denuncia import tela_acompanhar_denuncia
from dicas_e_infor import dicas_e_infor


def menu_principal():
    while True:
        print('-'*40)
        print('Selecione sua ação:')
        print('1 - Realizar denuncia')
        print('2 - Acompanhar denuncia')
        print('3 - Informações e dicas')
        print('4 - Sobre nós')
        print('5 - Sair')
        acao = input('> ')

        match acao:
            case "1":
                tela_denuncia()
            case "2":
                tela_acompanhar_denuncia()
            case "3":
                dicas_e_infor()
            case "4":
                print('Somos alunos querendo férias ;(')
            case "5":
                break

            case _:
                print("Opção inválida")








if __name__=="__main__":
    menu_principal()