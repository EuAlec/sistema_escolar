from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # ERRO ENCONTRADO: texto livre, impedindo o python de ler o arquivo
    # CORREÇÃO: retirar a sintaxe incorreta, adicionar include('portal.urls') e adicionar include na linha 2, após <path>
    path('cadastro/', include('portal.urls')),  # ERRO 4: sintaxe inválida. Deve ser: include('portal.urls') ou views.cadastro
]


# Verbos HTTP - FRONTEND <-> BACKEND
#  GET -> www.escola.com -> Exiba a página home da escola.
#  POST -> www.escola.com/cadastro -> Cadastrando um novo usuário.
#  PUT -> www.escola.com/logado/alterar/1 -> Alterando o dado do usuário.
#  DELETE -> www.escola.com/logado/deletar/1 -> Deletando um usuário.
