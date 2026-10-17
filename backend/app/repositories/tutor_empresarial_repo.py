from app.core.database import Database
from app.models.tutor_empresarial import TutorEmpresarial


class TutorEmpresarialRepository:

    def __init__(self):
        self.db = Database()

    def obtener_todos(self):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM tutores_empresariales ORDER BY tutor_empresarial_id ASC;")
        registros = cursor.fetchall()
        conn.close()

        return registros

    def obtener_por_id(self, tutor_empresarial_id: int):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM tutores_empresariales WHERE tutor_empresarial_id = %s;",
            (tutor_empresarial_id,)
        )
        registro = cursor.fetchone()
        conn.close()

        return registro

    def obtener_por_empresa(self, empresa_id: int):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM tutores_empresariales WHERE empresa_id = %s ORDER BY tutor_empresarial_id ASC;",
            (empresa_id,)
        )
        registros = cursor.fetchall()
        conn.close()

        return registros

    def crear(self, tutor: TutorEmpresarial):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        query = """
            INSERT INTO tutores_empresariales
            (documento, nombres, apellidos, correo, telefono, cargo, empresa_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            RETURNING tutor_empresarial_id;
        """

        cursor.execute(query, (
            tutor.documento,
            tutor.nombres,
            tutor.apellidos,
            tutor.correo,
            tutor.telefono,
            tutor.cargo,
            tutor.empresa_id
        ))

        nuevo_id = cursor.fetchone()["tutor_empresarial_id"]
        conn.commit()
        conn.close()

        return nuevo_id

    def actualizar(self, tutor_empresarial_id: int, tutor: TutorEmpresarial):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        query = """
            UPDATE tutores_empresariales
            SET documento = %s,
                nombres = %s,
                apellidos = %s,
                correo = %s,
                telefono = %s,
                cargo = %s,
                empresa_id = %s
            WHERE tutor_empresarial_id = %s
            RETURNING tutor_empresarial_id;
        """

        cursor.execute(query, (
            tutor.documento,
            tutor.nombres,
            tutor.apellidos,
            tutor.correo,
            tutor.telefono,
            tutor.cargo,
            tutor.empresa_id,
            tutor_empresarial_id
        ))

        actualizado = cursor.fetchone()
        conn.commit()
        conn.close()

        return actualizado is not None

    def eliminar(self, tutor_empresarial_id: int):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM tutores_empresariales WHERE tutor_empresarial_id = %s RETURNING tutor_empresarial_id;",
            (tutor_empresarial_id,)
        )

        eliminado = cursor.fetchone()
        conn.commit()
        conn.close()

        return eliminado is not None
