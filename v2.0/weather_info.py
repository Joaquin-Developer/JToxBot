# import pyowm, geojson
import os, json, requests

API_KEY = os.environ["PYOWN_API_KEY"]

def return_weather(city):
    id = get_id_city(city)
    resp = requests.get("http://api.openweathermap.org/data/2.5/weather?id=" + id + "&appid=" + API_KEY)
    resp_data = json.loads(resp.text)
    # data processing:
    actual_temperature = kelvin_to_celcius(resp_data.get("main").get("temp"))
    feels_like = kelvin_to_celcius(resp_data.get("main").get("feels_like"))
    min_temp = kelvin_to_celcius(resp_data.get("main").get("temp_min"))
    max_temp = kelvin_to_celcius(resp_data.get("main").get("temp_max"))
    cloudiness = str(resp_data.get("clouds").get("all")) + " %"
    text = """
    Datos de la ciudad de {}:
    Temperatura actual: {} °C
    Sensación térmica: {} °C
    Temp. máxima: {} °C
    Temp. mínima: {} °C
    Porcentaje de nubes: {}"""
    #print(text.format(city, actual_temperature, feels_like, max_temp, min_temp, cloudiness))
    return text.format(city, actual_temperature, feels_like, max_temp, min_temp, cloudiness)
    #return "functionality out of service (Coming on v2.0)"

def read_json_city_list():
    json_city_list = open(os.environ["PP_ROUTE"] + "/BOT_Telegram_Python/v2.0/data/city_list.json").read()
    return json.loads(json_city_list)

# Nota: OPTIMIZAR esta búsqueda:
def get_id_city(city):
    city_list_data = read_json_city_list()
    for elem in city_list_data:
        if ((elem.get("name")).lower() == city.lower()):
            return str(elem.get("id"))

def kelvin_to_celcius(kelvin):
    return round(kelvin - 273.15)

if __name__ == "__main__":
    return_weather("montevideo")
