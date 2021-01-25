
import os
import requests

while (True):
    #clean()
    send = input("Ingresar mensaje a enviar: ")
    id = "@Joaquin703"
    token = "1248720968:AAGvdHN1ykjKdX3I1V1YV-dUpd38EhIDPY8"
    url = "https://api.telegram.org/bot" + token + "/sendMessage"
    params = {
        'chat_id': id,
        'text': send        
    }

    requests.post(url, params=params)
    con = input("Presione x para salir: ")
    if con == "x":
        break # exit while

