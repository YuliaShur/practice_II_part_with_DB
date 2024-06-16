import requests
import data
import configuration

def create_order():
    """    Запрос на создание нового заказа.
    """
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_NEW_ORDER, json=data.order_body)

def get_order_by_track(track_id):
    """
    Запрос на получение заказа по его трек номеру.
    """
    return requests.get(configuration.URL_SERVICE + configuration.RECEIVING_ORDER_BY_ID + "?t=" + str(track_id))

