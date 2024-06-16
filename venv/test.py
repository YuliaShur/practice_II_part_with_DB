import requests
import json
import pytest
from request import create_order, get_order_by_track
from data import order_body

def test_order_creation():
    """    Тест создания заказа и получения его данных по треку.
    """
    # Создание заказа
    creation_response = create_order()

    # Проверка статуса ответа на создание заказа
    assert creation_response.status_code == 201, "Проверка статуса ответа на создание заказа"

    # Извлечение трека заказа из ответа
    track_id = creation_response.json()['track']  # Замените на правильный ключ!
    # Получение заказа по треку
    response = get_order_by_track(track_id)

    # Проверка статуса ответа на получение заказа по треку
    assert response.status_code == 200, "Проверка статуса ответа на получение заказа по треку"

    # (Дополнительная проверка данных заказа - опционально)
    # order_data = response.json()
    # assert order_data['track'] == track_id, "Трек заказа не совпадает"

