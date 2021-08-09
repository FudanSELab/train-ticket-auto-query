from atomic_queries import _query_orders, _collect_one_order, _login, _rebook_ticket
from utils import random_form_list
import time

base_address = "http://10.176.122.1:32677"


def query_and_rebook(headers):

    pairs = _query_orders(headers=headers, types=tuple([1]))
    #pairs2 = _query_orders(headers=headers, types=tuple([1]), query_other=True)

    # if not pairs and not pairs2:
    #     return

    # pairs = pairs + pairs2

    # (orderId, tripId)
    # pair = random_form_list(pairs)
    new_trip_id = "D1345"
    new_date = time.strftime("%Y-%m-%d", time.localtime())
    new_seat_type = "3"

    for pair in pairs: 
        #print(pair)
        _rebook_ticket(old_order_id=pair[0], old_trip_id=pair[1], new_trip_id=new_trip_id, new_date=new_date, new_seat_type=new_seat_type, headers=headers)





if __name__ == '__main__':
    _, token = _login()

    headers = {
        "Cookie": "JSESSIONID=DBE6EC845809D4BFEA66D76BA600995F; YsbCaptcha=63EEEE0E2D564384A7C0052999F3AEA6",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJmZHNlX21pY3Jvc2VydmljZSIsInJvbGVzIjpbIlJPTEVfVVNFUiJdLCJpZCI6IjRkMmE0NmM3LTcxY2ItNGNmMS1iNWJiLWI2ODQwNmQ5ZGE2ZiIsImlhdCI6MTYyODA5NjE1OSwiZXhwIjoxNjI4MDk5NzU5fQ.xoFsdd-erzuwjJFjl3M6enrCtths0Toy0NjotSohq7s",
        "Content-Type": "application/json"
    }
    headers["Authorization"] = "Bearer " + token
    
    start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    query_and_rebook(headers=headers)

    end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    print(f"start:{start_time} end:{end_time}")