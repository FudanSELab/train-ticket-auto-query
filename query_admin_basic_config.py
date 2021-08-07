import logging
import time

from atomic_queries import _query_admin_basic_config

logger = logging.getLogger("query_and_preserve")
# The UUID of user fdse_microservice is that
uuid = "4d2a46c7-71cb-4cf1-b5bb-b68406d9da6f"
date = time.strftime("%Y-%m-%d", time.localtime())

base_address = "http://10.176.122.6:32677"


def query_admin_basic_config(headers):
    _query_admin_basic_config(headers=headers)


if __name__ == '__main__':
    cookie = "JSESSIONID=823B2652E3F5B64A1C94C924A05D80AF; YsbCaptcha=2E037F4AB09D49FA9EE3BE4E737EAFD2"
    Authorization = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJmZHNlX21pY3Jvc2VydmljZSIsInJvbGVzIjpbIlJPTEVfVVNFUiJdLCJpZCI6IjRkMmE0NmM3LTcxY2ItNGNmMS1iNWJiLWI2ODQwNmQ5ZGE2ZiIsImlhdCI6MTYyODM1Nzg0NywiZXhwIjoxNjI4MzYxNDQ3fQ.A1Y_pMRGWgaDRMlAtPggKc-qX2nMmyp28RsaPkoG-sk"
    headers = {
        'Connection': 'close',
        "Cookie": f"{cookie}",
        "Authorization": f"Bearer {Authorization}",
        "Content-Type": "application/json"
    }

    start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    for j in range(7):
        for i in range(40):
            try:
                query_admin_basic_config(headers=headers)
                print("*****************************INDEX:" + str(j * 40 + i))
            except Exception as e:
                print(e)
        time.sleep(10)

    end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    print(f"start:{start_time} end:{end_time}")
