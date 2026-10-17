from app.core.database import Database
from app.models.tutor_academico import TutorAcademico


class TutorAcademicoRepository:

    def __init__(self):
        self.db = Database()

    def obtener_todos(self):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM tutores_academicos ORDER BY tutor_academico_id ASC;")
        registros = cursor.fetchall()
        conn.close()

        return registros

    def obtener_por_id(self, tutor_academico_id: int):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM tutores_academicos WHERE tutor_academico_id = %s;",
            (tutor_academico_id,)
        )
        registro = cursor.fetchone()
        conn.close()

        return registro

    def obtener_por_programa(self, programa_id: int):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM tutores_academicos WHERE programa_id = %s ORDER BY tutor_academico_id ASC;",
            (programa_id,)
        )
        registros = cursor.fetchall()
        conn.close()

        return registros

    def crear(self, tutor: TutorAcademico):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        query = """
            INSERT INTO tutores_academicos
            (documento, nombres, apellidos, correo, telefono, cargo, programa_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            RETURNING tutor_academico_id;
        """

        cursor.execute(query, (
            tutor.documento,
            tutor.nombres,
            tutor.apellidos,
            tutor.correo,
            tutor.telefono,
            tutor.cargo,
            tutor.programa_id
        ))

        nuevo_id = cursor.fetchone()["tutor_academico_id"]
        conn.commit()
        conn.close()

        return nuevo_id

    def actualizar(self, tutor_academico_id: int, tutor: TutorAcademico):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        query = """
            UPDATE tutores_academicos
            SET documento = %s,
                nombres = %s,
                apellidos = %s,
                correo = %s,
                telefono = %s,
                cargo = %s,
                programa_id = %s
            WHERE tutor_academico_id = %s
            RETURNING tutor_academico_id;
        """

        cursor.execute(query, (
            tutor.documento,
            tutor.nombres,
            tutor.apellidos,
            tutor.correo,
            tutor.telefono,
            tutor.cargo,
            tutor.programa_id,
            tutor_academico_id
        ))

        actualizado = cursor.fetchone()
        conn.commit()
        conn.close()

        return actualizado is not None

    def eliminar(self, tutor_academico_id: int):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM tutores_academicos WHERE tutor_academico_id = %s RETURNING tutor_academico_id;",
            (tutor_academico_id,)
        )

        eliminado = cursor.fetchone()
        conn.commit()
        conn.close()

        return eliminado is not None
