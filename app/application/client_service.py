# Empty
"""Methods for altering the file tables"""
from app.infrastructure import client_repository


def get(id):
    """Get a client"""
    print('client_service.get')
    return client_repository.get_client(id)


def post(client):
    """Get a client"""
    print('client_service.post')
    # TODO: calculate if the client is an adult and save it on isAdult
    return client_repository.create_client(client)
