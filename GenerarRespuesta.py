import json
import requests
 
#Variables para el Token y la URL del chatbot
TOKEN = "751988420:AAHrzn7RXWxVQQNha0tQUzyouE5lUcPde1g" #Cambialo por tu token
URL = "https://api.telegram.org/bot" + TOKEN + "/"
 
 
 
def update():
    #Llamar al metodo getUpdates del bot
    respuesta = requests.get(URL + "getUpdates")
 
    #Decodificar la respuesta recibida a formato UTF8
    mensajes_js = respuesta.content.decode("utf8")
 
    #Convertir el string de JSON a un diccionario de Python
    mensajes_diccionario = json.loads(mensajes_js)
 
    #Devolver este diccionario
    return mensajes_diccionario
 
 
def leer_mensaje():
 
    #Guardar el diccionario con todos los mensajes recientes
    mensajes = update()
 
    #Calcular el indice del ultimo mensaje recibido
    indice = len(mensajes["result"])-1
 
    #Extraer el texto, nombre de la persona e id del último mensaje recibido
    texto = mensajes["result"][indice]["message"]["text"]
    persona = mensajes["result"][indice]["message"]["from"]["first_name"]
    id_chat = mensajes["result"][indice]["message"]["chat"]["id"]
 
    #Devolver la id, nombre y texto del mensaje
    return id_chat, persona, texto
 
def enviar_mensaje(idchat, texto):
    #Llamar el metodo sendMessage del bot, passando el texto y la id del chat
    requests.get(URL + "sendMessage?text=" + texto + "&chat_id=" + str(idchat))
 
 
#Llamar a la funcion "leer_mensaje()"
idchat, nombre, texto = leer_mensaje()
 
#Generar una respuesta a partir de la informacion del mensaje
if "Hola" in texto:
    texto_respuesta = "Hola, " + nombre + "!"
    enviar_mensaje(idchat, texto_respuesta)
elif "Adios" in texto:
    texto_respuesta = "Hasta pronto!"
    enviar_mensaje(idchat, texto_respuesta)



