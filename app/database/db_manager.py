from django.db import connection
from constants import DATABASE_MG, DATABASE_PG

def get_pg_cursor():
    return connection[DATABASE_PG].cursor()

def get_mg_cursor():
    return connection[DATABASE_MG].cursor()