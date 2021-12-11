from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar_url = models.URLField()
    address = models.TextField()
    phone = models.CharField(max_length=20)
    is_organization = models.BooleanField()


class Message(models.Model):
    sender_id = models.ForeignKey(Profile, on_delete=models.DO_NOTHING, default=None, related_name='sender')
    recipient_id = models.ForeignKey(Profile, on_delete=models.DO_NOTHING, default=None, related_name='recipient')
    content = models.TextField()


class ItemBrand(models.Model):
    name = models.CharField(max_length=50)


class ItemType(models.Model):
    name = models.CharField(max_length=50)


class Item(models.Model):
    name = models.CharField(max_length=50)
    photo_url = models.URLField()
    post_date = models.DateField()
    expiration_date = models.DateField(default=None)
    description = models.TextField(default=None)
    brand_id = models.ForeignKey(ItemBrand, on_delete=models.DO_NOTHING, default=None)
    type_id = models.ForeignKey(ItemType, on_delete=models.DO_NOTHING, default=None)


class ItemNeed(models.Model):
    item_id = models.ForeignKey(Item, on_delete=models.DO_NOTHING, default=None)
    user_id = models.ForeignKey(Profile, on_delete=models.DO_NOTHING, default=None)
    amount = models.IntegerField()


class ItemListing(models.Model):
    item_id = models.ForeignKey(Item, on_delete=models.DO_NOTHING, default=None)
    user_id = models.ForeignKey(Profile, on_delete=models.DO_NOTHING, default=None)
    price = models.FloatField()
