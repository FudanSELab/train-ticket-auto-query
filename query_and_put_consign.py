import time

from atomic_queries import _query_orders_all_info, _put_consign
from utils import random_form_list


def query_one_and_put_consign(headers, pairs):
    """
    查询order并put consign
    :param uuid:
    :param headers:
    :return:
    """

    pair = random_form_list(pairs)

    order_id = _put_consign(result=pair, headers=headers)
    if not order_id:
        return

    print(f"{order_id} queried and put consign")


if __name__ == '__main__':
    cookie = "JSESSIONID=823B2652E3F5B64A1C94C924A05D80AF; YsbCaptcha=2E037F4AB09D49FA9EE3BE4E737EAFD2"
    Authorization = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJmZHNlX21pY3Jvc2VydmljZSIsInJvbGVzIjpbIlJPTEVfVVNFUiJdLCJpZCI6IjRkMmE0NmM3LTcxY2ItNGNmMS1iNWJiLWI2ODQwNmQ5ZGE2ZiIsImlhdCI6MTYyODcwNTc0MiwiZXhwIjoxNjI4NzA5MzQyfQ.VHlvCNvaDW41rO55XNV1nniKotW6ip1TFfHaDqyDO3s"
    headers = {
        'Connection': 'close',
        "Cookie": f"{cookie}",
        "Authorization": f"Bearer {Authorization}",
        "Content-Type": "application/json"
    }
    uuid = "4d2a46c7-71cb-4cf1-b5bb-b68406d9da6f"

    start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    pairs = _query_orders_all_info(headers=headers)
    pairs2 = _query_orders_all_info(headers=headers, query_other=True)

    pairs = pairs + pairs2

    for i in range(330):
        try:
            query_one_and_put_consign(headers=headers, pairs=pairs)
            print("*****************************INDEX:" + str(i))
        except Exception as e:
            print(e)

    end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    print(f"start:{start_time} end:{end_time}")
