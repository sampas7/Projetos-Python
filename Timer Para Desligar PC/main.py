import PySimpleGUI as sg
import pyautogui
import time

layout = [

    [sg.Text('Informe o tempo para desligar o PC. (em segundos)')],
    [sg.InputText(key = 'tempo_deslig')],
    [sg.Button('Confirmar'), sg.Button('Cancelar')],
    [sg.Text('É o Sampas.')],

]

janela = sg.Window('Desligar PC', layout)

while True:
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED or evento == 'Cancelar':
        break

    if evento == 'Confirmar':

        vari_tempo = valores['tempo_deslig']
        vari_tempo = float(vari_tempo)

        pyautogui.PAUSE = 1.5
        time.sleep(vari_tempo)
        pyautogui.press('win')
        time.sleep(1)
        pyautogui.click(x=27, y=993)
        time.sleep(2)
        pyautogui.click(x=45, y=891)
        pyautogui.click(x=45, y=891)


janela.close()
