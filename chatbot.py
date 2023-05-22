import os 
import openai
from dotenv import load_dotenv

load_dotenv()

#Preparamos la petición
api_key=os.getenv("OPENAI_API_KEY")
openai.api_key=api_key

modelo="text-davinci-002"
prompt="¿Cuál es la capital de México?"

#Enviamos una petición
respuesta=openai.Completion.create(
    engine=modelo, #Davinci
    prompt=prompt, #Indicación que se le dara a la IA 
    n=1 #Número de respuestas que queremos recibir
)

#Recibiendo la respuesta 
'''Nota: 
Como recibimos un archivo tipo JSON, debemos darle formato a nuestra respuesta, de la sig manera:
Obtenemos la primera categoria de las respuestas dadas con choices e índice 0
Con el método strip eliminaremos de cualquier string los espacios en blanco que hay antes y después '''
texto_generado=respuesta.choices[0].text.strip()
print(texto_generado)


