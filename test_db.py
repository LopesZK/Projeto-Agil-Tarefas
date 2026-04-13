from db import conectar

conn = conectar()
cursor = conn.cursor()

cursor.execute(
    "INSERT INTO tarefas (titulo, descricao, status) VALUES (%s, %s, %s)",
    ("Teste Python", "Integração funcionando", "A Fazer")
)

conn.commit()

print("✅ Inserido com sucesso!")