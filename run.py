from app import create_app
from app.extensions import db
from sqlalchemy import text  # Importa text de SQLAlchemy

app = create_app()

def test_db_connection():
    """Función para probar la conexión a la base de datos."""
    try:
        # Intenta realizar una consulta simple para verificar la conexión
        with app.app_context():
            result = db.session.execute(text('SELECT 1 FROM DUAL'))  # Usar text() para la consulta
            print("Conexión a la base de datos exitosa:", result.fetchone())
    except Exception as e:
        print("Error al conectar a la base de datos:", e)

if __name__ == "__main__":
    test_db_connection()  # Prueba la conexión antes de ejecutar la app
    app.run(debug=True)

