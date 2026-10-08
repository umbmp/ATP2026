import random

def nvalid():
    executar = True
    while executar:
        num = int(input("Insira um número inteiro de 1 a 10\n"))
        if num >= 1 and num <= 10:
            executar = False
        else:
             print("O número inserido não é válido")
    return num

def jogo(inicial):
    soma = inicial
    executar = True
    while executar:
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
        executar = False
            
    return
            
     

#menu do jogo

while op != 3:
    print("Olá! Sê bem-vindo à corrida ao 100.\n Menu\n\
   [1] Utilizador joga primeiro.\n   [2] Computador joga primeiro.\n   [3] Sair.")

    op = int(input("Selecione uma opção\n"))

    if op == 1:
        jogo(0)
             
    elif op == 2:
        print("Escolho o número 1.")
        jogo(1)      
         
    elif op == 3:
        print("Até à próxima!")    
        

    else:
        print("Opção não suportada. Tente novamente.")
    