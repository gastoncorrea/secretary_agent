from tools.database import DatabaseManager

db = DatabaseManager()
db.connect()

def crear_terapeuta(nombre, apellido, email, terapia):
    sql = """
        INSERT INTO therapists (nombre, apellido, email, terapia)
        VALUES (%s, %s, %s, %s)
    """
    return db.execute(sql, (nombre, apellido, email, terapia))

def obtener_terapeuta_por_email(email):
    sql = "SELECT * FROM therapists WHERE email = %s"
    return db.query(sql, (email,))

def listar_terapeutas():
    sql = "SELECT * FROM therapists"
    return db.query(sql)
