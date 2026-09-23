import random # gerar número aleatório

#só permitir nº entre 0 e 100

def nvalid():
    while True:
        numero = int(input("\nInsere um número inteiro: "))

        if numero >= 0 and numero <= 100:
            return numero
    
        else:
            print("O número inserido não é válido")

def jogo1():
    while True:
        tentativas = 0
        cpu = int(random.randrange(0, 100)) #número escolhido pelo computador
        njogador = nvalid()

        if cpu > njogador:
            print("Escolhe um número mais alto.")
        elif cpu < njogador:
            print("Escolhe um número mais baixo.")
        else:
            print (f"Parabéns! Acertaste no número em {tentativas} tentativas")
            return

        tentativas = tentativas + 1

def jogo2():
    
    max = 100
    min = 0
    cpu = (max - min)//2 #divisão inteira

    print("Pensa num número inteiro de 0 a 100.")

    while True:
        opt = int(input(f"O teu número é {cpu}?\n  [1]Sim, acertaste!" \
               "\n  [2]Não, é maior.\n  [3]Não, é menor."))
        
        if opt == 1:
            return
        
        elif opt == 2:
            min = cpu
            cpu = cpu + (max - min)//2

        elif opt == 3:
            max = cpu 
            cpu = cpu - (max - min)//2

        else:
            print("Opção inválida. Tente novamente.")


# ciclo para poder repetir o jogo (tenho que ter while)
while True:

    opt = int(input("Adivinha-tron!\nMenu:" \
    "\n  [1] Adivinha o número (de 0 a 100) que o computador escolhe:" \
    "\n  [2] Escolhe um número (de 0 a 100) para o computador adivinhar:" \
    "\n  [3] Sair do jogo\n"))

    if opt == 1:
        #jogo 1
        jogo1()
    
    elif opt == 2:
        #jogo 2
        jogo2()

    elif opt == 3:
        #sair
        print("Adeus :)")
        break

    else:
        print("A opção introduzida é invalida. Por favor, tente novamente.")






