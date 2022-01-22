from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView

from connector.connector import GUSConnector


class GUSConnectorAPIView(APIView):

    def get(self, request, *args, **kwargs):
        nip = self.kwargs.get("nip")
        gus_connector = GUSConnector(nip)
        gus_connector.run()
        data = gus_connector.data_dict
        return JsonResponse(data)
