from rest_framework.decorators import api_view
from rest_framework.response import Response

from petapp.models import *


@api_view(http_method_names=['GET'])
def item_types(request):
    return Response(ItemType.objects.all().values())


@api_view(http_method_names=['GET', 'POST'])
def profiles(request):
    if request.method == 'GET':
        return Response(Profile.objects.all().values())
    else:
        profile = request.data
        user = User(**(profile['user']))
        username_exists = len(User.objects.get(username=user.username)) > 0
        if not username_exists:
            user.save()
            profile['user'] = user
            profile = Profile.objects.create(**profile)
            return profile
        return Response()
