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
    yearNow = int(input('Digite o ano atual: '))
    yearBorn = int(input('Digite o seu ano de nascimento: '))
    if(yearNow > yearBorn):
        print(f'a sua idade e de {yearNow-yearBorn} anos')
    else:
        print(f'ano de nascimento invalido')

def q10():
    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite outro número: '))
    num3 = int(input('Digite mais um número: ')) 
    numero = [num1, num2, num3]
    numero.sort()
    print(f'{numero}')

def q11():
    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite outro número: '))
    num3 = int(input('Digite mais um número: '))
    if(num1>num2 and num1>num3):
        print(f'O maior número é {num1}')
    elif(num2>num1 and num2>num3):
        print(f'O maior número é {num2}')
    elif(num3>num1 and num3>num2):
        print(f'O maior número é {num3}')
    else:
        print(f'Os maiores números são iguais')

def q12():
    age = int(input('Digite a sua idade: '))
    if age < 17:
        print('você é menor de idade')
    elif age < 65:
        print('você já é de maior, mas ainda não é idoso')
    else:
        print('você é idoso')

def q13():
    