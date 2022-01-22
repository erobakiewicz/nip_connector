# NIP Connector

### Basic implementation of GUS REGON nip identifier for companies.


## Instalation

To install project locally type `pipenv install` in root dir. Set environment variables
DEBUG, SECRET_KEY and DATABASE_URL.

## Endpoints

There is only one endpoint `/api/v1/<str:nip>/` which returns JSON info about company.