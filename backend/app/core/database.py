import os
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

# Carga las variables del archivo .env al entorno de Python
load_dotenv()


class Database:
    def __init__(self):
        self.host = os.getenv("DB_HOST")
        self.database = os.getenv("DB_NAME")
        self.user = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASSWORD")
        self.port = os.getenv("DB_PORT")

    def get_connection(self):
        missing = [
            name for name, value in {
                "DB_HOST": self.host,
                "DB_NAME": self.database,
                "DB_USER": self.user,
                "DB_PASSWORD": self.password,
                "DB_PORT": self.port,
            }.items() if not value
        ]
        if missing:
            raise RuntimeError("Faltan variables de base de datos: " + ", ".join(missing))

        return psycopg2.connect(
            host=self.host,
            database=self.database,
            user=self.user,
            password=self.password,
            port=self.port,
            sslmode="require",
            connect_timeout=10,
            cursor_factory=RealDictCursor
        )
