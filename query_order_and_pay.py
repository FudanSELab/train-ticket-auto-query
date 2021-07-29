import time

from atomic_queries import _query_orders, _pay_one_order
from utils import random_form_list


def query_order_and_pay(headers):
    """
    查询Order并付款未付款Order
    :return:
    """
    pairs = _query_orders(headers=headers, types=tuple([0, 1]))
    pairs2 = _query_orders(headers=headers, types=tuple([0, 1]), query_other=True)

    if not pairs and not pairs2:
        return

    pairs = pairs + pairs2

    # (orderId, tripId) pair
    pair = random_form_list(pairs)

    order_id = _pay_one_order(pair[0], pair[1], headers=headers)
    if not order_id:
        return

    print(f"{order_id} queried and paid")


if __name__ == '__main__':
    cookie = "JSESSIONID=823B2652E3F5B64A1C94C924A05D80AF; YsbCaptcha=2E037F4AB09D49FA9EE3BE4E737EAFD2"
    Authorization = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJmZHNlX21pY3Jvc2VydmljZSIsInJvbGVzIjpbIlJPTEVfVVNFUiJdLCJpZCI6IjRkMmE0NmM3LTcxY2ItNGNmMS1iNWJiLWI2ODQwNmQ5ZGE2ZiIsImlhdCI6MTYyNzU0OTU5NSwiZXhwIjoxNjI3NTUzMTk1fQ.uDVxJn1v1StNmHw2mS8AnwKW2x4Suj547IOHtKKC-Sw"

    headers = {
        'Connection': 'close',
        "Cookie": f"{cookie}",
        "Authorization": f"Bearer {Authorization}",
        "Content-Type": "application/json"
    }

    start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    for i in range(40):
        try:
            query_order_and_pay(headers=headers)
            print("*****************************INDEX:" + str(i))
        except Exception as e:
            print(e)

    end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    print(f"start:{start_time} end:{end_time}")
