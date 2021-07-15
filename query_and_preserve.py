from atomic_queries import _query_high_speed_ticket, _query_normal_ticket, _query_assurances, _query_food, _query_contacts

import logging
import random
from typing import List
import string
import requests

logger = logging.getLogger("main")
headers = {
    "Cookie": "JSESSIONID=E629E6ACA021C7DD4DC00AC6F2F97D7F; YsbCaptcha=3B591B44263E4C8C9CE44F515BF735B6",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJmZHNlX21pY3Jvc2VydmljZSIsInJvbGVzIjpbIlJPTEVfVVNFUiJdLCJpZCI6IjRkMmE0NmM3LTcxY2ItNGNmMS1iNWJiLWI2ODQwNmQ5ZGE2ZiIsImlhdCI6MTYyNjMzNTk3NCwiZXhwIjoxNjI2MzM5NTc0fQ.uH-tN-9qlmZV-2KrflPenR87AaHPdhECTehWMj8wS4g",
    "Content-Type": "application/json"
}
# The UUID of fdse_microservice is that
uuid = "4d2a46c7-71cb-4cf1-b5bb-b68406d9da6f"
# TODO: 自动化日期
date = "2021-07-15"

base_address = "http://139.196.152.44:31000"


"""
    查询Order并付款未付款Order
    5. 查询ticket并Collect所有票
    6. 查询可进站票并进站所有票
"""
def query_and_preserve():
    """
    查票、付款、取票(Collect)、入站

    1. 查票（随机高铁或普通）
    2. 查保险、Food、Contacts
    3. 随机选择Contacts、保险、是否买食物、是否托运
    4. 买票
    :return:
    """
    start = ""
    end = ""
    trip_ids = []
    PRESERVE_URL = ""

    high_speed = random_boolean()
    if high_speed:
        start = "Shang Hai"
        end = "Su Zhou"
        high_speed_place_pair = (start, end)
        trip_ids = _query_high_speed_ticket(place_pair=high_speed_place_pair, headers=headers, time=date)
        PRESERVE_URL = f"{base_address}/api/v1/preserveservice/preserve"
    else:
        start = "Shang Hai"
        end = "Nan Jing"
        other_place_pair = (start, end)
        trip_ids = _query_normal_ticket(place_pair=other_place_pair, headers=headers, time=date)
        PRESERVE_URL = f"{base_address}/api/v1/preserveotherservice/preserveOther"

    _ = _query_assurances(headers=headers)
    food_result = _query_food(headers=headers)
    contacts_result = _query_contacts(headers=headers)

    base_preserve_payload = {
        "accountId": uuid,
        "assurance": "0",
        "contactsId": "",
        "date": date,
        "from": start,
        "to": end,
        "tripId": ""
    }

    trip_id = random_form_list(trip_ids)
    base_preserve_payload["tripId"] = trip_id

    need_food = random_boolean()
    if need_food:
        logger.info("need food")
        food_dict = random_form_list(food_result)
        base_preserve_payload.update(food_dict)
    else:
        logger.info("not need food")
        base_preserve_payload["foodType"] = "0"

    need_assurance = random_boolean()
    if need_assurance:
        base_preserve_payload["assurance"] = 1

    contacts_id = random_form_list(contacts_result)
    base_preserve_payload["contactsId"] = contacts_id

    # 高铁 2-3
    seat_type = random_form_list(["2", "3"])
    base_preserve_payload["seatType"] = seat_type

    need_consign = random_boolean()
    if need_consign:
        consign = {
            "consigneeName": random_str(),
            "consigneePhone": random_phone(),
            "consigneeWeight": random.randint(1, 10),
            "handleDate": date
        }
        base_preserve_payload.update(consign)

    print("payload:" + str(base_preserve_payload))

    print(f"choices: preserve_high: {high_speed} need_food:{need_food}  need_consign: {need_consign}  need_assurance:{need_assurance}")

    res = requests.post(url=PRESERVE_URL,
                        headers=headers,
                        json=base_preserve_payload)

    print(res.json())
    if res.json()["data"] != "Success":
        raise Exception(res.json() + " not success")


def query_order_and_pay():
    """
    查询Order并付款未付款Order
    :return:
    """
    pass


def random_boolean() -> bool:
    return random.choice([True, False])


def random_form_list(l: List):
    return random.choice(l)


def random_str():
    ''.join(random.choices(string.ascii_letters, k=random.randint(4, 10)))


def random_phone():
    ''.join(random.choices(string.digits, k=random.randint(8, 15)))


if __name__ == '__main__':

    for i in range(100):
        try:
            query_and_preserve()
            print("*****************************TIME:" + str(i))
        except Exception as e:
            print(e)
