from pick import pick
from os import system
import time
import random



palavra = ["fazer", "plena","fosse", "pisca", "justo", "tempo", "causa", "dizer", "prole", "comum", "ainda", "digno", "mundo", "feliz", "coisa"]
termo = random.choice(palavra)

lista = []
i = 0

while True:
    system('cls')
    

    title = f"Termo \nDica: a palavra possui {len(termo)} letras"
    option = ['Inicio', 'Ver tentativas' , 'Sair']

    option, index = pick(options=option, title= title, indicator= '-->', default_index=0)

    match index:
        case 0:
            if i != 10:
                tentativas = input("Digite sua tentativa: ")
                if tentativas.isspace() or tentativas == '':
                        tentativas = ''
                        print('Por favor digite sua tentativa')
                        time.sleep(1.4)
                elif len(tentativas) <5 or len(tentativas) > 5: 
                    print('Por favor digite uma palavra com 5 letras')
                    time.sleep(2)
                else:
                    lista.append({tentativas})
                    if tentativas == termo:
                        print("Você acertou a palavra, saia e entre de novo caso queria jogar com outra palavra ")

                    elif tentativas[i] == termo[i]:
                        for letra in termo:
                                if letra in tentativas: 
                                    print(f"a letra: [{letra}] está na posição: [{tentativas[i]}] ")     
                                time.sleep(2)

                    else: 
                        print("Você errou todas as palavras tente novamente ")
                        i += 1
                time.sleep(2)
            else:
                print("Acabou suas tentativas, tente novamente amanhã ou fecha e abra o arquivo")

                
         
        case 1:
                if len(lista) == 0:
                     title = "Não houve nenhuma tentativa ainda."
                     
                else:
                    title = f"Essas foram suas tentativa: {lista} "
                     
                option = ['Inicio' , 'Sair']
                option, index = pick(options=option, title= title, indicator= '-->', default_index=0)

                

                if index == 1:
                     exit()
        case 2:
              exit()
