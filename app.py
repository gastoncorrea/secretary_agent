from agents.database_agent import DatabaseAgent

if __name__ == "__main__":
    db_agent = DatabaseAgent()

    print("=== Insertando terapeuta ===")
    terapeuta_id = db_agent.crear_terapeuta(
        nombre="Luis",
        apellido="Gómez",
        email="lgomez@example.com",
        terapia="Fonoaudiología"
    )
    print("Nuevo terapeuta ID:", terapeuta_id)

    print("\n=== Buscando terapeuta ===")
    resultado = db_agent.buscar_terapeuta("lgomez@example.com")
    print(resultado)

    print("\n=== Listando terapeutas ===")
    print(db_agent.listar())
