import math
#Informa ao usuario o proposito deste scripty
print("Bem vindo ao sistema de calculo de seu Indice de massa corporal")
print("Para este calculo irei solicitar algumas informações pessoais.")
#realiza a leitura dos dados
peso = input ("Digite o seu peso em kg: ")
altura = input ("Digite a sual altura em metros: ")

IMC = float(peso) / math.pow ( float(altura) ,2) #Calcula o IMC
#print( type (peso))
#print (type(altura))
#print (type(IMC))

#imprimi o resultado do calculo do IMC
print(f"Seu IMC é:  %.2f" %IMC)
# Informa a sua situação
if IMC < 17:
     print("Seu peso esta MUITO abaixo do ideal")
elif IMC >= 17 and IMC < 18.49:
    print("Você esta abaixo do peso")
elif IMC > 18.49 and IMC < 24.99:
    print("Peso Normal")
elif IMC > 24.99 and IMC < 29.99:
    print("Acima do peso")
elif IMC > 29.99 and IMC < 34.99:
    print("Abesidade Grau 1")
elif IMC > 34.99 and IMC < 39.99:
    print("Abesidade Grau 1")
else:
  print("Seu IMC está como obesidade grau 3 (Mórbida)")