
from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_usuarios, name='lista_usuarios'),
    path('novo/', views.cadastrar_usuario, name='cadastrar_usuario'),
    path('<int:usuario_id>/', views.perfil_usuario, name='perfil_usuario'),
    path('excluir/<int:usuario_id>/', views.excluir_usuario, name='excluir_usuario'),
]
