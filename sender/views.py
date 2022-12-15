import datetime
from wsgiref import headers

from django.db.models import Q
from rest_framework import viewsets, status
from rest_framework.response import Response
from sender.serializers import *
from rest_framework.response import Response
from sender import tasks
import pytz
from rest_framework import serializers


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = GetClientSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = RetrieveClientSerializer(instance)
        return Response(serializer.data)


class QueueViewSet(viewsets.ModelViewSet):
    queryset = MessageQueue.objects.all()
    serializer_class = GetQueueSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = RetrieveQueueSerializer(instance)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        tz = pytz.timezone('Europe/Moscow')
        serializer.is_valid(raise_exception=True)
        queue = serializer.save()

        clients = Client.objects.filter(Q(tag=queue.client_filter) | Q(operator=queue.client_filter))

        for item in clients:
            timestamp = tz.localize(datetime.datetime.now())
            q = Message.objects.create(created=timestamp, client_id=item.id, queue_id=queue.id)
            q.save()
            body = {'id': q.id, 'phone': item.phone, 'text': queue.message_text}
            msgid = str(q.id)
            if queue.end_date > timestamp:
                if queue.start_date > timestamp:
                    tasks.send_queue.apply_async([body, msgid], eta=queue.start_date)
                else:
                    tasks.send_queue.delay(body, msgid)
            else:
                break

        return Response({'queue': queue.id}, status=status.HTTP_201_CREATED)
