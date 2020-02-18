# Empty
"""Methods for altering the file tables"""
from app.infrastructure import file_repository


def get_file(nombre):
    """Get a file"""
    return file_repository.get_file(nombre)


def post_file(nombre, contenido):
    """Create an new file"""
    return file_repository.post_file(nombre, contenido)
