import uuid

from django.db import models
from django.db.models import Q


class Client(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    phone = models.CharField(max_length=11)
    operator = models.CharField(max_length=3)
    tag = models.CharField(max_length=10)
    timezone = models.CharField(max_length=3)

    @property
    def message_count_success(self):
        return Message.objects.filter(client=self.id, status='OK').count()

    @property
    def message_count_fail(self):
        return Message.objects.filter(~Q(status='OK'), client=self.id).count()

    def __str__(self):
        return str(self.id)


class MessageQueue(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    start_date = models.DateTimeField()
    message_text = models.CharField(max_length=500)
    client_filter = models.CharField(max_length=50)
    end_date = models.DateTimeField()

    @property
    def message_count_success(self):
        return Message.objects.filter(queue=self.id, status='OK').count()

    @property
    def message_count_fail(self):
        return Message.objects.filter(~Q(status='OK'), queue=self.id).count()

    def __str__(self):
        return str(self.id)


class Message(models.Model):
    created = models.DateTimeField()
    status = models.CharField(null=True, max_length=20)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='messages')
    queue = models.ForeignKey(MessageQueue, on_delete=models.CASCADE, related_name='messages')

    def __str__(self):
        return str(self.id)
