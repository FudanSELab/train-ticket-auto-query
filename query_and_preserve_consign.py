from atomic_queries import _query_high_speed_ticket, _query_normal_ticket, _query_assurances, _query_food, \
    _query_contacts
from utils import random_boolean, random_phone, random_str, random_form_list

import logging
import random
import requests
import time

logger = logging.getLogger("query_and_preserve")
# The UUID of user fdse_microservice is that
uuid = "4d2a46c7-71cb-4cf1-b5bb-b68406d9da6f"
date = time.strftime("%Y-%m-%d", time.localtime())

base_address = "http://139.196.152.44:31000"


def query_and_preserve_consign(headers):
    """
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

    high_speed = True
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
    # food_result = _query_food(headers=headers)
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
    return base_preserve_payload, contacts_result, trip_ids, PRESERVE_URL, high_speed


def preserve(base_preserve_payload, contacts_result, trip_ids, PRESERVE_URL, high_speed, headers):
    trip_id = random_form_list(trip_ids)
    base_preserve_payload["tripId"] = trip_id

    need_food = random_boolean()
    if need_food:
        logger.info("need food")
        food_dict = {
            "foodType": 2,
            "foodName": "Spicy hot noodles",
            "foodPrice": 5
        }
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

    need_consign = True
    if need_consign:
        consign = {
            "consigneeName": "32",
            "consigneePhone": "12345677654",
            "consigneeWeight": random.randint(1, 10),
            "handleDate": date
        }
        base_preserve_payload.update(consign)

    # print("payload:" + str(base_preserve_payload))

    print(
        f"choices: preserve_high: {high_speed} need_food:{need_food}  need_consign: {need_consign}  need_assurance:{need_assurance}")

    res = requests.post(url=PRESERVE_URL,
                        headers=headers,
                        json=base_preserve_payload)

    if res.status_code != 200:
        print(" fail")
    else:
        print("success")


if __name__ == '__main__':
    cookie = "JSESSIONID=823B2652E3F5B64A1C94C924A05D80AF; YsbCaptcha=2E037F4AB09D49FA9EE3BE4E737EAFD2"
    Authorization = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJmZHNlX21pY3Jvc2VydmljZSIsInJvbGVzIjpbIlJPTEVfVVNFUiJdLCJpZCI6IjRkMmE0NmM3LTcxY2ItNGNmMS1iNWJiLWI2ODQwNmQ5ZGE2ZiIsImlhdCI6MTYyODcwMzQ5NSwiZXhwIjoxNjI4NzA3MDk1fQ.HkehJkZ8E4zdd2q83uydtvdmEH-fvu5bH5Y9bwzsIIk"
    headers = {
        'Connection': 'close',
        "Cookie": f"{cookie}",
        "Authorization": f"Bearer {Authorization}",
        "Content-Type": "application/json"
    }
    base_preserve_payload, contacts_result, trip_ids, PRESERVE_URL, high_speed = query_and_preserve_consign(
        headers=headers)

    start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    for i in range(330):
        try:
            preserve(base_preserve_payload, contacts_result, trip_ids, PRESERVE_URL, high_speed, headers)
            print("*****************************INDEX:" + str(i))
        except Exception as e:
            print(e)

    end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    print(f"start:{start_time} end:{end_time}")
