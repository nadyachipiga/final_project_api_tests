
# Надежда Чипига 33-я когорта, Финальный проект

import data
import sender_stand_requests

def test_order_track():
    new_order = sender_stand_requests.post_order(data.order_body)
    track = str(new_order.json()["track"])
    response = sender_stand_requests.get_order_track(track)
    assert response.status_code == 200