import datetime as dt

from django.test import TestCase
from petapp.models import *

class ItemsTest(TestCase):
    def setUp(self):
        Item.objects.create(name="Karma dla psów", photo_url="url", create_date=dt.datetime.now(), expiration_date=None, description="Jakis opis, super dobrej karmy dla psiaków", brand_id=1, type_id=1)
