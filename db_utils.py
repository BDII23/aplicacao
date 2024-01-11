import psycopg2
from django.conf import settings

class DBManager:
    def __init__(self, db_alias='pgdb'):
        db_config = settings.DATABASES.get(db_alias, {})
        self.conn = psycopg2.connect(
            host=db_config.get('HOST', ''),
            database=db_config.get('NAME', ''),
            user=db_config.get('USER', ''),
            password=db_config.get('PASSWORD', '')
        )
        self.cursor = self.conn.cursor()

    def execute_query(self, query):
        self.cursor.execute(query)
        self.conn.commit()

    def fetch_all(self):
        return self.cursor.fetchall()

    def close_connection(self):
        self.cursor.close()
        self.conn.close()

# Exemplo de uso
# Cria uma instância usando as configurações do banco de dados 'pgdb'
db_manager_pgdb = DBManager(db_alias='pgdb')

# Cria uma instância usando as configurações do banco de dados 'mgdb'
db_manager_mgdb = DBManager(db_alias='mgdb')
