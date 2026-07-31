from utils import *

restaurantes = [{"nome":"Madeiro", "categoria":"Lanches", "ativo":False},
                {"nome":"Pizza Suprema", "categoria":"Italiana", "ativo":True},
                {"nome":"Praça", "categoria":"Japonesa", "ativo":False}]

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
    
def excluir_restaurante():
    exibir_subtitulo("Excluir Restaurante")
    nome_restaurante = input("Digite o nome do restaurante que deseja excluir: ")
    restaurante_encontrado = None
    
    for restaurante in restaurantes:
        if nome_restaurante == restaurante["nome"]:
            restaurante_encontrado = restaurante
            break
        
    if restaurante_encontrado:
        while True:
            confirmacao = input(
                f"\nQuer continuar com a exclusão do restaurante '{restaurante_encontrado['nome']}'? (s/n): "
                ).lower().strip()
            if confirmacao == 's':
                restaurantes.remove(restaurante_encontrado)
                print(f"\nO restaurante '{restaurante_encontrado['nome']}' foi excluido com sucesso.")
                break
            elif confirmacao == 'n':
                print(f"\nA exclusão do restaurante '{restaurante_encontrado['nome']}' foi cancelada.")
                break
            else:
                print("\nERRO: Digite (s/n)")
                continue
    else:
        print("Restaurante não encontrado.")
        
    voltar_menu_principal()