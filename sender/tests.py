import datetime

import pytz
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from datetime import date
from sender.models import *

# Create your tests here.

class SenderTestCase(APITestCase):
    def setUp(self):
        tz = pytz.timezone('Europe/Moscow')
        timestamp = tz.localize(datetime.datetime.now())
        client1 = Client.objects.create(phone='79001111111', tag='no tag', operator='900', timezone='UTC')
        client2 = Client.objects.create(phone='79002222222', tag='some tag', operator='900', timezone='UTC')
        client3 = Client.objects.create(id='65563abc-d88e-4fe0-8ceb-c575d282920f',
                                        phone='76663333333', tag='some tag', operator='666', timezone='UTC')
        queue1 = MessageQueue.objects.create(id='33a6dda6-7ae6-4c0a-be03-e3c3be90ff83',
                                             start_date=timestamp, end_date=timestamp + datetime.timedelta(hours=10),
                                             message_text="some normal text", client_filter="900")
        message1 = Message.objects.create(created=timestamp, status='OK', queue=queue1,
                                          client=client3)
        message2 = Message.objects.create(created=timestamp, status='not OK', queue=queue1,
                                          client=client3)


    def test_get_client(self):
        resp = self.client.get(reverse('client-detail', args=['65563abc-d88e-4fe0-8ceb-c575d282920f']))
        self.assertEqual(status.HTTP_200_OK, resp.status_code)
        self.assertEqual(resp.data['phone'], '76663333333')
        self.assertEqual(resp.data['tag'], 'some tag')
        self.assertEqual(resp.data['operator'], '666')
        self.assertEqual(resp.data['timezone'], 'UTC')
