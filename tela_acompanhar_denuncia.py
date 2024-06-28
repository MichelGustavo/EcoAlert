from tela_denuncia import backup_dados_arquivo


def tela_acompanhar_denuncia():
    dados = backup_dados_arquivo()
    if len(dados)>0:    
        print('Lista de denúncias: ')
        for c in range(len(dados)):
            print('-'*40)
            print(f'denuncia {c+1}')
            print(f'Tipo: {dados[c][0]}')
            print(f'Descrição: {dados[c][1]}')
            print(f'Local: {dados[c][2]}')
            print(f'Quando: {dados[c][3]}')
        
    else:
        print('Não existem denuncias ativas')

    print('-'*40)
    input('Pressione enter para voltar \n> ')





if __name__ == "__main__":
    tela_acompanhar_denuncia()