def calculator():
    print('°<[}- - Calculator - -{]>°')
 
    while True:
        try:
            v1 = float(input('Type the first value: '))
            v2 = float(input('Type the second value: '))
            break
        except ValueError:
            print('Insert valid values!\nRestarting . . .')
        print(f'Chosen values: {v1} e {v2}')

    while True:
        operator = (input('Type the desired operation: '))
        match operator:
          case '+':
            print(f'The sum of {v1} + {v2} = {v1+v2}')
            break
          case '-':
            print(f'The subtraction of {v1} - {v2} = {v1-v2}')
            break
          case '*':
            print(f'The multiplication of {v1} x {v2} = {v1*v2}')
            break
          case '/':
            if v1 == 0 or v2 == 0:
               print('Invalid results for divisions with 0!')
               break
            else:
                print(f'The division of {v1} / {v2} = {v1/v2}')
                break
          case _:
            print(f'Insert a valid operator!\nRestarting...')
calculator()