# Match Case e Try/Except

# Estruturas de decisão

# Programar significa dar instruções para que o computador tome ações. Em muitos momentos, o programa precisa escolher caminhos diferentes.

# Match Case

    # É uma estrutura de decisão criada para facilitar comparações com múltiplas possibilidades.

        # 1- if / elif / else: Comparaçôes encadeadas, verbosas para muitas condições.
        # 2- Match Case: Comparações organizadas, limpas e fáceis de manter.
        # 3- Código mais legível: Menus, opções e decisões ficam muito mais claros.

opcao = int(input("Escolha uma opção (1-3): "))

match opcao:
    case 1:
        print("Você escolheu a opção 1.")
    case 2:
        print("Você escolheu a opção 2.")
    case 3:
        print("Você escolheu a opção 3.")
    case _:
        print("Opção inválida.")
