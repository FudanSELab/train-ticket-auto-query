from typing import List
import requests
from pprint import pprint
import logging

logger = logging.getLogger("atomic_queries")
base_address = "http://139.196.152.44:31000"

headers = {
    "Cookie": "JSESSIONID=B39196FE741E35DAE67BC0719C351390; YsbCaptcha=A274C4DA81AF498A943A2A8661111737",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJmZHNlX21pY3Jvc2VydmljZSIsInJvbGVzIjpbIlJPTEVfVVNFUiJdLCJpZCI6IjRkMmE0NmM3LTcxY2ItNGNmMS1iNWJiLWI2ODQwNmQ5ZGE2ZiIsImlhdCI6MTYyNjMzMDMxMywiZXhwIjoxNjI2MzMzOTEzfQ.SdZ6zov5vfoM70VD9yeTbVy8TSv-tKaeImInP4YOckU",
    "Content-Type": "application/json"
}

# The UUID of fdse_microservice is that
uuid = "4d2a46c7-71cb-4cf1-b5bb-b68406d9da6f"


def _login():
    pass


def _query_high_speed_ticket(place_pair: tuple = ("Shang Hai", "Su Zhou"), headers: dict = {}, time: str = "2021-07-15") -> List[str]:
    """
    返回TripId 列表
    :param place_pair: 使用的开始结束组对
    :param headers: 请求头
    :return: TripId 列表
    """

    url = f"{base_address}/api/v1/travelservice/trips/left"
    place_pairs = [("Shang Hai", "Su Zhou"),
                   ("Su Zhou", "Shang Hai"),
                   ("Nan Jing", "Shang Hai")]

    payload = {
        "departureTime": time,
        "startingPlace": place_pair[0],
        "endPlace": place_pair[1],
    }

    response = requests.post(url=url,
                             headers=headers,
                             json=payload)

    if response.status_code is not 200 or response.json().get("data") is None:
        logger.warning(f"request for {url} failed. response data is {response.json()}")
        return None

    data = response.json().get("data")  # type: dict

    trip_ids = []
    for d in data:
        trip_id = d.get("tripId").get("type") + d.get("tripId").get("number")
        trip_ids.append(trip_id)
    return trip_ids


def _query_normal_ticket(place_pair: tuple = ("Nan Jing", "Shang Hai"), headers: dict = {}, time: str = "2021-07-15") -> List[str]:
    url = f"{base_address}/api/v1/travel2service/trips/left"
    place_pairs = [("Shang Hai", "Nan Jing"),
                   ("Nan Jing", "Shang Hai")]

    payload = {
        "departureTime": time,
        "startingPlace": place_pair[0],
        "endPlace": place_pair[1],
    }

    response = requests.post(url=url,
                             headers=headers,
                             json=payload)
    if response.status_code is not 200 or response.json().get("data") is None:
        logger.warning(f"request for {url} failed. response data is {response.json()}")
        return None

    data = response.json().get("data")  # type: dict

    trip_ids = []
    for d in data:
        trip_id = d.get("tripId").get("type") + d.get("tripId").get("number")
        trip_ids.append(trip_id)
    return trip_ids





def _query_assurances(headers: dict = {}):
    url = f"{base_address}/api/v1/assuranceservice/assurances/types"
    response = requests.get(url=url,headers=headers)
    if response.status_code is not 200 or response.json().get("data") is None:
        logger.warning(f"query assurance failed, response data is {response.json()}")
        return None
    data = response.json().get("data")
    # assurance只有一种

    return [{"assurance": "1"}]


def _query_food(place_pair: tuple = ("Shang Hai", "Su Zhou"), train_num: str = "D1345", headers: dict = {}):
    url = f"{base_address}/api/v1/foodservice/foods/2021-07-14/{place_pair[0]}/{place_pair[1]}/{train_num}"

    response = requests.get(url=url, headers=headers)
    if response.status_code is not 200 or response.json().get("data") is None:
        logger.warning(f"query food failed, response data is {response.json()}")
        return None
    data = response.json().get("data")

    # food 是什么不会对后续调用链有影响，因此查询后返回一个固定数值
    return [{
        "foodName": "Soup",
        "foodPrice": 3.7,
        "foodType": 2,
        "stationName": "Su Zhou",
        "storeName": "Roman Holiday"
    }]


def _query_contacts(headers: dict = {}) -> List[str]:
    """
    返回座位id列表
    :param headers:
    :return: id list
    """
    global uuid
    url = f"{base_address}/api/v1/contactservice/contacts/account/{uuid}"

    response = requests.get(url=url, headers=headers)
    if response.status_code is not 200 or response.json().get("data") is None:
        logger.warning(f"query contacts failed, response data is {response.json()}")
        return None

    data = response.json().get("data")
    #print("contacts")
    #pprint(data)


    ids = [d.get("id") for d in data if d.get("id") is not None]
    #pprint(ids)
    return ids


if __name__ == '__main__':
    #_query_food(headers=headers)
    #_query_high_speed_ticket(headers=headers)
    _query_contacts(headers=headers)


