import json
from celery import shared_task
from sender.sender_api_properties import *
from sender.models import Client, Message, MessageQueue
import requests


@shared_task
def send_queue(*args, **kwargs):
    body = args[0]
    msgid = args[1]
    url = api + msgid
    try:
        response = requests.post(url, headers={'Authorization': 'Bearer {}'.format(token)}, json=body)
        response_dict = json.loads(response.text)
        q = Message.objects.get(id=msgid)
        q.status = response_dict['message']
        q.save()
    except Exception as e:
        q = Message.objects.get(id=msgid)
        q.status = str(e)
        q.save()




