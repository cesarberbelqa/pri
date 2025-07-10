# testimonials/admin.py

from django.contrib import admin
from .models import Testimonial

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'created_at', 'is_active')
    list_filter = ('status', 'is_active')
    search_fields = ('name', 'email', 'body')
    list_editable = ('status',) # Allows changing status directly from the list view
    readonly_fields = ('created_at', 'updated_at', 'deleted_at', 'name', 'email', 'body')
    actions = ['approve_testimonials', 'reject_testimonials']

    def has_add_permission(self, request):
        # Admins should not add testimonials, only approve them
        return False

    @admin.action(description='Approve selected testimonials')
    def approve_testimonials(self, request, queryset):
        queryset.update(status=Testimonial.StatusChoices.APPROVED)

    @admin.action(description='Reject selected testimonials')
    def reject_testimonials(self, request, queryset):
        queryset.update(status=Testimonial.StatusChoices.REJECTED)