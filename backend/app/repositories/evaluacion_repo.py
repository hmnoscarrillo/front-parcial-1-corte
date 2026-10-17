from app.core.database import Database
from app.models.evaluacion import Evaluacion


class EvaluacionRepository:

    def __init__(self):
        self.db = Database()

    def obtener_todos(self):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM evaluaciones ORDER BY evaluacion_id ASC;")
        registros = cursor.fetchall()
        conn.close()

        return registros

    def obtener_por_id(self, evaluacion_id: int):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM evaluaciones WHERE evaluacion_id = %s;",
            (evaluacion_id,)
        )
        registro = cursor.fetchone()
        conn.close()

        return registro

    def obtener_por_practica(self, practica_id: int):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM evaluaciones WHERE practica_id = %s ORDER BY evaluacion_id ASC;",
            (practica_id,)
        )
        registros = cursor.fetchall()
        conn.close()

        return registros

    def crear(self, evaluacion: Evaluacion):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        query = """
            INSERT INTO evaluaciones
            (practica_id, fecha_evaluacion, evaluador, nota_academica, nota_empresarial, nota_final, comentarios)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            RETURNING evaluacion_id;
        """

        cursor.execute(query, (
            evaluacion.practica_id,
            evaluacion.fecha_evaluacion,
            evaluacion.evaluador,
            evaluacion.nota_academica,
            evaluacion.nota_empresarial,
            evaluacion.nota_final,
            evaluacion.comentarios
        ))

        nuevo_id = cursor.fetchone()["evaluacion_id"]
        conn.commit()
        conn.close()

        return nuevo_id

    def actualizar(self, evaluacion_id: int, evaluacion: Evaluacion):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        query = """
            UPDATE evaluaciones
            SET practica_id = %s,
                fecha_evaluacion = %s,
                evaluador = %s,
                nota_academica = %s,
                nota_empresarial = %s,
                nota_final = %s,
                comentarios = %s
            WHERE evaluacion_id = %s
            RETURNING evaluacion_id;
        """

        cursor.execute(query, (
            evaluacion.practica_id,
            evaluacion.fecha_evaluacion,
            evaluacion.evaluador,
            evaluacion.nota_academica,
            evaluacion.nota_empresarial,
            evaluacion.nota_final,
            evaluacion.comentarios,
            evaluacion_id
        ))

        actualizado = cursor.fetchone()
        conn.commit()
        conn.close()

        return actualizado is not None

    def eliminar(self, evaluacion_id: int):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM evaluaciones WHERE evaluacion_id = %s RETURNING evaluacion_id;",
            (evaluacion_id,)
        )

        eliminado = cursor.fetchone()
        conn.commit()
        conn.close()

        return eliminado is not None
