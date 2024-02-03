import sys
import requests


def get_image(ll, spn, l):

    map_params = {
        "ll": ll,
        "spn": spn,
        "l": l,
    }

    map_api_server = "http://static-maps.yandex.ru/1.x/"
    response = requests.get(map_api_server, params=map_params)

    with open("test.png", "wb") as f:
        f.write(response.content)
