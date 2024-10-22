def q1():
    for i in range(1,101,1):
        print(f'{i}°')

def q2():
    for i in range (100,1,-1):
        if i % 2 == 0:
            print(f'{i} é par')

def q3():
    for i in range (500,1,-1):
        if i % 5 == 0:
            print(f'{i} é múltiplo de 5')

def q4():
    for i in range (1,21,1):
        nome = input('Digite o seu nome: ')
        idade = int(input("Digite a sua idade: "))
        sexo = input('Digite o seu sexo (F/M): ')[0].upper()
        
        if sexo == 'M' and idade > 21:
            print(f'Olá {nome}')

def q5():
    num1 = int(input('Digite o 1° valor: '))
    num2 = int(input('Digite o 2° valor: '))
    mult = 0
    for _ in range(num2):
        mult += num1

    print(f'O resultado da multiplicação é {mult}')

def q6():
    i = 1
    fibonacci = 1
    soma = 0
    while i < 20:
        print(fibonacci)
        fibonacci = fibonacci + soma
        soma = fibonacci - soma
        i+=1

def q7():
    for _ in range (3):
        aluno = input('Digite o nome do aluno: ').strip()
        nota1 = round(float(input('Digite a sua 1° nota: ')),2)
        nota2 = round(float(input('Digite a sua 2° nota: ')),2)
        media = (nota1 + nota2) /2
        mediAll += media
        

questao = int(input('Questão a ser executada: '))
eval(f'q{questao}()')