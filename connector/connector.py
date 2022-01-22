from django.http import JsonResponse
from requests import Session
from zeep import Client, Transport
from xml.etree.ElementTree import fromstring

SANDBOX_URL = 'https://wyszukiwarkaregontest.stat.gov.pl/wsBIR/wsdl/UslugaBIRzewnPubl-ver11-test.wsdl'
SANDBOX_PASSWORD = 'abcde12345abcde12345'


class GUSConnector:

    def __init__(self, nip):
        self.nip = nip
        self.login_key = 'abcde12345abcde12345'
        self.headers = {}
        transport = Transport(session=Session())
        transport.session.headers = self.headers
        self.client = Client(SANDBOX_URL, transport=transport)
        self.session_key = None
        self.data_dict = None

    def run(self):
        self.login()
        self.get_company_data()
        self.logout()

    def login(self):
        session_key = self.client.service.Zaloguj(
            pKluczUzytkownika=self.login_key
        )
        self.session_key = session_key
        self.headers.update({"sid": self.session_key})

    def get_company_data(self):
        data = self.client.service.DaneSzukajPodmioty(pParametryWyszukiwania={'Nip': self.nip})
        self.data_dict = {info.tag: "" if info.text is None else info.text for info in fromstring(data)[0]}

    def logout(self):
        self.client.service.Wyloguj(pIdentyfikatorSesji=self.session_key)
