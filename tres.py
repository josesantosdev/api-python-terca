import requests

url = 'https://viacep.com.br/ws/'
formato = '/json/'

def consultar_endereco(uf, cidade, logradouro):
  r = requests.get(f'{url}/{cidade}/{logradouro}{formato}')
  if (r.status_code == 200):
    return r.json()
  else:
    return []


def mostrar_resultados_busca(enderecos):

  total_enderecos = len(enderecos)

  if total_enderecos == 0:
    print('Nenhum resultado encontrado!')
  else:
    for i in range(total_enderecos):
      logradouro = enderecos[i]['logradouro']
      complemento =  enderecos[i]['complemento']
      bairro = enderecos[i]['bairro']
      localidade =  enderecos[i]['localidade']
      uf =  enderecos[i]['uf']
      cep =  enderecos[i]['cep']

    endereco_formatado = '{0}, {1}, {2}, {3}, {4}, {5}, {6}'.format(logradouro, complemento, bairro, localidade, uf, cep)

    print(f'[{i + 1}'\t.endereco_formatado)

if _name_ == 'main':
  uf = input('Qual é o seu estado (UF)?')
  cidade  = input('Qual a sua cidade? ')
  logradouro = input('Qual é o nome do logradouro?')
  enderecos= list(consultar_endereco(uf, cidade, logradouro))