import os 
import openai
import spacy
from dotenv import load_dotenv

#Importamos bibliotecas y configuramos la clave 
load_dotenv()
api_key=os.getenv("OPENAI_API_KEY")
openai.api_key=api_key

preguntas_anteriores=[]
respuestas_anteriores=[]


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
    conversacion_historica=""
    ingreso_usuario=input("\nTú: ")
    if ingreso_usuario.lower()=="salir":
        print("Hasta luego =D")
        break
    
    else:
        #Mantenemos el contexto de las conversaciones 
        for pregunta, respuesta in zip (preguntas_anteriores, respuestas_anteriores):
            conversacion_historica+=f"El usuario pregunta: {pregunta}\n"
            conversacion_historica+=f"ChatGPT responde: {respuesta}\n"

        prompt=(f"El usaurio pregunta: {ingreso_usuario}\n")
        conversacion_historica+=prompt
        respuesta_gpt=preguntar_chat_gpt(conversacion_historica)
        print(respuesta_gpt)

        preguntas_anteriores.append(ingreso_usuario)
        respuestas_anteriores.append(respuesta_gpt)


#Ejecución de chatbot
preguntar_chat_gpt()



