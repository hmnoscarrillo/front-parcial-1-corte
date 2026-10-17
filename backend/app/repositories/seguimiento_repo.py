from app.core.database import Database
from app.models.seguimiento import Seguimiento


class SeguimientoRepository:

    def __init__(self):
        self.db = Database()

    def obtener_todos(self):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM seguimientos ORDER BY seguimiento_id ASC;")
        registros = cursor.fetchall()
        conn.close()

        return registros

    def obtener_por_id(self, seguimiento_id: int):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM seguimientos WHERE seguimiento_id = %s;",
            (seguimiento_id,)
        )
        registro = cursor.fetchone()
        conn.close()

        return registro

    def obtener_por_practica(self, practica_id: int):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM seguimientos WHERE practica_id = %s ORDER BY seguimiento_id ASC;",
            (practica_id,)
        )
        registros = cursor.fetchall()
        conn.close()

        return registros

    def crear(self, seguimiento: Seguimiento):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        query = """
            INSERT INTO seguimientos
            (practica_id, tutor_academico_id, fecha_seguimiento, tipo, observaciones, estado)
            VALUES (%s, %s, %s, %s, %s, %s)
            RETURNING seguimiento_id;
        """

        cursor.execute(query, (
            seguimiento.practica_id,
            seguimiento.tutor_academico_id,
            seguimiento.fecha_seguimiento,
            seguimiento.tipo,
            seguimiento.observaciones,
            seguimiento.estado
        ))

        nuevo_id = cursor.fetchone()["seguimiento_id"]
        conn.commit()
        conn.close()

        return nuevo_id

    def actualizar(self, seguimiento_id: int, seguimiento: Seguimiento):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        query = """
            UPDATE seguimientos
            SET practica_id = %s,
                tutor_academico_id = %s,
                fecha_seguimiento = %s,
                tipo = %s,
                observaciones = %s,
                estado = %s
            WHERE seguimiento_id = %s
            RETURNING seguimiento_id;
        """

        cursor.execute(query, (
            seguimiento.practica_id,
            seguimiento.tutor_academico_id,
            seguimiento.fecha_seguimiento,
            seguimiento.tipo,
            seguimiento.observaciones,
            seguimiento.estado,
            seguimiento_id
        ))

        actualizado = cursor.fetchone()
        conn.commit()
        conn.close()

        return actualizado is not None

    def eliminar(self, seguimiento_id: int):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM seguimientos WHERE seguimiento_id = %s RETURNING seguimiento_id;",
            (seguimiento_id,)
        )

        eliminado = cursor.fetchone()
        conn.commit()
        conn.close()

        return eliminado is not None
