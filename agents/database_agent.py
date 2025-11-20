from tools.therapist_tools import (
    crear_terapeuta,
    obtener_terapeuta_por_email,
    listar_terapeutas
)

class DatabaseAgent:
    def crear_terapeuta(self, nombre, apellido, email, terapia):
        return crear_terapeuta(nombre, apellido, email, terapia)

    def buscar_terapeuta(self, email):
        return obtener_terapeuta_por_email(email)

    def listar(self):
        return listar_terapeutas()