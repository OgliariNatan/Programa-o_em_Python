
'''Implementação para testes de busca e processamento
dados do agor...'''


import urllib2
import urllib
import json
import pprint

#uso do modulo JSON como dicionario
data_string = urllib.quote(json.dumps({'id': 'data-explorer'}))

#cria a requisição http

response = urllib2.urlopen('http://demo.ckan.org/api/3/action/group_list', data_string)

assert response.code == 200

response_dict = json.loads(response.read())

#checa se o conteudo foi coletado
assert response_dict['success'] is True
result = response_dict['result']
pprint.pprint(result)