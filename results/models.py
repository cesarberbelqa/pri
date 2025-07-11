from django.db import models

class ResultSection(models.Model):
    """Configuração da seção de resultados na página inicial."""
    title = models.CharField(max_length=100, default="Nossos Resultados em Números", verbose_name="Título da Seção")
    is_active = models.BooleanField(default=True, verbose_name="Mostrar seção na home?")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última Atualização")

    class Meta:
        verbose_name = "Configuração da Seção de Resultados"
        verbose_name_plural = "Configurações da Seção de Resultados"

    def __str__(self):
        return self.title

class ResultCard(models.Model):
    """Representa um card individual na seção de resultados."""
    icon = models.CharField(
        max_length=50, 
        verbose_name="Ícone (Font Awesome)", 
        help_text="Ex: 'fas fa-heart' ou 'fa-solid fa-users'. Encontre ícones em fontawesome.com."
    )
    target_number = models.PositiveIntegerField(verbose_name="Número Alvo")
    title = models.CharField(max_length=100, verbose_name="Título do Card")
    order = models.PositiveIntegerField(default=0, verbose_name="Ordem de Exibição")
    is_active = models.BooleanField(default=True, verbose_name="Card Ativo?")
    
    class Meta:
        verbose_name = "Card de Resultado"
        verbose_name_plural = "Cards de Resultado"
        ordering = ['order']

    def __str__(self):
        return self.title