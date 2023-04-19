import requests




info = requests.get('https://www.json.org/json-en.html')
dados1 = info.text
dados2 = info.json()
print(type(dados1))
print(type(dados2))