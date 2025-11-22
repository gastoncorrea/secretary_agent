from google.adk.models.google_llm import Gemini
from google.adk.agents import LlmAgent
from google.adk.tools import AgentTool
from core.agent_config import retry_config
from therapist_agent.therapist_agent import therapist_agent


# Agente coordinador principal
root_agent = LlmAgent(
    name='coordinator',
    model=Gemini(model='gemini-2.5-flash-lite', retry_options=retry_config),
    instruction="""
    Eres un coordinador inteligente. Analiza el mensaje del usuario para identificar:
    
    - Si es TERAPEUTA: palabras como "soy terapeuta", "psicólogo", "actualizar mis datos"
    - Si es PACIENTE: palabras como "soy paciente", "mi tratamiento", "mis sesiones"  
    - Si es POTENCIAL_PACIENTE: palabras como "busco terapeuta", "primera consulta"
    
    Si no puedes identificar el tipo, pregunta: "¿Eres terapeuta, paciente o buscas una primera consulta?"
    
    Si identificas que es TERAPEUTA y quiere actualizar datos, usa la herramienta therapist_agent.
    Recibe la respuesta del agente therapist.
    Cuando recibas un `functionResponse`, DEBES:
   - Leer el campo: response.result
   - Responder al usuario utilizando SOLO ese contenido.
   - Nunca quedarte en silencio.
   - No generes un nuevo llamado a herramientas a menos que sea estrictamente necesario
    Para otros casos, responde directamente según el tipo de usuario.
 .

Ejemplo de cómo debes actuar:

Si recibes:
{
  "functionResponse": {
      "response": { "result": "mensaje del agente therapist" }
  }
}

Debes responder al usuario así:

"mensaje del agente therapist"

Nunca ignores functionResponse.
Nunca respondas en blanco.

    Nunca ignores las respuestas de las herramientas.
    """,
    tools=[AgentTool(agent=therapist_agent)],
    output_key="final_answer"
)