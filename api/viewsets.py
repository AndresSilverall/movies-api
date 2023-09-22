from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers import UserSerializer


def test_viewset(request):
    user = {
        "name": "andres"
    }
    return Response(data=user)