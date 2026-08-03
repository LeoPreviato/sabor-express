from utils import *
from database import *

def cadastrar_novo_restaurante():
    exibir_subtitulo("Cadastro de novos Restaurantes")
    
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
    
    print(f"\n[green]O restaurante '{nome_do_restaurante}' foi cadastrado com sucesso![/green]")
    voltar_menu_principal()
    
def listar_restaurantes():
    exibir_subtitulo("Listando Restaurantes")
    
    conexao = conectar()
    if conexao is None:
        return
    cursor = conexao.cursor()
    cursor.execute("SELECT nome, categoria, ativo FROM restaurantes")
    resultado = cursor.fetchall()
    
    tabela = Table(width=60)
    
    tabela.add_column("Nome")
    tabela.add_column("Categoria")
    tabela.add_column("Status")
    
    for linha in resultado:
        nome, categoria, ativo = linha
        status = "[green]Ativado[/green]" if ativo else "[red]Desativado[/red]"
        tabela.add_row(nome, categoria, status)
        
    console.print(tabela)
    
    cursor.close()
    conexao.close()
    voltar_menu_principal()
    
def alternar_estado_restaurante():
    exibir_subtitulo("Alternando estado do Restaurante")
    nome_restaurante = input("Digite o nome do restaurante que deseja alternar o estado: ")
    
    conexao = conectar()
    if conexao is None:
        return
    cursor = conexao.cursor()
    
    cursor.execute("SELECT nome FROM restaurantes WHERE nome = %s", (nome_restaurante,))
    resultado = cursor.fetchone()
    
    if resultado is None:
        print(f"\nO restaurante '{nome_restaurante}' não foi encontrado")
    else:
        cursor.execute("UPDATE restaurantes SET ativo = NOT ativo WHERE nome = %s", (nome_restaurante,))
        conexao.commit()
        
        cursor.execute("SELECT ativo FROM restaurantes WHERE nome = %s", (nome_restaurante, ))
        ativo_atualizado = cursor.fetchone()[0]
        
        mensagem = (
            f"O restaurante '{nome_restaurante}' foi [green]ativado[/] com sucesso"
            if ativo_atualizado
            else f"O restaurante '{nome_restaurante}' foi [red]desativado[/] com sucesso"
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
        print(f"O restaurante '{nome_restaurante}' [red]não foi encontrado[/]")
    else:
        while True:
            confirmacao = input(
                f"Quer continuar a exclusão do restaurante '{nome_restaurante}'? (s/n): "
                ).lower().strip()
            if confirmacao == 's':
                cursor.execute("DELETE FROM restaurantes WHERE nome = %s", (nome_restaurante,))
                conexao.commit()
                print(f"\nO restaurante '{nome_restaurante}' foi [green]excluido[/] com sucesso.")
                break
            elif confirmacao == 'n':
                print(f"\nA exclusão do restaurante '{nome_restaurante}' foi [red]cancelada[/].")
                break
            else:
                print("\n[red]ERRO[/]: Digite (s/n)")
                continue
    
    cursor.close()
    conexao.close()
    voltar_menu_principal()