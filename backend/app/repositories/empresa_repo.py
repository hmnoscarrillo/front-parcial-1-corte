from app.core.database import Database
from app.models.empresa import Empresa


class EmpresaRepository:

    def __init__(self):
        self.db = Database()

    def obtener_todos(self):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM empresas ORDER BY empresa_id ASC;")
        registros = cursor.fetchall()
        conn.close()

        return registros

    def obtener_por_id(self, empresa_id: int):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM empresas WHERE empresa_id = %s;",
            (empresa_id,)
        )
        registro = cursor.fetchone()
        conn.close()

        return registro

    def crear(self, empresa: Empresa):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        query = """
            INSERT INTO empresas
            (nit, nombre, sector, ciudad, direccion, telefono, correo, estado)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            RETURNING empresa_id;
        """

        cursor.execute(query, (
            empresa.nit,
            empresa.nombre,
            empresa.sector,
            empresa.ciudad,
            empresa.direccion,
            empresa.telefono,
            empresa.correo,
            empresa.estado
        ))

        nuevo_id = cursor.fetchone()["empresa_id"]
        conn.commit()
        conn.close()

        return nuevo_id

    def actualizar(self, empresa_id: int, empresa: Empresa):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        query = """
            UPDATE empresas
            SET nit = %s,
                nombre = %s,
                sector = %s,
                ciudad = %s,
                direccion = %s,
                telefono = %s,
                correo = %s,
                estado = %s
            WHERE empresa_id = %s
            RETURNING empresa_id;
        """

        cursor.execute(query, (
            empresa.nit,
            empresa.nombre,
            empresa.sector,
            empresa.ciudad,
            empresa.direccion,
            empresa.telefono,
            empresa.correo,
            empresa.estado,
            empresa_id
        ))

        actualizado = cursor.fetchone()
        conn.commit()
        conn.close()

        return actualizado is not None

    def eliminar(self, empresa_id: int):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM empresas WHERE empresa_id = %s RETURNING empresa_id;",
            (empresa_id,)
        )

        eliminado = cursor.fetchone()
        conn.commit()
        conn.close()

        return eliminado is not None
