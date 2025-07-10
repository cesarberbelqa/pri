# services/models.py

from django.db import models
from django.utils import timezone

class Service(models.Model):
    """Modelo para representar os serviços oferecidos."""

    class ServiceCategory(models.TextChoices):
        PODOLOGIA = 'POD', 'Podologia'
        MANICURE = 'MAN', 'Manicure'
        PEDICURE = 'PED', 'Pedicure'
        TRATAMENTO = 'TRT', 'Tratamento Especial'
        OUTROS = 'OUT', 'Outros'

    # Campos principais
    titulo = models.CharField(max_length=100, verbose_name="Título do Serviço")
    descricao = models.TextField(verbose_name="Descrição Detalhada")
    imagem = models.ImageField(upload_to='services_images/', verbose_name="Imagem Ilustrativa")
    
    # Detalhes do serviço
    duracao = models.PositiveIntegerField(help_text="Duração do serviço em minutos.", verbose_name="Duração (min)")
    preco = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Preço (R$)")
    categoria = models.CharField(
        max_length=3,
        choices=ServiceCategory.choices,
        default=ServiceCategory.PODOLOGIA,
        verbose_name="Categoria"
    )

    # Campos de controle
    ativo = models.BooleanField(default=True, verbose_name="Ativo")
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    data_atualizacao = models.DateTimeField(auto_now=True, verbose_name="Última Atualização")
    data_delecao = models.DateTimeField(blank=True, null=True, verbose_name="Data de Deleção")

    class Meta:
        verbose_name = "Serviço"
        verbose_name_plural = "Serviços"
        ordering = ['categoria', 'titulo']

    def __str__(self):
        return self.titulo

    def delete(self, using=None, keep_parents=False):
        """
        Sobrescreve o método delete para implementar a deleção lógica.
        """
        self.ativo = False
        self.data_delecao = timezone.now()
        self.save()