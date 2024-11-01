#Criando a própria biblioteca

def input_int(insert):
    while True:
        try:
            inteiro = int(input(insert))
        except ValueError:
            print('Valor digitado não é inteiro! Digite novamente.')
        except:
            print('Ocorreu um erro!! Tente novamente.')
        else:
            False

def input_float(insert):
    while True:
        try:
            inteiro = float(input(insert))
        except ValueError:
            print('Valor digitado não é inteiro! Digite novamente.')
        except:
            print('Ocorreu um erro!! Tente novamente.')
        else:
            False