from rest_framework import serializers
from django.core.exceptions import BadRequest
from .models import MessageQueue, Client, Message


class GetMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class GetQueueSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageQueue
        fields = (
            'id', 'start_date', 'end_date', 'message_text', 'client_filter', 'message_count_success',
            'message_count_fail')


class GetClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'phone', 'operator', 'tag', 'timezone',)


class RetrieveQueueSerializer(serializers.ModelSerializer):
    messages = GetMessageSerializer(many=True)

    class Meta:
        model = MessageQueue
        fields = (
            'id', 'start_date', 'end_date', 'message_text', 'client_filter', 'message_count_success',
            'message_count_fail', 'messages')


class RetrieveClientSerializer(serializers.ModelSerializer):
    messages = GetMessageSerializer(many=True)

    class Meta:
        model = Client
        fields = ('id', 'phone', 'operator', 'tag', 'timezone', 'message_count_success',
                  'message_count_fail', 'messages')
