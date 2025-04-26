import random
num = int(random.randrange(1, 50))
cont = 0
while True:
    resp = int(input('Insira um número entre 1 à 50: '))
    if resp == num: 
        print(f'\nParabéns, você acertou! O número era {num}!\nForam necessárias {cont} tentativas!')
        print('='*45)
        break
    elif resp < num:
        print(f'\nO número {resp} está abaixo do escolhido!')
        cont += 1
        print('-'*45)
    elif resp > num:
        print(f'\nO número {resp} está acima do escolhido!')
        cont += 1
        print('-'*45)
    else:
        print('\nInsira um valor válido!')
        print('-'*45)