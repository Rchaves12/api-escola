import requests


# GET Avaliações

# avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes/')

# Acessando o código de Status HTTP
# print(avaliacoes.status_code)

# Acessando os dados da resposta
# print(avaliacoes.json())
# print(type(avaliacoes.json()))

# Acessando a quantidade de registros
# print(avaliacoes.json()['count'])

# Acessando a próxima página de resultados
# print(avaliacoes.json()['next'])

# Acessando os resultados desta página
# print(avaliacoes.json()['results'])
# print(type(avaliacoes.json()['results']))

# Acessando o primeiro elemento da lista de resultados
# print(avaliacoes.json()['results'][0])

# Acessando o ultimo elemento da lista de resultados
# print(avaliacoes.json()['results'][-1])

# Acessando somento o nome da pessoal que fez a última avaliação
# print(avaliacoes.json()['results'][-1]['nome'])


# GET Avaliação
# avaliacao = requests.get('http://localhost:8000/api/v2/avaliacoes/3/')

# Acessando o código de Status HTTP
# print(avaliacao.json())

# GET Cursos

headers = {'Authorization': 'Token da4746c40cf29fbab46064c68291feeca68303c2'}
cursos = requests.get(url='http://localhost:8000/api/v2/cursos/', headers=headers)

print(cursos.status_code)
print(cursos.json())
