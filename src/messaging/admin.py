from django.contrib import admin
from .models import Message

# Register your models here.

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'subject', 'date_sent', 'is_read')
