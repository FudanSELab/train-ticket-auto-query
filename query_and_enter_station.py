from atomic_queries import _query_orders, _enter_station
from utils import random_form_list


def query_and_enter_station(headers):
    pairs = _query_orders(headers=headers, types=tuple([2]))
    pairs2 = _query_orders(headers=headers, types=tuple([2]), query_other=True)

    if not pairs and not pairs2:
        return

    pairs = pairs + pairs2

    # (orderId, tripId)
    pair = random_form_list(pairs)

    order_id = _enter_station(order_id=pair[0], headers=headers)
    if not order_id:
        return

    print(f"{order_id} queried and entered station")


if __name__ == '__main__':
    headers = {
        "Cookie": "JSESSIONID=DBE6EC845809D4BFEA66D76BA600995F; YsbCaptcha=63EEEE0E2D564384A7C0052999F3AEA6",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJmZHNlX21pY3Jvc2VydmljZSIsInJvbGVzIjpbIlJPTEVfVVNFUiJdLCJpZCI6IjRkMmE0NmM3LTcxY2ItNGNmMS1iNWJiLWI2ODQwNmQ5ZGE2ZiIsImlhdCI6MTYyNjM0OTcxOSwiZXhwIjoxNjI2MzUzMzE5fQ.nUTB1SI_gikEm8z8M6EQeyPuQx5zKevo40Y2rqf1EN4",
        "Content-Type": "application/json"
    }
    query_and_enter_station(headers=headers)
