from utils import *
from database import *

def cadastrar_novo_restaurante():
    exibir_subtitulo("Cadastro de novos restaurantes")
    
    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    categoria = input(f"Digite o nome da categoria do restaurante {nome_do_restaurante}: ")
    
    conexao = conectar()
    if conexao is None:
        return
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO restaurantes (nome, categoria, ativo) VALUES (%s, %s, %s)",
        (nome_do_restaurante, categoria, False)
    )
    conexao.commit()
    cursor.close()
    conexao.close()
    
    print(f"\nO restaurante '{nome_do_restaurante}' foi cadastrado com sucesso!")
    voltar_menu_principal()
    
def listar_restaurantes():
    exibir_subtitulo("Listando restaurantes")
    
    conexao = conectar()
    if conexao is None:
        return
    cursor = conexao.cursor()
    cursor.execute("SELECT nome, categoria, ativo FROM restaurantes")
    resultado = cursor.fetchall()
    
    print(f"{'Nome do Restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status")
    print("-" * 58)
    for linha in resultado:
        nome, categoria, ativo = linha
        status_restaurante = "Ativado" if ativo else "Desativado"
        print(f"- {nome} | {categoria} | {status_restaurante}")
    
    cursor.close()
    conexao.close()
    voltar_menu_principal()
    
def alternar_estado_restaurante():
    exibir_subtitulo("Alternando estado do restaurante")
    nome_restaurante = input("Digite o nome do restaurante que deseja alternar o estado: ")
    
    conexao = conectar()
    if conexao is None:
        return
    cursor = conexao.cursor()
    
    cursor.execute("SELECT nome FROM restaurantes WHERE nome = %s", (nome_restaurante,))
    resultado = cursor.fetchone()
    
    if resultado is None:
        print(f"O restaurante '{nome_restaurante}' não foi encontrado")
    else:
        cursor.execute("UPDATE restaurantes SET ativo = NOT ativo WHERE nome = %s", (nome_restaurante,))
        conexao.commit()
        
        cursor.execute("SELECT ativo FROM restaurantes WHERE nome = %s", (nome_restaurante, ))
        ativo_atualizado = cursor.fetchone()[0]
        
        mensagem = (
            f"O restaurante '{nome_restaurante}' foi ativado com sucesso"
            if ativo_atualizado
            else f"O restaurante '{nome_restaurante}' foi desativado com sucesso"
        )
        print(mensagem)
    
    cursor.close()
    conexao.close()
    voltar_menu_principal()
    
def excluir_restaurante():
    exibir_subtitulo("Excluir Restaurante")
    nome_restaurante = input("Digite o nome do restaurante que deseja excluir: ")
    
    conexao = conectar()
    if conexao is None:
        return
    cursor = conexao.cursor()
    
    cursor.execute("SELECT nome FROM restaurantes WHERE nome = %s", (nome_restaurante,))
    resultado = cursor.fetchone()
    
    if resultado is None:
        print(f"O restaurante '{nome_restaurante}' não foi encontrado")
    else:
        while True:
            confirmacao = input(
                f"Quer continuar a exclusão do restaurante '{nome_restaurante}'? (s/n): "
                ).lower().strip()
            if confirmacao == 's':
                cursor.execute("DELETE FROM restaurantes WHERE nome = %s", (nome_restaurante,))
                conexao.commit()
                print(f"\nO restaurante '{nome_restaurante}' foi excluido com sucesso.")
                break
            elif confirmacao == 'n':
                print(f"\nA exclusão do restaurante '{nome_restaurante}' foi cancelada.")
                break
            else:
                print("\nERRO: Digite (s/n)")
                continue
    
    cursor.close()
    conexao.close()
    voltar_menu_principal()