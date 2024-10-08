def q1():
    num1 = int(input('digite um número: '))
    num2 = int(input('digite outro número: '))
    if(num1+num2 > 10):
        print(f'a soma dos valores é de {num1+num2}')

def q2():
    num1 = int(input('digite um número: '))
    num2 = int(input('digite outro número: '))
    if(num1+num2 > 20):
        print(f'{num1+num2+8}')
    else:
        print(f'{(num1+num2)-5}')

def q3():
    num1 = int(input('insira um valor: '))
    if(num1 % 3 == 0):
        print(f'O número {num1} é multiplo de 3')
    else:
        print(f'O número {num1} não é multiplo de 3')

def q4():
    num1 = int(input('insira um valor: '))
    if(num1%5 == 0):
        print(f'O número {num1} é divisível por 5')
    else:
        print(f'O número {num1} não é divisível por 5')

def q5():
    num1 = int(input('insira um valor: '))
    if(num1 % 3 == 0 and num1 % 7 == 0):
        print(f'O número {num1} é divisível por 3 e por 7')
    else:
        print(f'O número {num1} não é divisível por 3 e por 7')
 
def q6():
    salario = round(int(input('digite o seu salário: ')),2)
    prestacao = round(int(input('digite a prestação desejada: ')),2)
    if(prestacao > (salario/10)*3):
        print(f'o valor de (R${prestacao}) excede o limite (R${(salario/10)*3}), prestação negada')
    else:
        print(f'prestação no valor de (R${prestacao}) aceita, aproveite o dinheiro')

def q7():
    num = float(input('insira um valor: '))
    if(num >= 20 and num <=50):
        print('O valor está na faixa correta')
    else:
        print('O valor está na faixa incorreta')

def q8():
    num = int(input('insira um valor: '))
    if(num > 20):
        print(f'O valor {num} é maior que 20')
    elif(num == 20):
        print(f'O valor é igual a 20')
    else:
        print(f'O valor {num} é menor do que 20')

def q9():
    