import os

restaurantes = [{"nome":"Madeiro", "categoria":"Lanches", "ativo":False},
                {"nome":"Pizza Suprema", "categoria":"Italiana", "ativo":True},
                {"nome":"Praça", "categoria":"Japonesa", "ativo":False}]

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
    print("3 - Alternar estado do Restaurante")
    print("4 - Sair do Programa\n")

def finalizar_app():
    exibir_subtitulo("Finalizando o app")

def voltar_menu_principal():
    input("\nDigite uma tecla para voltar ao menu principal ")
    main()

def opcao_invalida():
    print("Opção inválida\n")
    voltar_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=" * 30)
    print(texto.center(30))
    print("=" * 30)
    print()

def cadastrar_novo_restaurante():
    exibir_subtitulo("Cadastro de novos restaurantes")
    
    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    categoria = input(f"Digite o nome da categoria do restaurante {nome_do_restaurante}: ")
    dados_do_restaurante = {"nome":nome_do_restaurante, "categoria":categoria, "ativo":False}
    restaurantes.append(dados_do_restaurante)
    print(f"\nO restaurante '{nome_do_restaurante}' foi cadastrado com sucesso!")
    voltar_menu_principal()

def listar_restaurantes():
    exibir_subtitulo("Listando restaurantes")
    
    print(f"{'Nome do Restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status")
    print("-" * 58)
    for restaurante in restaurantes:
        nomes_restaurantes = restaurante["nome"]
        categoria_restaurante = restaurante["categoria"]
        status_restaurante = "Ativado" if restaurante["ativo"] else "Desativado"
        print(f"- {nomes_restaurantes.ljust(20)} | {categoria_restaurante.ljust(20)} | {status_restaurante}")
    
    voltar_menu_principal()

def alternar_estado_restaurante():
    exibir_subtitulo("Alternando estado do restaurante")
    nome_restaurante = input("Digite o nome do restaurante que deseja alternar o estado: ")
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if nome_restaurante == restaurante["nome"]:
            restaurante_encontrado = True
            restaurante["ativo"] = not restaurante["ativo"]
            mensagem = (
                f"O restaurante {nome_restaurante} foi ativado com sucesso"
                if restaurante["ativo"]
                else f"O restaurante {nome_restaurante} foi desativado com sucesso"
            )
            print(mensagem)

    if not restaurante_encontrado:
        print(f"O restaurante '{nome_restaurante}' não foi encontrado")
    
    voltar_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
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
