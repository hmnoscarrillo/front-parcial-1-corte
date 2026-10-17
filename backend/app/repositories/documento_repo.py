from app.core.database import Database
from app.models.documento import Documento


class DocumentoRepository:

    def __init__(self):
        self.db = Database()

    def obtener_todos(self):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM documentos ORDER BY documento_id ASC;")
        registros = cursor.fetchall()
        conn.close()

        return registros

    def obtener_por_id(self, documento_id: int):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM documentos WHERE documento_id = %s;",
            (documento_id,)
        )
        registro = cursor.fetchone()
        conn.close()

        return registro

    def obtener_por_practica(self, practica_id: int):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM documentos WHERE practica_id = %s ORDER BY documento_id ASC;",
            (practica_id,)
        )
        registros = cursor.fetchall()
        conn.close()

        return registros

    def crear(self, documento: Documento):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        query = """
            INSERT INTO documentos
            (practica_id, nombre_documento, tipo_documento, fecha_subida, ruta_archivo, estado)
            VALUES (%s, %s, %s, %s, %s, %s)
            RETURNING documento_id;
        """

        cursor.execute(query, (
            documento.practica_id,
            documento.nombre_documento,
            documento.tipo_documento,
            documento.fecha_subida,
            documento.ruta_archivo,
            documento.estado
        ))

        nuevo_id = cursor.fetchone()["documento_id"]
        conn.commit()
        conn.close()

        return nuevo_id

    def actualizar(self, documento_id: int, documento: Documento):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        query = """
            UPDATE documentos
            SET practica_id = %s,
                nombre_documento = %s,
                tipo_documento = %s,
                fecha_subida = %s,
                ruta_archivo = %s,
                estado = %s
            WHERE documento_id = %s
            RETURNING documento_id;
        """

        cursor.execute(query, (
            documento.practica_id,
            documento.nombre_documento,
            documento.tipo_documento,
            documento.fecha_subida,
            documento.ruta_archivo,
            documento.estado,
            documento_id
        ))

        actualizado = cursor.fetchone()
        conn.commit()
        conn.close()

        return actualizado is not None

    def eliminar(self, documento_id: int):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM documentos WHERE documento_id = %s RETURNING documento_id;",
            (documento_id,)
        )

        eliminado = cursor.fetchone()
        conn.commit()
        conn.close()

        return eliminado is not None
