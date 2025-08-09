import requests
import config
import data

def post_order(body):
    return requests.post(config.URL_SERVICE+config.CREATE_ORDER , json=body, headers=data.headers)

def get_order_track(track):
    return requests.get(config.URL_SERVICE+config.GET_ORDERS+str(track))