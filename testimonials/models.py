# testimonials/models.py

from django.db import models
from django.utils import timezone

class Testimonial(models.Model):
    """Model to store customer testimonials."""

    class StatusChoices(models.TextChoices):
        PENDING = 'PEN', 'Pending Review'
        APPROVED = 'APR', 'Approved'
        REJECTED = 'REJ', 'Rejected'

    # Core fields
    name = models.CharField(max_length=100, verbose_name="Name")
    email = models.EmailField(verbose_name="Email") # Django's EmailField provides validation
    body = models.TextField(verbose_name="Testimonial Body")
    
    # Moderation and control fields
    status = models.CharField(
        max_length=3,
        choices=StatusChoices.choices,
        default=StatusChoices.PENDING,
        verbose_name="Status"
    )
    is_active = models.BooleanField(default=True, verbose_name="Is Active")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creation Date")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Last Update")
    deleted_at = models.DateTimeField(blank=True, null=True, verbose_name="Deletion Date")

    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"
        ordering = ['-created_at'] # Show newest testimonials first in the admin

    def __str__(self):
        return f'Testimonial by {self.name} ({self.status})'
    
    def delete(self, using=None, keep_parents=False):
        """
        Overrides the delete method to implement logical deletion.
        """
        self.is_active = False
        self.deleted_at = timezone.now()
        self.save()