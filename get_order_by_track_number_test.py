import sender_stand_request
import data

# Николай Новак, 44-я когорта — Финальный проект. Инженер по тестированию плюс

# Тест проверяет успешность получения информации о заказе по его трек-номеру.
def test_get_order_by_track_number():
    # Шаг 1: Создаем заказ и получаем его тело ответа
    order_response = sender_stand_request.post_new_order(data.order_body)
    
    # Шаг 2: Извлекаем трек-номер из ответа сервера
    track = order_response.json()["track"]
    
    # Шаг 3: Запрашиваем информацию по данному треку
    response = sender_stand_request.get_order_by_track(track)
    
    # Шаг 4: Проверяем, что сервер вернул статус-код 200 (ОК)
    assert response.status_code == 200