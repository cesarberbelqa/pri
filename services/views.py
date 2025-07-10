# services/views.py

from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Service
from .forms import ServiceForm  # 1. Importe o novo formulário

class ServiceListView(ListView):
    """View para listar todos os serviços ativos."""
    model = Service
    template_name = 'services/service_list.html'
    context_object_name = 'services'
    
    def get_queryset(self):
        # Mostra apenas os serviços ativos para o público geral
        return Service.objects.filter(ativo=True)

# Mixin para garantir que apenas usuários logados possam criar/editar/deletar
class StaffRequiredMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff: # ou is_superuser
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

class ServiceCreateView(StaffRequiredMixin, CreateView):
    """View para criar um novo serviço."""
    model = Service
    form_class = ServiceForm  # 2. Use form_class em vez de 'fields'
    template_name = 'services/service_form.html'
    success_url = reverse_lazy('services:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Cadastrar Novo Serviço'
        return context

class ServiceUpdateView(StaffRequiredMixin, UpdateView):
    """View para atualizar um serviço existente."""
    model = Service
    form_class = ServiceForm  # 3. Use form_class também aqui
    template_name = 'services/service_form.html'
    success_url = reverse_lazy('services:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = f'Editar Serviço: {self.object.titulo}'
        return context

class ServiceDeleteView(StaffRequiredMixin, DeleteView):
    """View para confirmar a deleção (lógica) de um serviço."""
    model = Service
    template_name = 'services/service_confirm_delete.html'
    success_url = reverse_lazy('services:list')
    
    # Sobrescrevemos o método delete para usar nossa deleção lógica do modelo
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()  # Chama o método delete() do nosso modelo
        return HttpResponseRedirect(success_url)