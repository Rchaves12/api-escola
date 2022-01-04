import requests

headers = {'Authorization': 'Token 09d529fa57a7e423978465b4c645cedf0ba398f9'}
url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'


curso_atualizado = {
    "titulo": "Gerencia Ágil de Projetos com Scrum 3",
    "url": "http://www.geekuniversity.com.br/ncs3"
}

# Buscanado o curso com ID 6
# curso = requests.get(url=f'{url_base_cursos}6/', headers=headers)
# print(curso.json())

resultado = requests.put(url=f'{url_base_cursos}6/', headers=headers, data=curso_atualizado)
# print(resultado)
# Testando Código de status HTTP
assert resultado.status_code == 200

# Tetando o título
assert resultado.json()['titulo'] == curso_atualizado['titulo']
