# Projeto Ágil - Sistema de Tarefas

## Descrição
API para gerenciamento de tarefas usando Flask e MySQL.

## Funcionalidades
- Criar tarefas
- Listar tarefas
- Atualizar tarefas
- Deletar tarefas

# Tecnologias
- Python
- Flask
- MySQL

## Metodologia
Kanban (To Do, In Progress, Done)

# Como rodar
python app.py

# Estrutura do Projeto
- /src -> Código da aplicação
- /tests -> Testes automatizados
- /.github/workflows -> Integração contínua (CI)

# Testes Automatizados
Os testes foram implementados utilizando Pytest para validar o funcionamento da API.
Para rodar localmente:
pytest

##Integração Contínua
O projeto utiliza GitHub Actions para executar testes automaticamente a cada push no repositório.

# Mudança de Escopo
Durante o desenvolvimento, foi adicionada a funcionalidade de status das tarefas (To Do, In Progress, Done), permitindo melhor controle do fluxo de trabalho.
