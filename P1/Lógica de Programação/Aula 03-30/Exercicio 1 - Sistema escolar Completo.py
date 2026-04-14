nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
frequencia = int(input("Frequência: "))

media = (nota1 + nota2) / 2

aprovado = (media >= 7.0) and (frequencia >= 75)

print("Média:", media)
print("Aprovado?", aprovado)
