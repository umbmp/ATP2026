import random

def nvalid():
    while True:
        num = int(input("Insira um número inteiro de 1 a 10\n"))
        if num >= 1 and num <= 10:
                return num
        
        else:
             print("O número inserido não é válido")

def jogo(inicial = 0):
    soma = inicial
    while True:
        num = nvalid()
        soma = soma + num
        print(f"O valor atual é {soma}")
        if soma < 90:
            cpu = 11 - num 
            soma = soma + cpu 
            print(f"Escolho o número {cpu}. O valor atual é {soma}")
        else:
            cpu = 100 - soma
            if cpu > 0:
                print(f"Escolho o número {cpu}. Cheguei ao 100!")
            elif cpu == 0:
                print("Chegaste aos 100. Parabéns!!")
            else:
                print("Ups! Ultrapassaste os 100.")
            return
     

#menu do jogo

while True:
    print("Olá! Sê bem-vindo à corrida ao 100.\n Menu\n\
   [1] Utilizador joga primeiro.\n   [2] Computador joga primeiro.\n   [3] Sair.")

    op = int(input("Selecione uma opção\n"))

    if op == 1:
        jogo()
             
    elif op == 2:
        print("Escolho o número 1.")
        jogo(1)      
         
    elif op == 3:
        print("Até à próxima!")
        break

    else:
        print("Opção não suportada. Tente novamente.")
    