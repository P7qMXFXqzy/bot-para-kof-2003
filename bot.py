import keyboard
from time import sleep
from random import randint
from movesetPadrao import classeMovesetPadrao
import checagens
    
            
objetoMoveset = classeMovesetPadrao()
while keyboard.is_pressed('q')==False:
    if(checagens.checarLutaAcontecendo() == True):
        escolha = randint(1, 6)
        if(escolha == 1):objetoMoveset.botaoUnico()
        elif(escolha == 2):objetoMoveset.ataqueComMovimento()
        elif(escolha == 3):objetoMoveset.ataqueEspecial()
        elif(escolha == 4):objetoMoveset.superEspecial()
        elif(escolha == 5):objetoMoveset.trocarPersonagem()
        elif(escolha == 6): objetoMoveset.dash()
    else:print("luta não acontecendo")