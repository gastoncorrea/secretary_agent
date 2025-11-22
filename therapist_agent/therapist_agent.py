from google.adk.models.google_llm import Gemini
from google.adk.agents import LlmAgent
from google.adk.tools import FunctionTool
from google.adk.tools.tool_context import ToolContext
from core.agent_config import retry_config


# Agente terapeuta simple para la prueba
therapist_agent = LlmAgent(
    name='therapist_agent',
    model=Gemini(model='gemini-2.5-flash-lite', retry_options=retry_config),
    instruction="Eres un agente especializado en gestión de terapeutas. Cuando un terapeuta quiera actualizar sus datos, responde con los campos necesarios: nombre, especialidad, años de experiencia, email, teléfono, biografía y horarios disponibles.",
    output_key="therapist_response"
)