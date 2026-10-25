import matplotlib.pyplot as plt

def medias(tabMeteo):
    res = []
    for e in tabMeteo:
        #data, tmin, tmax, *_ = e , para n ter que usar tantas linhas
        d = e[0]
        max = e[2]
        min = e[1]
        med = (max + min)/2
        res.apppend((d,med)) # atenção usar append 
    return res


def guardaTabMeteo(t, fnome):
    file = open(fnome,"w")
    for data, tmin, tmax, prec in t:
        
        ano, mes, dia = data
        file.write(f"{ano}-{mes}-{dia}|{tmin}|{tmax}|{prec}\n")

    file.close()
    return

def carregaTabMeteo(fnome):
    res = []
    file = open(fnome, "r")
    
    for line in file:
        d, tmin, tmax, prec = line.split("|")
        pdata = d.split("-")
        ano = int(pdata[0])
        mes = int(pdata[1])
        dia = int(pdata[2]) 
        res.append (((ano,mes,dia), float(tmin), float(tmax), float(prec)))
    file.close()
    return res

def minMin(tabMeteo):
    min = tabMeteo[0,1]
    for dia in tabMeteo:
            tmin = dia[1]
            if tmin < min:
                    min = tmin
    return min

def amplTerm(tabMeteo):
    res = []
    for data, tmin, tmax,*_ in tabMeteo:
        amplitude = tmax - tmin
        res.append((data,amplitude))
    return res 

def maxChuva(tabMeteo):
    precmax = tabMeteo[0,3]
    datamax = tabMeteo[0,0]
    for data, *_, *_, prec in tabMeteo:
        if prec > precmax:
            precmax = prec
            datamax = data
    return (datamax, precmax)

def diasChuvosos(tabMeteo, p):
   res = []
   for data, *_, *_, prec in tabMeteo:
           if prec > p:
                 res.append((data,prec))              
   return res

def maxPeriodoCalor(tabMeteo, p):
    i = 0
    imax  = 0
    for *_ , *_ , *_ , prec in tabMeteo:
        if prec < p:
            i = i + 1
        else:
            i = 0
        if i > imax:
            imax = i
    return imax

def grafTabMeteo(t):
    y_min = [tmin for _, tmin, _, _ in t]
    y_max = [tmax for _, _, tmax, _ in t]
    y_plu = [plu for _, _, _, plu in t]
    x = [f"{data[0]}-{data[1]}-{data[2]}" for data, *_ in t]
    plt.plot(x, y_min, color = "green", marker="o", label="Temperatura mínima")
    plt.plot(x, y_max, color = "red", marker="o", label="Temperatura máxima")
    plt.plot(x, y_plu, color = "blue", marker="o", label="Pluviosidade")
    plt.plot
    plt.legend()
    plt.show()
    return


print ("Print seja bem-vindo ao analisador de dados!")
print ("""Menu:
1) Calcular Temperatura Média Diária
2) Guardar Tabela Meteorológica num Ficheiro
3) Carregar Tabela Meteorológica de um Ficheiro
4) Calcular a Temperatura Mínima
5) Calcular Amplitude Térmica
6) Determinar o Dia em que a Precipitação foi Máxima
7) Determinar Dias em que a Precipitação foi Superior a um Limite
8) Determinar o Maior Número Consecutivo de Dias com Precipitação Abaixo des um Limite 
9) Desenhar Gráficos da Temperatura Máxima, Temperatura Míninima e Pluviosidade
0) Sair do Programa""")

op = int(input("Escolha uma opção:\n"))

while op != 0:
     
    if op == 1:
        medias()

    elif op == 2:
        ficheiro = input("Insira como quer guardar o ficheiro.")
        guardaTabMeteo(t,ficheiro)

    elif op == 3:
        ficheiro = input("Insira o ficheiro a carregar.")
        carregaTabMeteo(ficheiro)

    elif op == 4:
        minMin()

    elif op == 5:
        amplTerm()

    elif op == 6:
        maxChuva()

    elif op == 7:
        lim =int(input("Insira o Limite que pretende usar"))
        diasChuvosos(, lim)

    elif op == 8:
        lim =int(input("Insira o Limite que pretende usar"))
        maxPeriodoCalor(, lim)

    elif op == 9:
        grafTabMeteo()

    else:
         print("Opção inválida. Tente novamente.")
    

print("Até à próxima!")
