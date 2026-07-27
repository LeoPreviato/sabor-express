import os

restaurantes = ["Madeiro", "McDonald's"]

def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░      
""")

def exibir_opcoes():
    print("1 - Cadastrar Restaurante")
    print("2 - Listar Restaurantes")
    print("3 - Ativar/Desativar Restaurante")
    print("4 - Sair do Programa\n")

def finalizar_app():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Finalizando o app\n")
    
def opcao_invalida():
    print("Opção inválida\n")
    input("Digite uma tecla para voltar ao menu principal")
    main()
    
def cadastrar_novo_restaurante():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Cadastro de novos restaurantes\n")
    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    restaurantes.append(nome_do_restaurante)
    print(f"\nO restaurante {nome_do_restaurante} foi cadastrado com sucesso!")
    input("\nDigite uma tecla para voltar para o menu principal: ")
    main()
    
def listar_restaurantes():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Listando restaurantes\n")
    
    for restaurante in restaurantes:
        print(f"- {restaurante}")
    
    input("\nDigite uma tecla para voltar para o menu principal: ")
    main()

def escolher_opcao():
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print("Ativar/Desativar restaurante")
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == "__main__":
    main()