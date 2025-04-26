def calculadora():
    print('°<[}- - Calculadora - -{]>°')

    while True:
        try:
            v1 = float(input('Insira o primeiro valor: '))
            v2 = float(input('Insira o segundo valor: '))
            break
        except ValueError:
            print('Insira valores válidos!\nReiniciando . . .')
        print(f'Valores escolhidos: {v1} e {v2}')

    while True:
        operador = (input('Insira a operação desejada: '))
        match operador:
          case '+':
            print(f'A soma de {v1} + {v2} = {v1+v2}')
            break
          case '-':
            print(f'A subtração de {v1} - {v2} = {v1-v2}')
            break
          case '*':
            print(f'A multiplicação de {v1} x {v2} = {v1*v2}')
            break
          case '/':
            if v1 == 0 or v2 == 0:
               print('Resultado inválido por ser divisão por 0!')
               break
            else:
                print(f'A divisão de {v1} / {v2} = {v1/v2}')
                break
          case _:
            print(f'Insira um valor válido!\nReiniciando...')
calculadora()