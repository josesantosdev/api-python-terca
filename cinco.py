import requests
r = requests.get('http://www.google.com/search', params={'q':
'Protocolo HTTP'})
def salvar_arquivo_html (texto_html):
  arquivo = open("dados.txt", "w")
  arquivo.write(texto_html)
  arquivo.close()

if (r.status_code == 200):
 print()
 print('Retorno : ', r.text)
 print()
else:
 print('Nao houve sucesso na requisicao.')