import json
import requests
 
#Variables para el Token y la URL del chatbot
# USAR VARIABLES DE ENTORNO PARA E TOKEN!
TOKEN = "..." #Poner el token
URL = "https://api.telegram.org/bot" + TOKEN + "/"
 
def update():	
    #Llamar al metodo getUpdates del bot haciendo una peticion HTTPS (se obtiene una respuesta codificada)
    resp = requests.get(URL + "getUpdates")
    #Decodificar la respuesta recibida a formato UTF8 (se obtiene un string JSON)
    json_messages = resp.content.decode("utf8")
    #Convertir el string de JSON a un diccionario de Python
    return json.loads(json_messages)
 
def read_messages():
    # call update() and save the dictionary with the messages
    messages = update()
    # calculate the index from last received message:
    index = len(messages["result"])-1
    #Extraer el texto, nombre de la persona e id del último mensaje recibido
    text = messages["result"][index]["message"]["text"]
    person = messages["result"][index]["message"]["from"]["first_name"]
    id_chat = messages["result"][index]["message"]["chat"]["id"]
    print(person + " (id: " + str(id_chat) + ") ha escrito: " + text)
 
if __name__ == '__main__':
    read_messages()