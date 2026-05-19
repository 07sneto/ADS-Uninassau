import random

# Sorteia um número entre 0 e 100
numRandom = random.randint(0, 100)

# Parte do Usúario

numUser = int(input("Digite um número entre 0 e 100: "))
numTent = 1
while numUser != numRandom:
    if numUser < numRandom:
        print("O número sorteado é maior do que o que você digitou.")
    else:
        print("O número sorteado é menor do que o que você digitou.")
    numUser = int(input("Digite um número entre 0 e 100: "))
    numTent = numTent + 1

print("Parabéns! Você acertou o número sorteado:", numRandom)
print("Você tentou", numTent, "vezes.")