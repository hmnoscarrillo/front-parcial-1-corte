from app.core.database import Database
from app.models.convenio import Convenio


class ConvenioRepository:

    def __init__(self):
        self.db = Database()

    def obtener_todos(self):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM convenios ORDER BY convenio_id ASC;")
        registros = cursor.fetchall()
        conn.close()

        return registros

    def obtener_por_id(self, convenio_id: int):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM convenios WHERE convenio_id = %s;",
            (convenio_id,)
        )
        registro = cursor.fetchone()
        conn.close()

        return registro

    def obtener_por_empresa(self, empresa_id: int):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM convenios WHERE empresa_id = %s ORDER BY convenio_id ASC;",
            (empresa_id,)
        )
        registros = cursor.fetchall()
        conn.close()

        return registros

    def crear(self, convenio: Convenio):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        query = """
            INSERT INTO convenios
            (codigo, empresa_id, programa_id, fecha_inicio, fecha_fin, estado)
            VALUES (%s, %s, %s, %s, %s, %s)
            RETURNING convenio_id;
        """

        cursor.execute(query, (
            convenio.codigo,
            convenio.empresa_id,
            convenio.programa_id,
            convenio.fecha_inicio,
            convenio.fecha_fin,
            convenio.estado
        ))

        nuevo_id = cursor.fetchone()["convenio_id"]
        conn.commit()
        conn.close()

        return nuevo_id

    def actualizar(self, convenio_id: int, convenio: Convenio):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        query = """
            UPDATE convenios
            SET codigo = %s,
                empresa_id = %s,
                programa_id = %s,
                fecha_inicio = %s,
                fecha_fin = %s,
                estado = %s
            WHERE convenio_id = %s
            RETURNING convenio_id;
        """

        cursor.execute(query, (
            convenio.codigo,
            convenio.empresa_id,
            convenio.programa_id,
            convenio.fecha_inicio,
            convenio.fecha_fin,
            convenio.estado,
            convenio_id
        ))

        actualizado = cursor.fetchone()
        conn.commit()
        conn.close()

        return actualizado is not None

    def eliminar(self, convenio_id: int):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM convenios WHERE convenio_id = %s RETURNING convenio_id;",
            (convenio_id,)
        )

        eliminado = cursor.fetchone()
        conn.commit()
        conn.close()

        return eliminado is not None
