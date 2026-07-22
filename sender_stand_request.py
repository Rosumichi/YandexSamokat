import configuration
import requests
import data

def post_new_order(order_body):
    """Отправка POST-запроса на создание нового заказа"""
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_ORDERS,
        json=order_body,
        headers=data.headers
    )

def get_order_by_track(track):
    """Отправка GET-запроса на получение информации о заказе по его трек-номеру"""
    return requests.get(
        configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK,
        params={"t": track}
    )