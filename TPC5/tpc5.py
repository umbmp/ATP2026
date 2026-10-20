def inserir_aluno(turma):
    print("Por favor insira os dados do aluno.")
    
    nome = input("Insira o nome do aluno")
    id = input("Insira o id do aluno")
    notas = []
    tpc = float(input("Insira a nota do aluno no TPC"))
    notas.append(tpc)
    proj = float(input("Insira a nota do aluno no projeto"))
    notas.append(proj)
    teste =float(input("Insira a nota do aluno no teste"))
    notas.append(teste)
    aluno = (nome, id, notas)
    turma.apppend(aluno)
    return turma

def listar_alunos(turma):
    for a in turma:
        print(a)
    return

def procurar_id(turma,id):
    
    aluno = None
    for a in turma:
        if a[1] == id:
            aluno = a
    return aluno

def guardarTurma(turma, fnome):
    file = open(fnome,"w") 
    
    for aluno in turma:
        nome, id, notas = aluno
        notaTPC, notaProj, notaTeste = notas
        file.write(f"{nome}#{id}#{notaTPC};{notaProj};{notaTeste}\n")
    file.close()

def carregarTurma(fnome):
    turma = []
    file = open(fnome,"r")
    for line in file:
        nome, id, n = line.split("#")
        partesNotas = n.split(";")
        notaTPC = float(partesNotas[0]) # indice do elemento do txt que quero atribuir à minha variavel
        notaProj = float(partesNotas[1])
        notaTeste = float(partesNotas[2])
        notas = [notaTPC, notaProj, notaTeste]
        aluno = (nome, int(id), notas)
        turma.append(aluno)
    file.close()
    return turma


print ("Menu:\n"
    "- 1: Criar uma turma;\n"
    "- 2: Inserir um aluno na turma;\n"
    "- 3: Listar a turma;\n"
    "- 4: Consultar um aluno por id;\n"
    "- 8: Guardar a turma em ficheiro;\n"
    "- 9: Carregar uma turma dum ficheiro;\n"
    "- 0: Sair da aplicação. \n")

op = int(input("Insira a opção que pretende:"))
turmas = []

while op != 0:

    if op == 1:
        turma= []

    elif op == 2:
        
        turma = inserir_aluno(turma)

    elif op == 3:
        listar_alunos(turma)

    elif op == 4:

        id= int(input("Insiira o id do aluno que pretende procurar"))
        aluno = procurar_id(id)
        if aluno == None:
            print("O id inserido não corresponde a nenhum aluno")
        else:
            print(aluno)

    elif op == 8:
        guardarTurma(turma,"turma.txt")

    elif op == 9:
        turma = carregarTurma("turma.txt")

    else:
        print("Opção inválida tente novamente")
       
print("Até à próxima!")
