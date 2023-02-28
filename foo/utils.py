import requests
import datetime


def json_load():
    data = requests.get('https://api.npoint.io/ce6d4e606f2fd82a0d68')
    data_words = data.json()
    return data_words
