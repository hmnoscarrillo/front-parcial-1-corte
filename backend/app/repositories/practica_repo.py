from app.core.database import Database
from app.models.practica import Practica


class PracticaRepository:

    def __init__(self):
        self.db = Database()

    def obtener_todos(self):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM practicas ORDER BY practica_id ASC;")
        registros = cursor.fetchall()
        conn.close()

        return registros

    def obtener_por_id(self, practica_id: int):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM practicas WHERE practica_id = %s;",
            (practica_id,)
        )
        registro = cursor.fetchone()
        conn.close()

        return registro

    def obtener_por_estudiante(self, estudiante_id: int):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM practicas WHERE estudiante_id = %s ORDER BY practica_id ASC;",
            (estudiante_id,)
        )
        registros = cursor.fetchall()
        conn.close()

        return registros

    def crear(self, practica: Practica):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        query = """
            INSERT INTO practicas
            (estudiante_id, empresa_id, programa_id, convenio_id, tutor_academico_id, tutor_empresarial_id, cargo, fecha_inicio, fecha_fin, modalidad, estado)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            RETURNING practica_id;
        """

        cursor.execute(query, (
            practica.estudiante_id,
            practica.empresa_id,
            practica.programa_id,
            practica.convenio_id,
            practica.tutor_academico_id,
            practica.tutor_empresarial_id,
            practica.cargo,
            practica.fecha_inicio,
            practica.fecha_fin,
            practica.modalidad,
            practica.estado
        ))

        nuevo_id = cursor.fetchone()["practica_id"]
        conn.commit()
        conn.close()

        return nuevo_id

    def actualizar(self, practica_id: int, practica: Practica):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        query = """
            UPDATE practicas
            SET estudiante_id = %s,
                empresa_id = %s,
                programa_id = %s,
                convenio_id = %s,
                tutor_academico_id = %s,
                tutor_empresarial_id = %s,
                cargo = %s,
                fecha_inicio = %s,
                fecha_fin = %s,
                modalidad = %s,
                estado = %s
            WHERE practica_id = %s
            RETURNING practica_id;
        """

        cursor.execute(query, (
            practica.estudiante_id,
            practica.empresa_id,
            practica.programa_id,
            practica.convenio_id,
            practica.tutor_academico_id,
            practica.tutor_empresarial_id,
            practica.cargo,
            practica.fecha_inicio,
            practica.fecha_fin,
            practica.modalidad,
            practica.estado,
            practica_id
        ))

        actualizado = cursor.fetchone()
        conn.commit()
        conn.close()

        return actualizado is not None

    def eliminar(self, practica_id: int):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM practicas WHERE practica_id = %s RETURNING practica_id;",
            (practica_id,)
        )

        eliminado = cursor.fetchone()
        conn.commit()
        conn.close()

        return eliminado is not None
