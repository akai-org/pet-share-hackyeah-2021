from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response

from petapp.models import *

@api_view(http_method_names=['GET'])
def get_all_item_types(request):
    return Response(ItemType.objects.all().values())


@api_view(http_method_names=['GET', 'POST'])
def users(request):
    if request.method == 'GET':
        return Response(Profile.objects.all().values())
    else:
        profile = request.data
        print(profile['user'])
        user = User(**(profile['user']))
        if len(User.objects.filter(id=user.id).values()):
            user.save()
        profile['user'] = user
        Profile(**profile).save()
        return Response(Profile.objects.all().values())

@api_view(http_method_names=['GET'])
def items(request):
    if request.method == "GET":
        return Response(Item.objects.all().values())

