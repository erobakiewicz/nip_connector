# NIP Connector

### Basic implementation of GUS REGON nip identifier for companies.


## Instalation

Using docker just run `docker-compose up`.

To install project locally using pipenv type `pipenv install` in root dir. Set environment variables
DEBUG, SECRET_KEY and DATABASE_URL.

## Endpoints

There is only one endpoint `/api/v1/<str:nip>/` which returns JSON info about company.