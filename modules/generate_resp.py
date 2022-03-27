# pylint: disable=missing-module-docstring
import json
import requests
from core import config


class Resp:
    """Response"""

    @staticmethod
    def update():
        # Llamar al metodo getUpdates del bot haciendo una peticion HTTPS (se obtiene una respuesta codificada)
        resp = requests.get(config.URL + "getUpdates")
        # Decodificar la respuesta recibida a formato UTF8 (se obtiene un string JSON)
        json_messages = resp.content.decode("utf8")
        # Convertir el string de JSON a un diccionario de Python
        return json.loads(json_messages)

    @staticmethod
    def read_messages():
        """call update() and save the dictionary with the messages"""
        messages = Resp.update()
        # calculate the index from last received message:
        index = len(messages["result"]) - 1
        # From the text extract the name of person and id of the last message_
        text = messages["result"][index]["message"]["text"]
        person = messages["result"][index]["message"]["from"]["first_name"]
        id_chat = messages["result"][index]["message"]["chat"]["id"]
        print(person + " (id: " + str(id_chat) + ") ha escrito: " + text)
        return id_chat, person, text

    @staticmethod
    def send_message(id_chat, text):
        """call the method sendMessage from the bot:"""
        requests.get(config.URL + "sendMessage?text=" + text + "&chat_id=" + str(id_chat))


if __name__ == "__main__":

    # Llamar a la funcion "leer_mensaje()"
    id_chat, person, text = Resp.read_messages()

    # Generar una respuesta a partir de la informacion del mensaje
    if "Hola" in text:
        resp = "Hola, " + person + "!"
        Resp.send_message(id_chat, resp)
    elif "Adios" in text:
        resp = "Hasta pronto!"
        Resp.send_message(id_chat, resp)

    # probar...
