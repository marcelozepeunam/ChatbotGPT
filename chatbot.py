import os 
import openai
import spacy
from dotenv import load_dotenv

#Importamos bibliotecas y configuramos la clave 
load_dotenv()
api_key=os.getenv("OPENAI_API_KEY")
openai.api_key=api_key

#Función para peticiones
def preguntar_chat_gpt(prompt, modelo="text-davinci-002"):
    respuesta=openai.Completion.create(
        engine=modelo,
        prompt=prompt,
        n=1,
        max_tokens=150,
        temperature=0.9
    )
    return respuesta.choices[0].text.strip()

#Funcionamiento básico
print('Bienvenido a nuestro chatbot básico. Escribe "salir" cuando quieras terminar')
while True:
    ingreso_usuario=input("\nTú: ")
    if ingreso_usuario.lower()=="salir":
        print("Hasta luego =D")
        break
    
    else:
        prompt=(f"El usaurio pregunta: {ingreso_usuario}\nChatGPT responde: ")
        respuesta_gpt=preguntar_chat_gpt(prompt)
        print(f"Chatbot: {respuesta_gpt}")

#Ejecución de chatbot
preguntar_chat_gpt()



