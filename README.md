🏫 Sistema Escolar Django

Sistema web para gerenciamento escolar desenvolvido com Django, permitindo o cadastro e administração de professores, alunos e aulas em uma interface centralizada.

📖 Sobre o Projeto

O Sistema Escolar Django é uma aplicação web back-end desenvolvida para fins educacionais, com foco no aprendizado do framework Django. O sistema permite gerenciar entidades escolares como professores, alunos e aulas por meio de um painel administrativo e rotas organizadas em um app dedicado chamado portal.

Funcionalidades principais:
- Cadastro e listagem de Professores com disciplina, contato e status ativo
- Cadastro e listagem de Alunos com matrícula e informações de contato
- Registro de Aulas com vínculo entre aluno e professor, horário e status (Agendada, Confirmada, Cancelada ou Realizada)
- Painel administrativo Django para gestão completa dos dados

Erros Encontrados:

sistema_escolar_django/  
├── Portal/
│ ├── models.py = Adicionado na linha 2 o comando from django.utils import timezone 
│                 Alteração do tipo errado: models.IntegerField() para models.CharField
│ ├── views.py = correção do caminho para 'portal/index.html'
│ ├── forms.py = Implementação correta de from portal.models import Professor
│ ├── admin.py = Troca do campo inexistente 'especialidade' por 'disciplina'
│ └── urls.py = Remoção da linha: path('cadastro/',views.cadastro) pois não existia em views.py
├── sistema/
│ ├── urls.py = Texto sem formatação. Removida a sintaxe errada e adicionado: include('portal.urls')
│ └── settings.py = Faltou registrar o app 'portal'. Foi adicionado da seguinte forma: 'portal',
└── manage.py





Alexander de Oliveira Ribeiro
