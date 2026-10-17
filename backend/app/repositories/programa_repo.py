from app.core.database import Database
from app.models.programa import Programa


class ProgramaRepository:

    def __init__(self):
        self.db = Database()

    def obtener_todos(self):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM programas ORDER BY programa_id ASC;")
        registros = cursor.fetchall()
        conn.close()

        return registros

    def obtener_por_id(self, programa_id: int):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM programas WHERE programa_id = %s;",
            (programa_id,)
        )
        registro = cursor.fetchone()
        conn.close()

        return registro

    def crear(self, programa: Programa):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        query = """
            INSERT INTO programas
            (nombre, facultad, nivel, duracion_semestres, estado)
            VALUES (%s, %s, %s, %s, %s)
            RETURNING programa_id;
        """

        cursor.execute(query, (
            programa.nombre,
            programa.facultad,
            programa.nivel,
            programa.duracion_semestres,
            programa.estado
        ))

        nuevo_id = cursor.fetchone()["programa_id"]
        conn.commit()
        conn.close()

        return nuevo_id

    def actualizar(self, programa_id: int, programa: Programa):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        query = """
            UPDATE programas
            SET nombre = %s,
                facultad = %s,
                nivel = %s,
                duracion_semestres = %s,
                estado = %s
            WHERE programa_id = %s
            RETURNING programa_id;
        """

        cursor.execute(query, (
            programa.nombre,
            programa.facultad,
            programa.nivel,
            programa.duracion_semestres,
            programa.estado,
            programa_id
        ))

        actualizado = cursor.fetchone()
        conn.commit()
        conn.close()

        return actualizado is not None

    def eliminar(self, programa_id: int):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM programas WHERE programa_id = %s RETURNING programa_id;",
            (programa_id,)
        )

        eliminado = cursor.fetchone()
        conn.commit()
        conn.close()

        return eliminado is not None
