from atomic_queries import _query_route

if __name__ == '__main__':

    headers = {
        "Cookie": "JSESSIONID=CAF07ABCB2031807D1C6043730C69F17; YsbCaptcha=ABF26F4AE563405894B1540057F62E7B",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJmZHNlX21pY3Jvc2VydmljZSIsInJvbGVzIjpbIlJPTEVfVVNFUiJdLCJpZCI6IjRkMmE0NmM3LTcxY2ItNGNmMS1iNWJiLWI2ODQwNmQ5ZGE2ZiIsImlhdCI6MTYyNjM0NDgyNSwiZXhwIjoxNjI2MzQ4NDI1fQ.4eOMmQDhnq-Hjj1DuiH8duT6rXkP0QfeTnaXwvYGKD4",
        "Content-Type": "application/json"
    }

    _query_route(headers=headers)
