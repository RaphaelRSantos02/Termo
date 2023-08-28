from pick import pick
from os import system
import time
import random
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

colorama_init()

palavra = ["fazer" "plena","fosse", "pisca", "justo", "tempo", "causa", "dizer", "prole", "comum", "ainda", "digno", "mundo", "feliz", "coisa"]
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
            if i != 11:
                tentativas = input("Digite sua tentativa: ")
                if tentativas.isspace() or tentativas == '':
                        tentativas = ''
                        print('Por favor digite sua tentativa')
                        time.sleep(1.4)
                elif len(tentativas) <5 or len(tentativas) > 5: 
                    print('Por favor digite uma palavra com 5 letras')
                    time.sleep(2)
                else:
                    if tentativas == termo:
                        print("Você acertou a palavra, saia e entre de novo caso queria jogar com outra palavra ")
                        time.sleep(2)
                    else:
                        string = ''
                        if ((tentativas[0] in termo) or (tentativas[1] in termo) or
                        (tentativas[2] in termo) or (tentativas[3] in termo) or 
                        (tentativas[4] in termo)):
                            for letra in range(len(tentativas)):
                                if tentativas[letra] == termo[letra]:
                                    string+=f'{Fore.GREEN}{tentativas[letra]}{Style.RESET_ALL}'
                                elif tentativas[letra] in termo:
                                    string+=f'{Fore.YELLOW}{tentativas[letra]}{Style.RESET_ALL}'
                                else:
                                    string += f'{Fore.RED}{tentativas[letra]}{Style.RESET_ALL}'
                        else:
                            string = "Você errou todas as letras tente novamente"

                        lista.append(tentativas)
                        print(string)
                        time.sleep(2)
                i+=1
            else:
                print("Acabou suas tentativas, tente novamente amanhã ou fecha e abra o arquivo")
                time.sleep(4)

        case 1:
                if len(lista) == 0:
                     title = "Não houve nenhuma tentativa ainda."
                     
                else:
                    title = f"Essas foram suas tentativas: "
                    for item in lista:
                         title+=f'\n- {item}'
                     
                option = ['Inicio' , 'Sair']
                option, index = pick(options=option, title=title, indicator= '-->', default_index=0)

                if index == 1:
                     exit()
        case 2:
              exit()