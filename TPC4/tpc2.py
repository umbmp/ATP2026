

import random

def elems():
    executar = True
    while executar:
        elem = int(input("Quantos elemnetos deve ter a lista? (A lista deverá ter 2 ou mais elementos)\n"))
        if elem >= 0:
                executar = False
        else:
             print("O número inserido não é válido")
    return elem



def nvalid():
    executar = True
    while executar:
            
            num = int(input("Que número (de 1 a 100) pretende introduzir?\n"))
            if num >= 1 and num <= 100:
                    executar = False
            else:
                print("O número inserido não é válido")
    return num

def soma(lista):
    soma = 0

    for e in lista:
        soma = soma + e

    return soma


def crescente(lista):
    i = 0
    valor = True
    while i < len(lista)-1 and valor:
        if lista[i] > lista[i + 1]:
            valor = False
            

    return valor


def decrescente(lista):
    i = 0
    valor = True
    while i < len(lista) - 1 and valor:
        if lista[i] < lista[i + 1]:
            valor = False

    return valor

def searchn(lista, elem):
    res= -1
    i = 0
    encontrei = False
    while i < len(lista) and not encontrei:
        if lista[i] == elem:
            res = i
            encontrei = True
    i = i + 1
    return res

op = -1

while op != 0:


    print("Menu:" \
    "[1] Criar Lista" \
    "[2] Ler Lista" \
    "[3] Soma" \
    "[4] Média" \
    "[5] Maior" \
    "[6] Menor" \
    "[7] EstaOrdenada por ordem crescente" \
    "[8] EstaOrdenada por ordem decrescente" \
    "[9] Procura um elemento" \
    "[0] Sair")

    op = int(input("Escolha uma opção:\n"))

    if op == 1:
        lista = []
        elem = elems()
        while elem > 0:
            lista.append(random.randint(1,100))
            elem = elem - 1

    elif op == 2:
        lista = []
        elem = elems()
        
        while elems > 0:
        
            lista.append(nvalid())
            elem = elem - 1

    elif op == 3:
        print(f"A soma dos elementos da lista é {soma(lista)}")

    elif op == 4:
        
        print(f"A média é {soma(lista) / len(lista)}")
        
    elif op == 5:
        maior = lista[0]

        for e in lista:
            if e > maior:
                maior = e

        print(f"O maior número é {maior}")

    elif op == 6:
        menor = lista[0]
        
        for e in lista:
            if e < menor:
                menor = e
        
    elif op == 7:
        result = crescente(lista)
        if result == True:
            print("Sim")
        else:
            print("Não")

    elif op == 8:
        result = decrescente(lista)
        if result == True:
                print("Sim")
        else:
                print("Não")

    elif op == 9:
        print(searchn(lista, elem))

        
    elif op == 0:
        
        print(lista)
        print("Até à próxima")
       

    else:
        print ("Opção não suportada. Insira outro número")