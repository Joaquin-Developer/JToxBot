# pylint: disable=missing-function-docstring
# -*- coding: utf-8 -*-
import json
from typing import Any
import requests
from googletrans import Translator
from core import config
import utils

# import pyowm, geojson


def kelvin_to_celcius(kelvin) -> int:
    return round(kelvin - 273.15)


def read_json_city_list() -> Any:
    json_city_list = open(config.CITIES_JSON_ROUTE).read()
    return json.loads(json_city_list)


def binary_search_get_city(city_list_data, objective):
    """returns index of element in list"""
    print(objective)
    left = 0
    right = len(city_list_data) - 1
    while left <= right:
        # mid = left + (right - left) // 2
        mid = (left + right) // 2

        if city_list_data[mid].get("name") == objective:
            return mid

        if city_list_data[mid].get("name") > objective:
            right = mid - 1
        else:
            left = mid + 1

    return -1


def get_id_city(city) -> str:
    city_list_data = read_json_city_list()
    # sorted alphabetically:
    city_list_data = sorted(city_list_data, key=lambda k: k.get("name"), reverse=False)

    index = binary_search_get_city(city_list_data, city)

    if index == 1:
        return None

    print(city_list_data[index])
    return str(city_list_data[index].get("id"))


def translate_weather_to_spanish(original_text):
    translator = Translator(service_urls=["translate.googleapis.com"])
    return translator.translate(original_text, dest="es").text
    # except Exception as ex:
    #     print("Error: " + str(ex))
    #     return "No se pudo obtener información del clima."


class WeatherInfo:
    """Wrapper"""

    @staticmethod
    def get_weather(city):
        """get weather info"""
        city_id = get_id_city(city)

        if city_id is None:
            return "No se encontró la ciudad '{}'".format(city)

        resp = requests.get("http://api.openweathermap.org/data/2.5/weather?id=" + id + "&appid=" + config.API_KEY)
        resp_data = json.loads(resp.text)
        # data processing:
        actual_temperature = kelvin_to_celcius(resp_data.get("main").get("temp"))
        feels_like = kelvin_to_celcius(resp_data.get("main").get("feels_like"))
        min_temp = kelvin_to_celcius(resp_data.get("main").get("temp_min"))
        max_temp = kelvin_to_celcius(resp_data.get("main").get("temp_max"))
        cloudiness = str(resp_data.get("clouds").get("all")) + " %"
        weather = translate_weather_to_spanish(resp_data.get("weather")[0].get("description"))

        text: str = utils.get_from_config("Messages", "weather_message")

        data = text.format(city, actual_temperature, feels_like, max_temp, min_temp, cloudiness, weather)
        print(data)
        return data


if __name__ == "__main__":
    WeatherInfo.get_weather("Montevideo")
