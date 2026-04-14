# Exemplos com "and"

# Dados do Sistema
saldo_conta = 1000.0
limite_cartao = 500.0

# Entrada do Usúario
valor_saque = float(input("Quanto sacar? "))

# Decisão Completa
autorizado = (valor_saque <= saldo_conta) and (valor_saque <= limite_cartao)
