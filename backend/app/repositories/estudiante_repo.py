from app.core.database import Database
from app.models.estudiante import Estudiante


class EstudianteRepository:

    def __init__(self):
        self.db = Database()

    def obtener_todos(self):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM estudiantes ORDER BY estudiante_id ASC;")
        registros = cursor.fetchall()
        conn.close()

        return registros

    def obtener_por_id(self, estudiante_id: int):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM estudiantes WHERE estudiante_id = %s;",
            (estudiante_id,)
        )
        registro = cursor.fetchone()
        conn.close()

        return registro

    def obtener_por_programa(self, programa_id: int):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM estudiantes WHERE programa_id = %s ORDER BY estudiante_id ASC;",
            (programa_id,)
        )
        registros = cursor.fetchall()
        conn.close()

        return registros

    def crear(self, estudiante: Estudiante):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        query = """
            INSERT INTO estudiantes
            (documento, nombres, apellidos, correo, telefono, semestre, programa_id, estado)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            RETURNING estudiante_id;
        """

        cursor.execute(query, (
            estudiante.documento,
            estudiante.nombres,
            estudiante.apellidos,
            estudiante.correo,
            estudiante.telefono,
            estudiante.semestre,
            estudiante.programa_id,
            estudiante.estado
        ))

        nuevo_id = cursor.fetchone()["estudiante_id"]
        conn.commit()
        conn.close()

        return nuevo_id

    def actualizar(self, estudiante_id: int, estudiante: Estudiante):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        query = """
            UPDATE estudiantes
            SET documento = %s,
                nombres = %s,
                apellidos = %s,
                correo = %s,
                telefono = %s,
                semestre = %s,
                programa_id = %s,
                estado = %s
            WHERE estudiante_id = %s
            RETURNING estudiante_id;
        """

        cursor.execute(query, (
            estudiante.documento,
            estudiante.nombres,
            estudiante.apellidos,
            estudiante.correo,
            estudiante.telefono,
            estudiante.semestre,
            estudiante.programa_id,
            estudiante.estado,
            estudiante_id
        ))

        actualizado = cursor.fetchone()
        conn.commit()
        conn.close()

        return actualizado is not None

    def eliminar(self, estudiante_id: int):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM estudiantes WHERE estudiante_id = %s RETURNING estudiante_id;",
            (estudiante_id,)
        )

        eliminado = cursor.fetchone()
        conn.commit()
        conn.close()

        return eliminado is not None
