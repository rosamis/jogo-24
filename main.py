import random
from itertools import permutations

# Faz permutação 3 a 3 de uma lista
def permutacao_lista(cartas):
    return list(permutations(cartas, 3))

# Aleatoriza os valores de cada carta
def aleatoriza_cartas():
    cartas = []
    i = 0
    while i < 4:
        carta = random.randint(1, 9)
        cartas.append(carta)
        i += 1
    return cartas

def calcula(operacao, a, b):
    if operacao == '+':
        return a + b
    if operacao == '-':
        return a - b
    if operacao == '*':
        return a * b
    if operacao == '/':
        return a / b

# Permuta as operações, faz os calculos e retorna se da 24 ou não
def verifica(cartas):
    permutacao_operadores = permutacao_lista(['+','-','*','/'])

    for p in permutacao_operadores:
        aux = []
        r1 = calcula(p[0],cartas[0],cartas[1])
        r2 = calcula(p[1],cartas[2],cartas[3])
        if(calcula(p[2],r1,r2) == 24):
            return True
    return False

def possibilidades(cartas):
    # Faz todas as permutações de cartas possiveis
    permutacao = permutacao_lista(cartas)  
    # Coloca o último elemento que nao esta na permutação na lista de cartas
    for p in permutacao:
        aux1 = cartas.copy()
        aux2 = cartas.copy()
        
        for e in p:
            aux1.remove(e)
            
        aux2.append(aux1[0])
        
        if(verifica(aux2)):
            return True
    return False
    
def main():
    cartas = aleatoriza_cartas()

    if(possibilidades(cartas)):
        print('Poderá ganhar')
    else:
        print('Não poderá ganhar')

if __name__ == "__main__":
    main()