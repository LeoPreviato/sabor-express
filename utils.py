import os

def voltar_menu_principal():
    input("\nDigite uma tecla para voltar ao menu principal ")
    from main import main
    main()

def exibir_subtitulo(texto):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=" * 30)
    print(texto.center(30))
    print("=" * 30)
    print()
