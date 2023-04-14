from matplotlib import pyplot as plt
import cv2
import math
import requests



"""PARA TESTE DA BIBLIOTECA OPENCV, PARA analise de imagens"""


img = cv2.imread('download.png', cv2.IMREAD_COLOR)

cv2.namedWindow('Ola Mundo')
cv2.imshow('PAGINA INICIAL, VEJA COMO FICA', img)
cv2.waitKey()

for y in range(0, img.shape[0], 10): #percorre linhas
        for x in range(0, img.shape[1], 10): #percorre colunas
            img[y:y+5, x: x+5] = (0,255,255)

cv2.imshow("Imagem modificada", img)
cv2.waitKey(0)

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#Converto em gray
cv2.imshow('Imagem convertida')
#Função cria histograma
h = cv2.calHist([img], [0], None, [256], [0, 256])
plt.figure()
plt.title('Histograma da imagem')
plt.xlabel('Intensidade')
plt.ylabel('quantidade de pixel')
plt.plot(h)
plt.xlim([0, 256])
plt.show()
cv2.waitKey(0)


#Página 55