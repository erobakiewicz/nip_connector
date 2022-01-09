from requests import Session
from zeep import Client, Transport
from django.http import HttpResponse

class GUSConnector:
    SANDBOX_URL = 'https://wyszukiwarkaregontest.stat.gov.pl/wsBIR/wsdl/UslugaBIRzewnPubl-ver11-test.wsdl'
    SANDBOX_PASSWORD = 'abcde12345abcde12345'

    def __init__(self, nip):
        SANDBOX_URL = 'https://wyszukiwarkaregontest.stat.gov.pl/wsBIR/wsdl/UslugaBIRzewnPubl-ver11-test.wsdl'
        self.nip = nip
        self.login_key = 'abcde12345abcde12345'
        transport = Transport(session=Session())
        transport.session.headers = {}
        self.client = Client(SANDBOX_URL, transport=transport)
        self.session_key = None

    def run(self):
        self.login()
        self.logout()

    def login(self):
        session_key = self.client.service.Zaloguj(
            pKluczUzytkownika=self.login_key
        )
        print(session_key)
        self.session_key = session_key

    def logout(self):
        self.client.service.Wyloguj(pIdentyfikatorSesji=self.session_key)











