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
    name = input('Digite o seu nome: ')
    nota1 = int(input('Digite a primeira nota: '))
    nota2 = int(input('Digite a segunda nota: '))
    if((nota1 + nota2)/2 >= 7):
        print(f'Muito bem {name} você foi aprovado com a média de {(nota1 + nota2)/2}')
    elif ((nota1 + nota2)/2 >= 4):
        print(f'Tome cuidado {name} você está de prova final com a média de {(nota1 + nota2)/2}')
    else:
        print(f'{name}, infelizmente você está reprovado com a média de {(nota1 + nota2)/2}')

def q14():
    salary = round(float(input('Digite o seu salário: ')),2)
    if salary > 2000.0:
        print(f'O desconto do seu salário é de 30% {salary - (salary/10)*7}, o valor final dele é de {salary - (salary/10)*3}')
    elif salary > 1200.0:
        print(f'O desconto do seu salário é de 25% {salary - (salary/10)*7.5}, o valor final dele é de {salary - (salary/10)*2.5}')
    elif salary > 600.0:
        print(f'O desconto do seu salário é de 20% {salary - (salary/10)*8}, o valor final dele é de {salary - (salary/10)*2}')
    else:
        print(f'seu salário está isento de INSS, se mantendo em {salary}')

def q15():
    product = round(float(input('Digite o valor do produto: ')),2)
    if product >= 20.0:
        print(f'Para atingir 45% da margem de lucro, o produto será vendido no valor de {product + (product/10)*4.5}')
    else:
        print(f'Para atingir 30% da margem de lucro, o produto será vendido no valor de {product + (product/10)*3}')

def q16():
    age = int(input('Digite a sua idade: '))
    if age >= 18:
        print('Você competirá na categoria Sênior')
    elif age >= 14:
        print('Você competirá na categoria Juvenil B')
    elif age >= 11:
        print('Você competirá na categoria Juvenil A')
    elif age >= 8:
        print('Você competirá na categoria Infantil B')
    else:
        print('Você competirá na categoria Infantil A')

def q17():
    name = input('Digite o seu nome: ')
    age = int(input('Digite a sua idade: '))
    if age > 65:
        print(f'Olá {name}, por conta da sua idade ({age}) o seu plano seria R$400,00')
    elif age > 59:
        print(f'Olá {name}, por conta da sua idade ({age}) o seu plano seria R$250,00')
    elif age > 45:
        print(f'Olá {name}, por conta da sua idade ({age}) o seu plano seria R$150,00')
    elif age > 29:
        print(f'Olá {name}, por conta da sua idade ({age}) o seu plano seria R$120,00')
    elif age > 10:
        print(f'Olá {name}, por conta da sua idade ({age}) o seu plano seria R$60,00')
    else:
        print(f'Olá {name}, por conta da sua idade ({age}) o seu plano seria R$30,00')

def q18():
    year = int(input('Digite o número do mês desejado: '))
    match year:
        case 1:
            print(f'O mês {year} representa Janeiro')
        case 2:
            print(f'O mês {year} representa Fevereiro')
        case 3:
            print(f'O mês {year} representa Março')
        case 4:
            print(f'O mês {year} representa Abril')
        case 5:
            print(f'O mês {year} representa Maio')
        case 6:
            print(f'O mês {year} representa Junho')
        case 7:
            print(f'O mês {year} representa Julho')
        case 8:
            print(f'O mês {year} representa Agosto')
        case 9:
            print(f'O mês {year} representa Setembro')
        case 10:
            print(f'O mês {year} representa Outubro')
        case 11:
            print(f'O mês {year} representa Novembro')
        case 12:
            print(f'O mês {year} representa Dezembro')
        case _:
            print(f'O mês {year} não é válido')

def q19():
    