import os

restaurantes = [
    'Pizza', 'Sushi', 'Bronkz'
]


def exibir_nome_programa():
    
    print("Sabor Express\n")

def exibir_opcoes():

    print('1 - Cadastrar restaurante')
    print('2 - Listar restaurante')
    print('3 - Ativar restaurante')
    print('4 - Sair')

def finalize_app():
    os.system('cls')
    print('APP encerrado')
      
def opcao_invalida():
    print('Opção inválida!\n')
    input('Digite um opção válida:')
    main()
    
def cadastrar_restaurante():
    os.system('cls')
    print('Cadastro de novos restaurantes\n')
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_restaurante)
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!')
    input('Digite uma tecla para voltar ao menu principal.')
    main()
    
def listar_restaurantes():
    os.system('cls')
    print('Listar restaurantes\n')
    for restaurante in restaurantes:
        print(f'.{restaurante}')
            
    input('Digite uma tecla para voltar ao menu principal.')
    
    
    
def escolher_opcao():
    
    try:
        opcao_escolhida = int(input('Escolha uma opção: ' ))
        # opcao_escolhida = int(opcao_escolhida)
        
        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print('Atiivar Restaurante')   
        elif opcao_escolhida == 4:
            finalize_app()
        else:
            opcao_invalida()     
    except:
        opcao_invalida()
    
def main():
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
    
    