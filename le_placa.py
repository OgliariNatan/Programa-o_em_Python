import cv2
import pytesseract
from pytesseract import Output
from PIL import Image
import string
import re
import numpy as np
###Instancia o pytesseract
caminho = r"C:\Program Files\Tesseract-OCR"
pytesseract.pytesseract.tesseract_cmd = caminho + r'\tesseract.exe'

img2 = cv2.imread("placa-carro.jpg")
img = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
(T,Thresh1) = cv2.threshold(img, 44, 54, cv2.THRESH_TRUNC)
(T,Thresh3) = cv2.threshold(Thresh1, 43, 44, cv2.THRESH_BINARY)
(T,Thresh2) = cv2.threshold(Thresh3, 0 ,255,
 cv2.ADAPTIVE_THRESH_GAUSSIAN_C)
(T,Thresh4) = cv2.threshold(Thresh2, 30, 255, cv2.CALIB_CB_ADAPTIVE_THRESH)
nome_da_janela = 'Placa lida'
cv2.imshow(nome_da_janela, Thresh4)
cv2.waitKey(0)

print( 'PIXEL DA IMAGEM: ' + str(img))

print('\n\n\nUSO DA BIBLIOTECA TESSERACT')

texto1 = pytesseract.image_to_string(img, lang='por')
print( 'Lido a placa:' + texto1)

imagem_a_ser_lida = 'print_5.jpg'

imagem = cv2.imread(imagem_a_ser_lida)
texto = pytesseract.image_to_string(imagem, lang='por')
print(texto)

############### FROM
print('AQUI PAR ABAIXO')
d = pytesseract.image_to_data(imagem, output_type=Output.DICT)
print(d.keys())

n_bordas = len(d['text'])
for i in range(n_bordas):
     if int(d['conf'][i]) > 60 :
      (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
      img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

nome_da_janela_1 = ' Imagem com retangulo'
cv2.imshow(nome_da_janela_1, imagem) #Indica o nome do retangulo e a imagem a ser exibida.
cv2.waitKey(0)