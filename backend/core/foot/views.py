from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Foot
from .serialazers import FootSerializer


class FootListView(APIView):
    def get(self, request, *args, **kwargs):
        foots = Foot.objects.all()[0:4]
        serializer = FootSerializer(foots, many=True)
        return Response(serializer.data)


class FootDetailView(APIView):
    def get(self, request, foot_id, *args, **kwargs):
        foot = get_object_or_404(Foot, id=foot_id)
        serializer = FootSerializer(foot)
        return Response(serializer.data)
