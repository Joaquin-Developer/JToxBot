# import pyowm, geojson
import os, json, requests, math
from googletrans import Translator

API_KEY = os.environ["PYOWN_API_KEY"]

def get_weather(city):
    id = get_id_city(city)
    if id == None:
        print("No se encontró la ciudad '{}'".format(city))
        return "No se encontró la ciudad '{}'".format(city)
    else:
        resp = requests.get("http://api.openweathermap.org/data/2.5/weather?id=" + id + "&appid=" + API_KEY)
        resp_data = json.loads(resp.text)
        # data processing:
        actual_temperature = kelvin_to_celcius(resp_data.get("main").get("temp"))
        feels_like = kelvin_to_celcius(resp_data.get("main").get("feels_like"))
        min_temp = kelvin_to_celcius(resp_data.get("main").get("temp_min"))
        max_temp = kelvin_to_celcius(resp_data.get("main").get("temp_max"))
        cloudiness = str(resp_data.get("clouds").get("all")) + " %"
        weather = translate_weather_to_spanish(resp_data.get("weather")[0].get("description"))
        text = """
        Datos de la ciudad de {}:
    Temperatura actual: {} °C
    Sensación térmica: {} °C
    Temp. máxima: {} °C
    Temp. mínima: {} °C
    Porcentaje de nubes: {}
    Clima actual: {}
    
Tox."""
        print(text.format(city, actual_temperature, feels_like, max_temp, min_temp, cloudiness, weather))
        return text.format(city, actual_temperature, feels_like, max_temp, min_temp, cloudiness, weather)
        # return "functionality out of service (Coming on v2.0)"

    
def read_json_city_list():
    json_city_list = open(os.environ["PP_ROUTE"] + "/BOT_Telegram_Python/v2.0/data/city_list.json").read()
    return json.loads(json_city_list)

def get_id_city(city):
    city_list_data = read_json_city_list()
    # sorted alphabetically:
    city_list_data = sorted(city_list_data, key=lambda k: k.get("name"), reverse=False)

    index = binary_search_get_city(city_list_data, city)
    if index != -1:   
        print(city_list_data[index]) 
        return str(city_list_data[index].get("id"))

    # for elem in city_list_data:
    #     if ((elem.get("name")).lower() == city.lower()):
    #         return str(elem.get("id"))

def binary_search_get_city(city_list_data, objective):
    # returns index of element in list:
    print(objective)
    left = 0
    right = len(city_list_data) - 1
    while (left <= right):
        #mid = left + (right - left) // 2
        mid = (left + right) // 2

        if (city_list_data[mid].get("name") == objective):
            return mid

        if (city_list_data[mid].get("name") > objective):
            right = mid - 1            
        else:
            left = mid + 1
            
    return -1
                

def kelvin_to_celcius(kelvin):
    return round(kelvin - 273.15)

def translate_weather_to_spanish(original_text):
    try:
        translator = Translator(service_urls=['translate.googleapis.com'])
        text = translator.translate(original_text, dest='es').text
    except Exception as e:
        print("Error: " + str(e))
        return "No se pudo obtener información del clima."
    else:
        return text

if __name__ == "__main__":
    get_weather("Montevideo")

