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
    for _ in range (15):
        aluno = input('Digite o nome do aluno: ').strip()
        erro = True
        while erro == True:
            try:
                nota1 = round(float(input('Digite a sua 1° nota: ')),2)
            except ValueError:
                print('O valor informado não é um número inteiro!')
                erro = True
            except: # captura qualquer erro
                print('Ocorreu um erro desconhecido! Tente novamente!')
                erro = True
            else:
                erro = False
        erro = True
        while erro == True:
            try:
                nota2 = round(float(input('Digite a sua 2° nota: ')),2)
            except ValueError:
                print('O valor informado não é um número inteiro!')
                erro = True
            except: # captura qualquer erro
                print('Ocorreu um erro desconhecido! Tente novamente!')
                erro = True
            else:
                erro = False 
        media = (nota1 + nota2) /2
        mediAll += media

    print(f'A média final da turma é de {mediAll/15}')
        
def q8():
    for _ in range (5):
        nome = input('Digite o seu nome: ')
        erro = True
        while erro == True:
            salario = 0.0
            try:
                salario = round(float(input('Número 1: ')),2)
            except ValueError: # só é executado para o tipo de erro ValueError
                print('O valor informado não é um número inteiro!')
                erro = True
            except: # captura qualquer erro
                print('Ocorreu um erro desconhecido! Tente novamente!')
                erro = True
            else:
                erro = False

        if salario < 1300.00:
            print (f'Olá {nome}, você está isento de IRRF')
        elif salario < 2300.00:
            print(f'Olá {nome}, você terá um desconto de 10% de desconto do IRRF, seu salário ficará {salario - (salario/10)}')
        else:
            print(f'Olá {nome}, você terá um desconto de 15% de desconto do IRRF, seu salário ficará {salario - (salario/10)*1.5}')

def q9():
    print()

def q10():
    print()

def q11():
    num = 1
    cont = 0
    while num != 0:
        erro = True
        while erro == True:
            num = 1.0
            try:
                num = round(float(input('Número: ')),2)
            except ValueError: # só é executado para o tipo de erro ValueError
                print('O valor informado não é um número inteiro!')
                erro = True
            except: # captura qualquer erro
                print('Ocorreu um erro desconhecido! Tente novamente!')
                erro = True
            else:
                erro = False
        if num >= 100.0 and num < 200.1:
            cont += 1
    print(f'O total de números entre 100 e 200 foi de {cont}')

def q12():
    ctA = 5000000
    ctB = 7000000
    cont = 0
    while ctA <= ctB:
        ctA+=(5000000/100)*3
        ctB+=(7000000/100)*2
        cont+=1
    print(f'O tempo necessário foi de {cont} anos')
    
def q13():
    print()

def q14():
    num = 0
    while num != 1:
        factor = 1
        erro = True
        while erro == True:
            num = 1.0
            try:
                num = round(int(input('Número: ')),2)
            except ValueError: # só é executado para o tipo de erro ValueError
                print('O valor informado não é um número inteiro!')
                erro = True
            except: # captura qualquer erro
                print('Ocorreu um erro desconhecido! Tente novamente!')
                erro = True
            else:
                erro = False
        for x in range (num, 1, -1):
            factor *= x
        print(factor)

def q15():
    
questao = int(input('Questão a ser executada: '))
eval(f'q{questao}()')