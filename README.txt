Gerenciador de Tarefas em Python (Tkinter)

Aplicativo simples feito em Python + Tkinter para organizar tarefas diárias.
Permite adicionar tarefas com título, prazo e prioridade, marcar como concluídas e manter um histórico.

Funcionalidades

Adicionar tarefas com título, data limite (DD/MM/AAAA) e prioridade (Alta, Média, Baixa)

Destaca em vermelho as tarefas atrasadas

Ordenação automática por prioridade e data

Salva tudo em um arquivo tarefas.json

Histórico de tarefas concluídas

Inicia junto com o Windows (opcional, usando atalho no shell:startup)

Instalação e Uso
1. Clone o repositório
git clone https://github.com/seuusuario/APP-Tarefas.git
cd gerenciador-tarefas

2. Rode o app
python tarefas.py


Certifique-se de ter o Python 3.10+ instalado.

3. Criar executável (opcional)

Para rodar sem precisar do Python:

pip install pyinstaller
pyinstaller --onefile --noconsole tarefas.py


O arquivo ficará disponível em dist/tarefas.exe.

Iniciar junto com o Windows

Para abrir automaticamente ao ligar o PC:

Pressione Win + R → digite shell:startup

Cole um atalho do tarefas.py (usando pythonw.exe) ou do tarefas.exe dentro dessa pasta

Reinicie o Windows

Estrutura do projeto
gerenciador-tarefas/
 ┣ tarefas.py        # Código principal do app
 ┣ tarefas.json      # Arquivo gerado automaticamente com suas tarefas
 ┗ README.md         # Este documento

Tecnologias

Python

Tkinter

Melhorias futuras

Editar tarefas existentes

Adicionar lembretes/alertas

Exportar histórico para CSV/Excel

Versão web (Flask ou Django)

Autor

Feito por Alaor Jorge



Se gostou, deixe uma estrela no repositório.
