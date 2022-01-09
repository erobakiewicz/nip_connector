from django.shortcuts import render
from rest_framework.views import APIView

from connector.connector import GUSConnector


class GUSConnectorAPIView(APIView):

    def get(self, request, *args, **kwargs):
        nip = self.kwargs.get("nip")
        gus_connector = GUSConnector(nip)
        return gus_connector.run()
