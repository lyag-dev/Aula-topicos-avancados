from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_inicial, name='pagina_inicial'),
    path('api/alunos', views.api_alunos, name='api_alunos'),
    path('api/alunos/<int:id>', views.api_alunos_detalhe, name='api_alunos_detalhe'),
]

