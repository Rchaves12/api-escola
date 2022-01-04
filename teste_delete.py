import requests

headers = {'Authorization': 'Token 09d529fa57a7e423978465b4c645cedf0ba398f9'}
url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'




# Buscanado o curso com ID 6
# curso = requests.get(url=f'{url_base_cursos}6/', headers=headers)
# print(curso.json())

resultado = requests.delete(url=f'{url_base_cursos}6/', headers=headers)

# Testando Código de status HTTP
assert resultado.status_code == 204

# Testando se o tamanho do conteúdo retorno é 0
assert len(resultado.text) == 0
