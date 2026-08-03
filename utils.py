import os
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich import print

console = Console()

def voltar_menu_principal():
    input("\nDigite uma tecla para voltar ao menu principal ")
    from main import main
    main()

def exibir_subtitulo(texto):
    os.system('cls' if os.name == 'nt' else 'clear')
    titulo = Text(texto, justify="center")
    console.print(Panel(titulo, width=60))
    print()
