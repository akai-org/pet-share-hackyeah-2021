from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    avatar_url = models.TextField(default=None)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    is_organization = models.BooleanField()


class Message(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=None)
    content = models.TextField()


class ItemBrand(models.Model):
    name = models.CharField(max_length=50)


class ItemType(models.Model):
    name = models.CharField(max_length=50)


class Item(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(default=None)
    brand_id = models.ForeignKey(ItemBrand, on_delete=models.DO_NOTHING, default=None)
    type_id = models.ForeignKey(ItemType, on_delete=models.DO_NOTHING, default=None)


class ItemNeed(models.Model):
    item_id = models.ForeignKey(Item, on_delete=models.DO_NOTHING, default=None)
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=None)
    description = models.TextField(default=None)
    amount = models.IntegerField()
    brand_id = models.ForeignKey(ItemBrand, on_delete=models.DO_NOTHING, default=None)
    type_id = models.ForeignKey(ItemType, on_delete=models.DO_NOTHING, default=None)


class Listing(models.Model):
    item_id = models.ForeignKey(Item, on_delete=models.DO_NOTHING, default=None)
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=None)
    price = models.FloatField()
    posted = models.BooleanField()
