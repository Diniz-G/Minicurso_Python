#from random import randint
import random

print('*****************************')
print('**** Jogo da adivinhação ****')
print('*****************************')

n_sec = random.randint(1, 100)
tentativas = 10
rodada = 1

#print(n_sec)
#while(tentativas >= rodada):
for rodada in range(1, tentativas + 1):
    print('### Tentativa', rodada, 'de', tentativas,'###')
    chute = input('Digite um número de 1 a 100: ')
    chute = int(chute)
    #print(chute, 'Esse é o seu chute!')

    igual = chute == n_sec
    maiorq = chute > n_sec
    #if(chute<1 or chute>100):
    #    continue #quebra o laço, indo para a proxima rodada
    if(chute>=1 and chute <=100):
        if(igual):
            print("Boa garoto!!")
            break
        else:
            print("Errado!")
            if(maiorq):
                print('Muito alto!')
            else:
                print('Muito baixo!')
        
        rodada = rodada + 1
    else:
        print('Chute fora dos valores')

print('Game Over\nO número secreto era', n_sec,"!")
print('Você gastou', rodada, 'chances.')