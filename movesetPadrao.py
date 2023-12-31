import pyautogui
from time import sleep
from random import choice, randint
class classeMovesetPadrao:
    #z = soco fraco; c = soco forte x = chute fraco; a = chute forte; i = cima; j = trás; k = baixo; l = frente.
    botoesAtaque = ["z", "c", "a", "x"]
    botoesMovimento = ["i", "j", "k", "l"]
    #apertar um único botão (seja ataque ou movimento)
    def botaoUnico(self):
        botaoEscolhido = choice(self.botoesAtaque)
        pyautogui.keyDown(botaoEscolhido)
        pyautogui.keyUp(botaoEscolhido)
    #realizar um ataque com um movimento
    def ataqueComMovimento(self):
        direcionalEscolhido = choice(self.botoesMovimento)
        ataqueEscolhido = choice(self.botoesAtaque)
        pyautogui.keyDown(direcionalEscolhido)
        pyautogui.keyDown(ataqueEscolhido)
        pyautogui.keyUp(ataqueEscolhido)
        pyautogui.keyUp(direcionalEscolhido)
    #soltar um golpe especial
    def ataqueEspecial(self):
        ataqueEscolhido = choice(self.botoesAtaque)
        id = randint(0, 3)
        #sentido 0 = sentido normal; sentido 1 = sentido invertido
        sentido = randint(0, 1)
        #meia-lua
        if(id == 0):
            if(sentido == 0):direcional = "l"
            else:direcional = "j"
            pyautogui.keyDown("k")
            pyautogui.keyDown(direcional)
            pyautogui.keyUp("k")
            pyautogui.keyUp(direcional)
            pyautogui.keyDown(ataqueEscolhido)
            pyautogui.keyUp(ataqueEscolhido)
        #meia-lua completa
        elif(id == 1):
            if(sentido == 0):
                direcionalUm = "j"
                direcionalDois = "l"
            else:
                direcionalUm = "l"
                direcionalDois = "j"
            pyautogui.keyDown(direcionalUm)
            pyautogui.keyDown("k")
            pyautogui.keyUp(direcionalUm)
            pyautogui.keyDown(direcionalDois)
            pyautogui.keyUp("k")
            pyautogui.keyUp(direcionalDois)
            pyautogui.keyDown(ataqueEscolhido)
            pyautogui.keyUp(ataqueEscolhido)
        #frente e meia-lua
        elif(id == 2):
            if(sentido == 0):direcional = "l"
            else:direcional = "j"
            pyautogui.keyDown(direcional)
            pyautogui.keyDown("k")
            pyautogui.keyUp(direcional)
            pyautogui.keyDown(direcional)
            pyautogui.keyUp("k")
            pyautogui.keyDown(ataqueEscolhido)
            pyautogui.keyUp(direcional)
            pyautogui.keyUp(ataqueEscolhido)
        #frente, trás, frente
        elif(id == 3):
            if(sentido == 0):
                direcionalUm = "l"
                direcionalDois = "j"
            else:
                direcionalUm = "j"
                direcionalDois = "l"
            pyautogui.keyDown(direcionalUm)
            pyautogui.keyUp(direcionalUm)
            pyautogui.keyDown(direcionalDois)
            pyautogui.keyUp(direcionalDois)
            pyautogui.keyDown(direcionalUm)
            pyautogui.keyUp(direcionalUm)
            pyautogui.keyDown(ataqueEscolhido)
            pyautogui.keyUp(ataqueEscolhido)
    #soltar um super especial (que consume a barra de energia)
    def superEspecial(self):
        ataqueEscolhido = choice(self.botoesAtaque)
        id = randint(0, 5)
        #sentido 0 = sentido normal; sentido 1 = sentido invertido
        sentido = randint(0, 1)
        #duas meias luas
        if(id == 0):
            if(sentido == 0): direcional = "l"
            else: direcional = "j"
            pyautogui.keyDown("k")
            pyautogui.keyDown(direcional)
            pyautogui.keyUp("k")
            pyautogui.keyUp(direcional)
            pyautogui.keyDown("k")
            pyautogui.keyDown(direcional)
            pyautogui.keyUp("k")
            pyautogui.keyUp(direcional)
            pyautogui.keyDown(ataqueEscolhido)
            pyautogui.keyUp(ataqueEscolhido)
        #duas meias luas completas
        elif(id == 1):
            if(sentido == 0): 
                direcionalUm = "j"
                direcionalDois = "l"
            else:
                direcionalUm = "l"
                direcionalDois = "j"
            pyautogui.keyDown(direcionalUm)
            pyautogui.keyDown('k')
            pyautogui.keyUp(direcionalUm)
            pyautogui.keyDown(direcionalDois)
            pyautogui.keyUp('k')
            pyautogui.keyUp(direcionalDois)
            pyautogui.keyDown(ataqueEscolhido)
            pyautogui.keyUp(ataqueEscolhido)
        #comando para o ataque "Power Geyser"
        elif(id == 2):
            if(sentido == 0): 
                direcionalUm = "j"
                direcionalDois = "l"
            else:
                direcionalUm = "l"
                direcionalDois = "j"
            pyautogui.keyDown("k")
            pyautogui.keyDown(direcionalUm)
            pyautogui.keyUp("k")
            pyautogui.keyUp(direcionalUm)
            pyautogui.keyDown("k")
            pyautogui.keyDown(direcionalUm)
            pyautogui.keyUp("k")
            pyautogui.keyUp(direcionalUm)
            pyautogui.keyDown(direcionalDois)
            pyautogui.keyDown(ataqueEscolhido)
            pyautogui.keyUp(ataqueEscolhido)
            pyautogui.keyUp(direcionalDois)
        #comando para o ataque "Haoh Shoukouken"
        elif(id == 3):
            if(sentido == 0): 
                direcionalUm = "j"
                direcionalDois = "l"
            else:
                direcionalUm = "l"
                direcionalDois = "j"
            pyautogui.keyDown(direcionalDois)
            pyautogui.keyUp(direcionalDois)
            pyautogui.keyDown(direcionalUm)
            pyautogui.keyDown("k")
            pyautogui.keyUp(direcionalUm)
            pyautogui.keyDown(direcionalDois)
            pyautogui.keyUp("k")
            pyautogui.keyUp(direcionalDois)
            pyautogui.keyDown(ataqueEscolhido)
            pyautogui.keyUp(ataqueEscolhido)
        #uma meia lua pra frente e uma meia lua completa pra trás
        elif(id == 3):
            if(sentido == 0): 
                direcionalUm = "j"
                direcionalDois = "l"
            else:
                direcionalUm = "l"
                direcionalDois = "j"
            pyautogui.keyDown("k")
            pyautogui.keyDown(direcionalDois)
            pyautogui.keyUp("k")
            pyautogui.keyDown("k")
            pyautogui.keyUp(direcionalDois)
            pyautogui.keyDown(direcionalUm)
            pyautogui.keyUp("k")
            pyautogui.keyUp(direcionalUm)
            pyautogui.keyDown(ataqueEscolhido)
            pyautogui.keyUp(ataqueEscolhido)
    #trocar personagem durante a luta
    def trocarPersonagem(self):
        #"sentido" define que personagem entrará na luta
        sentido = randint(0,1)
        if(sentido == 0): botaoSelecionado = "a"
        else: botaoSelecionado = "x"
        pyautogui.keyDown(botaoSelecionado)
        pyautogui.keyDown("c")
        pyautogui.keyUp(botaoSelecionado)
        pyautogui.keyUp("c")
    #executar um dash (pressionar duas vezes na mesma direção)
    def dash(self):
        sentido = randint(0, 1)
        if(sentido == 0): sentido = "l"
        else: sentido = "j"
        pyautogui.keyDown(sentido)
        pyautogui.keyUp(sentido)
        pyautogui.keyDown(sentido)
        pyautogui.keyUp(sentido)