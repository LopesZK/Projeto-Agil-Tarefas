import requests

url = "http://127.0.0.1:5000/tarefas/1"

dados = {
    "titulo": "Atualizado",
    "descricao": "Agora funcionando 100%",
    "status": "Concluído"
}

resposta = requests.put(url, json=dados)

print(resposta.json())