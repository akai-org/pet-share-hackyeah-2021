import json
import profile

from rest_framework.decorators import api_view
from rest_framework.response import Response

from petapp.models import *


@api_view(http_method_names=['GET'])
def get_all_item_types(request):
    return Response(ItemType.objects.all().values())
