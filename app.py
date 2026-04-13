from flask import Flask, request, jsonify
from db import conectar

app = Flask(__name__)

@app.route('/')
def home():
    return "API Rodando!"

# Criar tarefa
@app.route('/tarefas', methods=['POST'])
def criar_tarefa():
    dados = request.json
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO tarefas (titulo, descricao, status) VALUES (%s, %s, %s)",
        (dados['titulo'], dados['descricao'], 'A Fazer')
    )
    conn.commit()

    return jsonify({"mensagem": "Tarefa criada!"})

# Listar tarefas
@app.route('/tarefas', methods=['GET'])
def listar():
    conn = conectar()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM tarefas")
    tarefas = cursor.fetchall()

    return jsonify(tarefas)

# Atualizar
@app.route('/tarefas/<int:id>', methods=['PUT'])
def atualizar(id):
    dados = request.json
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE tarefas SET titulo=%s, descricao=%s, status=%s WHERE id=%s",
        (dados['titulo'], dados['descricao'], dados['status'], id)
    )
    conn.commit()

    return jsonify({"mensagem": "Atualizada!"})

# Deletar
@app.route('/tarefas/<int:id>', methods=['DELETE'])
def deletar(id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM tarefas WHERE id=%s", (id,))
    conn.commit()

    return jsonify({"mensagem": "Deletada!"})

if __name__ == '__main__':
    app.run(debug=True)