from atomic_queries import _query_advanced_ticket, _login

import logging
import random
import time

logger = logging.getLogger("query_advanced_ticket")
# The UUID of user fdse_microservice is that
uuid = "4d2a46c7-71cb-4cf1-b5bb-b68406d9da6f"
date = time.strftime("%Y-%m-%d", time.localtime())

base_address = "http://10.176.122.1:32677"



if __name__ == '__main__':
    _, token = _login()
    headers = {
        "Cookie": "JSESSIONID=823B2652E3F5B64A1C94C924A05D80AF; YsbCaptcha=2E037F4AB09D49FA9EE3BE4E737EAFD2",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJmZHNlX21pY3Jvc2VydmljZSIsInJvbGVzIjpbIlJPTEVfVVNFUiJdLCJpZCI6IjRkMmE0NmM3LTcxY2ItNGNmMS1iNWJiLWI2ODQwNmQ5ZGE2ZiIsImlhdCI6MTYyNzE5OTA0NCwiZXhwIjoxNjI3MjAyNjQ0fQ.3IIwwz7AwqHtOFDeXfih25i6_7nQBPL_K7BFxuyFiKQ",
        "Content-Type": "application/json"
    }
    headers["Authorization"] = "Bearer " + token

    start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    place_pairs = [("Shang Hai", "Su Zhou"),
                   ("Su Zhou", "Shang Hai"),
                   ("Nan Jing", "Shang Hai")]
    type = "quickest"
    for i in range(200):
        place_pair = random.choice(place_pairs)
        print(f"search {type} between {place_pair[0]} to {place_pair[1]}")
        try:
            trip_ids = _query_advanced_ticket(place_pair=place_pair, headers=headers, time=date, type=type)
            print(f"get {len(trip_ids)} routes.")
            print("*****************************INDEX:" + str(i))
        except Exception as e:
            print(e)

    end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    print(f"start:{start_time} end:{end_time}")