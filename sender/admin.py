from django.contrib import admin
from sender.models import MessageQueue, Client

# Register your models here.
admin.site.register(MessageQueue)
admin.site.register(Client)