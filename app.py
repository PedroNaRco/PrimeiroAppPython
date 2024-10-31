import os

restaurantes = [
    {'nome': 'Praça', 'categoria': 'comida br', 'ativo': False},
    {'nome': 'Pizza calabresa', 'categoria': 'italiana', 'ativo': True},
    {'nome': 'Cantina', 'categoria': 'italiano', 'ativo': False}
]


def exibir_nome_programa():
    
    print("Sabor Express\n")

def exibir_opcoes():

    print('1 - Cadastrar restaurante')
    print('2 - Listar restaurante')
    print('3 - Alternar estado do restaurante')
    print('4 - Sair')

def finalize_app():
    exibir_subtitulos('Finalizando APP')
      
def voltar_ao_menu():
    input('\nDigite uma tecla para voltar ao menu.')
    main()
          
      
def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu()
    
def exibir_subtitulos(texto):
    os.system('cls')
    linha = '*' * (len(texto) + 4)
    print(linha)
    print(texto)
    print(linha)
    
    
def cadastrar_restaurante():
    exibir_subtitulos('Cadastro de novos restaurantes')    
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_restaurante}:')
    dados_do_restaurante = {'nome':nome_restaurante,'categoria':categoria,'ativo':False}
    restaurantes.append(dados_do_restaurante)
    restaurantes.append(nome_restaurante)
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu()
    
def listar_restaurantes():
    exibir_subtitulos('Lista restaurantes')
    
    print(f'{'Nome do restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = 'ativado' if restaurante['categoria'] else 'desativado'
        ativo = restaurante['ativo']
        print(f'{nome_restaurante.ljust(20)}:| {categoria.ljust(20)} | {ativo}')
            
    voltar_ao_menu()
    
def alternar_estado_restaurante():
    exibir_subtitulos('Alternando o estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrato = False
    
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrato = True
            restaurante['ativo'] = not restaurante['ativo']
            menssgem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(menssgem)
    if not restaurante_encontrato:
        print('O restaurante não foi encontrato')
        
    
    
    
    voltar_ao_menu()
    
def escolher_opcao():
    
    try:
        opcao_escolhida = int(input('Escolha uma opção: ' ))
        # opcao_escolhida = int(opcao_escolhida)
        
        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()   
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
    
    