# services/urls.py

from django.urls import path
from .views import ServiceListView, ServiceCreateView, ServiceUpdateView, ServiceDeleteView

app_name = 'services'  # Namespace para as URLs

urlpatterns = [
    # URL para listar todos os serviços (ex: /servicos/)
    path('', ServiceListView.as_view(), name='list'),
    
    # URL para criar um novo serviço (ex: /servicos/novo/)
    path('create/', ServiceCreateView.as_view(), name='create'),
    
    # URL para editar um serviço existente (ex: /servicos/1/editar/)
    path('<int:pk>/update/', ServiceUpdateView.as_view(), name='update'),
    
    # URL para deletar um serviço existente (ex: /servicos/1/deletar/)
    path('<int:pk>/delete/', ServiceDeleteView.as_view(), name='delete'),
]