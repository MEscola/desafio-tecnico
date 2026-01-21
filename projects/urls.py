from django.urls import path
from . import views

urlpatterns = [
    # Exemplo: Se você tiver uma view chamada 'lista_projetos'
    # path('', views.lista_projetos, name='lista_projetos'),
    
    # Se você quiser que a home do projeto seja acessada aqui também:
    path('', views.home, name='home'),
    path('cadastro/', views.cadastrar_projeto, name='cadastrar_projeto'),
    #path('projeto/<int:project_id>/subitem/', views.subitem, name='adicionar_subitem'),
    path('lista/', views.lista_projetos, name='lista_projetos'),
    path('projeto/<int:project_id>/',views.detalhe_projeto, name='detalhe_projeto'),
    path('projeto/<int:project_id>/subitem/',views.criar_subitem,name='criar_subitem'),
    path('projeto/deletar/<int:project_id>/', views.deletar_projeto, name='deletar_projeto'),
    path('subitem/deletar/<int:subitem_id>/', views.deletar_subitem, name='deletar_subitem'),
    path('projeto/editar/<int:project_id>/', views.editar_projeto, name='editar'),
]