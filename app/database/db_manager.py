from constants import DATABASE_MG, DATABASE_PG
import psycopg2
from django.conf import settings
from pymongo import MongoClient

pg_settings = settings.DATABASES[DATABASE_PG]
pg_connection = psycopg2.connect(
    user=pg_settings['USER'],
    password=pg_settings['PASSWORD'],
    host=pg_settings['HOST'],
    port=pg_settings['PORT'],
    database=pg_settings['NAME']
)

mg_settings = settings.DATABASES[DATABASE_MG]
mg_connection = MongoClient(
    host=mg_settings['HOST'],
    port=mg_settings['PORT']
)


def get_pg_cursor():
    return pg_connection.cursor()

def get_mg_cursor():
    return mg_connection.cursor()
