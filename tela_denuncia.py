import pickle
import os

def criar_arquivo_de_denuncias_se_nao_existir():
    arquivo_existe = os.path.isfile('denuncias.pickle')
    if not arquivo_existe:
        with open('denuncias.pickle', 'wb') as documento:
            pickle.dump([], documento)


def backup_dados_arquivo():
    with open('denuncias.pickle', 'rb') as documento:
        dados = pickle.load(documento)
        return dados


def salvar_dados_no_arquivo(dados):
    dados_backup = list(backup_dados_arquivo())
    dados_backup.append(dados)

    with open('denuncias.pickle', 'wb') as documento:        
        pickle.dump(dados_backup, documento)
        print('denuncia realizada com sucesso')


def tipo_de_poluicao():
    while True:
        print('Insira o tipo de poluição: ')
        print('1 - Despejo ilegal de resíduos')
        print('2 - Contaminação química')
        print('3 - Esgoto não tratado')
        print('4 - Outro')
        tipo_poluicao = input('> ')

        match tipo_poluicao:
            case "1":
                tipo_poluicao = "Despejo ilegal de resíduos"
                return tipo_poluicao
            case "2":
                tipo_poluicao = "Contaminação química"
                return tipo_poluicao
            case "3":
                tipo_poluicao = "Esgoto não tratado"
                return tipo_poluicao
            case "4":
                tipo_poluicao = input("Insira a poluição: ")
                return tipo_poluicao
            case _:
                print('Opção inválida')


def descricao_da_poluicao():
    print('Descreva o que você observou. Inclua detalhes como cor, odor, aparência, etc:')
    descricao_poluicao = input('> ')
    return descricao_poluicao


def localizacao_da_ocorrencia():
    print("Informe o local exato da poluição. Você pode usar o GPS ou inserir o endereço manualmente")
    localizacao_ocorrencia = input('> ')
    return localizacao_ocorrencia


def data_e_hora_da_ocorrencia():
    print("Informe quando você notou a poluição.")
    data_e_hora = input("> ")
    return data_e_hora


def informacoes_adicionais():
    print('Se houver alguma informação adicional que você gostaria de adicionar, por favor, faça-o aqui')
    info_adicional = input("> ")
    return info_adicional


def tela_denuncia():

    criar_arquivo_de_denuncias_se_nao_existir()
    
    vetor_denuncia = [str]*5

    print('Por favor, preencha os campos abaixo para relatar um caso de poluição de água. Sua identidade será mantida anônima')

    topicos =  [tipo_de_poluicao(), descricao_da_poluicao(), localizacao_da_ocorrencia(), data_e_hora_da_ocorrencia(), informacoes_adicionais()]

    for c in range(len(vetor_denuncia)):
        vetor_denuncia[c] = topicos[c]
    
    salvar_dados_no_arquivo(vetor_denuncia)

if __name__=="__main__":
    tela_denuncia()