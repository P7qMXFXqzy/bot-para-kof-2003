import pyautogui
#checar se a luta está em andamento; False = luta não acontecendo, True = luta em andamento
def checarLutaAcontecendo():
    #se "press start" está presente na tela, retornar True, senão retornar False
    if(pyautogui.pixel(926,84)[0] == 248):return True
    else:return False
