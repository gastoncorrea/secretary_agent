from google.adk.agents.llm_agent import Agent
from google.adk.tools import FunctionTool

def get_pacient_schedule():
    """Devuelve los datos necesarios para que un paciente solicite un turno"""
    
    requirements = {
        "accion":"solicitar_turno",
        "campos_requeridos":[
            {
                "campo":"nombre",
                "tipo":"string",
                "descripcion":"Nombre del paciente",
                "ejemplo":"andrea"
                },
            {
                "campo":"apellido",
                "tipo":"string",
                "descripcion":"apellido del paciente",
                "ejemplo":"carrizo"
                },
            {
                "campo":"dni",
                "tipo":"numero",
                "descripcion":"dni del paciente",
                "ejemplo":"33653821"
                },
            {
                "campo":"obra_social",
                "tipo":"string",
                "descripcion":"obra social del paciente",
                "ejemplo":"osde"
                },{
                "field": "fecha_nac",
                "type": "date",
                "description": "Fecha de nacimiento (formato YYYY-MM-DD)",
                "example": "1985-05-15"
            }
        ],
        "optional_fields": [
            {
                "field": "email",
                "type": "string",
                "description": "Email de contacto",
                "example": "maria.gonzalez@email.com"
            },
            {
                "field": "telefono",
                "type": "string",
                "description": "Número de teléfono",
                "example": "+5491112345678"
            },
            {
                "field": "motivo_consulta",
                "type": "string",
                "description": "Breve descripción del motivo de la consulta",
                "example": "Dolor lumbar"
            }
        ],
        "field_descriptions": {
            "nombre": "Nombre de pila del paciente",
            "apellido": "Apellido del paciente", 
            "dni": "Documento sin puntos ni espacios",
            "obra_social": "Nombre de la obra social o 'particular'",
            "fecha_nac": "Fecha en formato año-mes-día",
            "email": "Para confirmación y recordatorios",
            "telefono": "Para contactos urgentes",
            "motivo_consulta": "Ayuda a asignar el profesional adecuado"
        }
    }
    return requirements

therapist_agent = Agent(
    name='therapist',
    model='gemini-2.5-flash-lite',
    instruction="""Estas diseñado para actuar como un asistente del AGENTE COORDINADOR que se llama coordinator.
    El agente coordinator te asignará tareas específicas relacionadas con la gestión de terapeutas que pertencen al centro y 
    vos debes consultar con el agente de datos.
    
    ***ACCIONES***
    1. Devolver al agente coordinador los requerimientos de datos necesarios para completar la solicitud del terapeuta si el agente coordinador lo solicita.
     a) El terapeuta puede solicitar agregar o modificar sus datos personales, devolver campos requeridos y opcionales al agente coordinador y esperar que el agente coordinador solicite al usuario y te brinde esos datos.
    """,
    tools=[FunctionTool(get_pacient_schedule)],
) 