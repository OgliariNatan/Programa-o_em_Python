import cv2
import pytesseract
from PIL import Image
import string
import re





img2 = cv2.imread("placa-carro.jpg")
img = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
(T,Thresh1) = cv2.threshold(img, 44, 54, cv2.THRESH_TRUNC)
(T,Thresh3) = cv2.threshold(Thresh1, 43, 44, cv2.THRESH_BINARY)
(T,Thresh2) = cv2.threshold(Thresh3, 0 ,255,
 cv2.ADAPTIVE_THRESH_GAUSSIAN_C)
(T,Thresh4) = cv2.threshold(Thresh2, 30, 255, cv2.CALIB_CB_ADAPTIVE_THRESH)
cv2.imshow("Placa lida", Thresh4)
cv2.waitKey(0)

print( 'PIXEL DA IMAGEM: ' + str(img))

print('\n\n\nUSO DA BIBLIOTECA TESSERACT')
"""
#caminho = C:\Program Files\Tesseract-OCR\tesseract.exe
pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\tesseract.exe'
img3 = cv2.imread("texto.jpg")
texto = pytesseract.image_to_string(img3)
print(texto)
"""
imagem = cv2.imread("placa-carro.jpg")

caminho = r"C:\Program Files\Tesseract-OCR"
#pytesseract.pytesseract.tesseract_cmd = caminho + r'\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
texto = pytesseract.image_to_string(imagem)
print('Lido: ' + texto)
print('FIM')