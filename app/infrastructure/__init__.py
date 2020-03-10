# Empty
from app.infrastructure.client_repository import clientRepository
import mysql.connector
from app.common import Constants

mydb = mysql.connector.connect(
    host=Constants.MYSQL_HOST,
    user=Constants.MYSQL_DB,
    passwd=Constants.MYSQL_DB,
    database=Constants.MYSQL_DB
)

client_repository = clientRepository(mydb)
