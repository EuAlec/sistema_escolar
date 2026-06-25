🏫 Sistema Escolar Django

Sistema web para gerenciamento escolar desenvolvido com Django, permitindo o cadastro e administração de professores, alunos e aulas em uma interface centralizada.

📖 Sobre o Projeto

O Sistema Escolar Django é uma aplicação web back-end desenvolvida para fins educacionais, com foco no aprendizado do framework Django. O sistema permite gerenciar entidades escolares como professores, alunos e aulas por meio de um painel administrativo e rotas organizadas em um app dedicado chamado portal.

Funcionalidades principais:
- Cadastro e listagem de Professores com disciplina, contato e status ativo
- Cadastro e listagem de Alunos com matrícula e informações de contato
- Registro de Aulas com vínculo entre aluno e professor, horário e status (Agendada, Confirmada, Cancelada ou Realizada)
- Painel administrativo Django para gestão completa dos dados


📁 Estrutura do Projeto
sistema_escolar_django/
│
├── sistema/                  # Configurações principais do projeto Django
│   ├── settings.py           # Configurações gerais (banco, apps, idioma)
│   ├── urls.py               # Rotas principais
│   ├── wsgi.py
│   └── asgi.py
│
├── portal/                   # App principal do sistema escolar
│   ├── migrations/           # Histórico de migrações do banco de dados
│   ├── templates/            # Templates HTML
│   ├── static/               # Arquivos estáticos (CSS, JS, imagens)
│   ├── models.py             # Models: Professor, Aluno, Aula
│   ├── views.py              # Lógica das páginas
│   ├── urls.py               # Rotas do app portal
│   ├── forms.py              # Formulários Django
│   └── admin.py              # Configuração do painel admin
│
└── manage.py                 # Utilitário de linha de comando do Django
