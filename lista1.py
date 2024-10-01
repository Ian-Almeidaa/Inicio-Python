def q1():
    name = input('insira o seu nome:')
    print(f'ola {name} esta lista foi feita pelo Ian')

########

def q2():
    print('30 x 27 =',30*27)

########

def q3():
    print('a media dos valores 5, 8 e 12 e',(5+8+12)/3)

########

def q4():
    num1 = int(input('insira um numero:'))
    print(num1)

########

def q5():
    num1 = float(input('insira um numero:'))
    num2 = float(input('insira outro numero:'))
    print(num1, num2)

########

def q6():
    num = int(input('insira um numero:'))
    print(f'antecessor:{num-1} numero inicial:{num} sucessor:{num+1}')

########

def q7():
    name = input('insira o seu nome:')
    address = input('insira o seu endereco:')
    number = input('insira o seu telefone:')
    print(f'o seu cadastro ficou\nNome: {name}\nEndereco: {address}\nTelefone: {number}')

def q8():
    num1 = int(input('insira um numero:'))
    num2 = int(input('insira outro numero:'))
    print(f'a subtracao ({num1} - {num2}) e igual a {num1-num2}')

def q9():
    num = int(input('insira um numero:'))
    print(f'1/4 de {num} e {num/4}')

def q10():
    num1 = int(input('insira um numero:'))
    num2 = int(input('insira outro numero:'))
    num3 = int(input('insira outro numero:'))
    print(f'a media aritmetica dos valores {num1, num2, num3} e de {(num1+num2+num3)/3}')

def q11():
    num1 = float(input('insira um numero:'))
    num2 = float(input('insira outro numero:'))
    print(f'o resultado das 4 operacoes basicas sao\nSoma ({num1} + {num2}) = {num1+num2}\nSubtracao ({num1} - {num2}) = {num1-num2}\nMultiplicacao ({num1} x {num2}) = {num1*num2}\nDivisao ({num1} ÷ {num2}) = {num1/num2}')

def q12():
    num = float(input('insita um numero:'))
    print(f'o quadrado do numero {num} e de {num**2}')

def q13():
    saldo = float(input('digite o saldo atual:'))
    print(f'o saldo apos a aplicacao e de {saldo+(saldo*2)/100}')

def q14():
    base = float(input('insira o valor da base do triangulo: '))
    high = float(input('insira o valor da altura do triangulo: '))
    print(f'o perimetro do triangulo e de {base+high} e a sua area e de {(base*high)/2}')

def q15():
    product = float(input('insira o valor do produto: '))
    discount = int(input('insira o desconto desejado (%): '))
    print(f'o valor original e de {product} e o valor apos o desconto e de {product - (product*(discount/100))}')

def q16():
    salary = float(input('insira o salario atual: '))
    adjustment = int(input('insira o novo reajuste (%): '))
    print(f'apos o reajuste o salario saiu de R${salary} para R${salary + (salary*(adjustment/100))}')

def q17():
    celcius = float(input('insira a temperatura atual: '))
    print(f'o valor em Fahrenheit e de {(9*celcius + 160) /5}')

def q18():
    