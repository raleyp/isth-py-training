from adaptor import file_routes as file
from domain.model import Usuario

print('Iniciando')


usuario = Usuario()
usuario.Username = 'marnylopez'
usuario.Nombre = 'Marny'
usuario.Apellido = 'Lopez'

file.create_file('archivo', usuario.provide())
