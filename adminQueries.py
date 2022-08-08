import logging
import time
from queries import Query

logger = logging.getLogger("auto-queries")
datestr = time.strftime("%Y-%m-%d", time.localtime())

class AdminQuery(Query):

    # station相关增删改查
    def stations_post(self, station_id: str = "", name: str = "", stay_time: int = 15, headers: dict = {}) -> str:
        """
        添加车站stations
        :param station_id: 新增station的id
        :param name: 新增station的名称
        :param stay_time: 新增station的的停靠时间
        :param headers: 请求头
        :return
        """
        logger.info(f"[stations_post]: station_id:{station_id}")
        if headers == {}:
            headers = self.session.headers
        # 请求url
        url = f"{self.address}/api/v1/adminbasicservice/adminbasic/stations"

        # 请求载荷，对应@requestbody注解
        payload = {
            "id": station_id,
            "name": name,
            "stayTime": stay_time,
        }

        # 发送请求、获取响应
        # 重复添加某一id对应的station不会抛出异常，但也不会覆盖或造成影响
        response = self.session.post(url=url, headers=headers, json=payload)

        if response.status_code != 200 or response.json().get("data") is None:  # 响应错误则忽略并打印日志
            logger.warning(f"request for {url} failed. response data is {response.text}")
            return None

        # 返回值为新增的车站信息
        data = response.json().get("data")
        print(data)
        return data

    def stations_get(self, headers: dict = {}) -> str:
        """
        获取所有车站信息
        :param headers: 请求头
        :return 所有车站组成的列表，每个车站的具体信息为字典形式，整合成string返回
        """
        logger.info(f"[stations_get]: admin_get")
        if headers == {}:
            headers = self.session.headers
        # 请求url
        url = f"{self.address}/api/v1/adminbasicservice/adminbasic/stations"

        # 发送请求、获取响应
        response = self.session.get(url=url, headers=headers)

        if response.status_code != 200 or response.json().get("data") is None:  # 响应错误则忽略并打印日志
            logger.warning(f"request for {url} failed. response data is {response.text}")
            return None

        data = response.json().get("data")  # 用string形式返回
        print(data)
        return data

    def stations_put(self, station_id: str = "", name: str = "", stay_time: int = 15, headers: dict = {}) -> str:
        """
        修改某一车站信息
        :param station_id: station的id
        :param name: 修改后station的名称
        :param stay_time: 修改后station的的停靠时间
        :param headers: 请求头
        :return
        """
        logger.info(f"[stations_put]: station_id:{station_id}")
        if headers == {}:
            headers = self.session.headers
        # 请求url
        url = f"{self.address}/api/v1/adminbasicservice/adminbasic/stations"

        # 请求载荷，对应@requestbody注解
        payload = {
            "id": station_id,
            "name": name,
            "stayTime": stay_time,
        }

        # 发送请求、获取响应
        # 对于此put请求而言，如果输入的payload代表的车站(由id决定)不存在则修改车站信息会抛出异常
        # {"status":0,"msg":"Station not exist","data":null}
        response = self.session.put(url=url, headers=headers, json=payload)

        if response.status_code != 200 or response.json().get("data") is None:  # 响应错误则忽略并打印日志
            logger.warning(f"request for {url} failed. response data is {response.text}")
            return None

        # 返回值为修改后的车站信息
        data = response.json().get("data")  # 用string形式返回
        print(data)
        return data

    def stations_delete(self, station_id: str = "", name: str = "", stay_time: int = 15, headers: dict = {}) -> str:
        """
        删除某一车站信息
        :param station_id: 删除station的id
        :param name: 删除station的名称（可以不正确）
        :param stay_time: 删除station的的停靠时间（可以不正确）
        :param headers: 请求头
        :return
        """
        logger.info(f"[stations_delete]: station_id:{station_id}")
        if headers == {}:
            headers = self.session.headers
        # 请求url
        url = f"{self.address}/api/v1/adminbasicservice/adminbasic/stations"

        # 请求载荷，对应@requestbody注解
        payload = {
            "id": station_id,  # 用于检索车站
            "name": name,
            "stayTime": stay_time,
        }

        # 发送请求、获取响应
        # 对于此delete请求而言，如果输入的payload代表的车站(由id决定)不存在则删除车站会抛出异常
        # {"status": 0, "msg": "Station not exist", "data": null}
        response = self.session.delete(url=url, headers=headers, json=payload)

        if response.status_code != 200 or response.json().get("data") is None:  # 响应错误则忽略并打印日志
            logger.warning(f"request for {url} failed. response data is {response.text}")
            return None

        # 返回值为删除车站的信息（id + 输入的name + 0）
        data = response.json().get("data")  # 用string形式返回
        print(data)
        return data

    # contact相关增删改查
    def contacts_post(self, account_id: str = "4d2a46c7-71cb-4cf1-b5bb-b68406d9da6f",
                      contact_name: str = "Contacts_X", document_type: int = 1,
                      document_number: str = "DocumentNumber_X", phone_number: str = "19921940977",
                      headers: dict = {}):
        """
        添加联系人contact
        # :param contact_id: 新增contact的id (不需要输入，在新建时随机生成)
        :param account_id: 新增contact的账户id
        :param contact_name: 新增contact的名称
        :param document_type:
        :param document_number:
        :param phone_number:
        :param headers: 请求头
        :return
        """
        logger.info(f"[contacts_post]: user_account_id:{account_id}")
        if headers == {}:
            headers = self.session.headers
        # 请求url
        url = f"{self.address}/api/v1/adminbasicservice/adminbasic/contacts"

        # 请求载荷
        payload = {
            "accountId": account_id,
            "name": contact_name,
            "documentType": document_type,
            "documentNumber": document_number,
            "phoneNumber": phone_number
        }

        # 发送请求、获取响应
        # 重复添加同一个contact是不会导致异常的，其内部生成的id不同
        response = self.session.post(url=url, headers=headers, json=payload)

        if response.status_code != 200:  # 响应错误则忽略并打印日志
            logger.warning(f"request for {url} failed. response data is {response.text}")
            return None

        # 返回值为null（{"status":1,"msg":"Create Success","data":null}）
        return response.json()["data"]

    def contacts_get(self, headers: dict = {}) -> str:
        """
        获取所有联系人
        :param headers: 请求头
        :return
        """
        logger.info(f"[contacts_get]: admin_get")
        if headers == {}:
            headers = self.session.headers
        # 请求url
        url = f"{self.address}/api/v1/adminbasicservice/adminbasic/contacts"

        # 发送请求、获取响应
        response = self.session.get(url=url, headers=headers)

        if response.status_code != 200 or response.json().get("data") is None:  # 响应错误则忽略并打印日志
            logger.warning(f"request for {url} failed. response data is {response.text}")
            return None

        data = response.json().get("data")  # 用string形式返回
        print(data)
        return data

    def contacts_put(self, contact_id: str, account_id: str = "4d2a46c7-71cb-4cf1-b5bb-b68406d9da6f",
                     contact_name: str = "Contacts_Y", document_type: int = 2,
                     document_number: str = "DocumentNumber_Y", phone_number: str = "19921940900",
                     headers: dict = {}) -> str:
        """
        修改某一联系人信息
        :param contact_id: 新增contact的id
        :param account_id: 新增contact的账户id
        :param contact_name: 新增contact的名称
        :param document_type:
        :param document_number:
        :param phone_number:
        :param headers: 请求头
        :return
        """
        logger.info(f"[contacts_put]: user_account_id:{account_id}")

        if headers == {}:
            headers = self.session.headers
        # 请求url
        url = f"{self.address}/api/v1/adminbasicservice/adminbasic/contacts"

        # 请求载荷，对应@requestbody注解
        payload = {
            "id": contact_id,
            "accountId": account_id,
            "name": contact_name,
            "documentType": document_type,
            "documentNumber": document_number,
            "phoneNumber": phone_number
        }

        # 发送请求、获取响应
        # 对于此put请求而言，如果输入的payload代表的联系人(由id决定)不存在则修改车站信息会抛出异常
        # {"status":0,"msg":"Contacts not found","data":null}
        response = self.session.put(url=url, headers=headers, json=payload)

        if response.status_code != 200 or response.json().get("data") is None:  # 响应错误则忽略并打印日志
            logger.warning(f"request for {url} failed. response data is {response.text}")
            return None

        # 返回值为修改后的联系人信息
        data = response.json().get("data")  # 用string形式返回
        print(data)
        return data

    def contacts_delete(self, contact_id: str = "", headers: dict = {}) -> str:
        """
        删除某一联系人信息
        :param contact_id: 删除contact的id
        :param headers: 请求头
        :return
        """
        logger.info(f"[contacts_delete]: user_account_id:{contact_id}")

        if headers == {}:
            headers = self.session.headers
        # 请求url
        url = f"{self.address}/api/v1/adminbasicservice/adminbasic/contacts" + "/" + contact_id

        # 发送请求、获取响应
        # 对于此delete请求而言，如果输入id代表的联系人不存在也仅仅会返回输入的contactId
        response = self.session.delete(url=url, headers=headers)

        if response.status_code != 200 or response.json().get("data") is None:  # 响应错误则忽略并打印日志
            logger.warning(f"request for {url} failed. response data is {response.text}")
            return None

        # 返回值为输入的contactId
        data = response.json().get("data")  # 用string形式返回
        print(data)
        return data

    # trains相关增删改查
    def trains_post(self, train_id: str = "ManSu", economy_class: int = 2147483647,
                    confort_class: int = 2147483647, average_speed: int = 80,
                    headers: dict = {}) -> str:
        """
        添加车型
        :param train_id: 新增train的id (需要输入)
        :param economy_class: 经济座
        :param confort_class: 商务座
        :param average_speed:平均速度
        :param headers: 请求头
        :return
        """
        logger.info(f"[trains_post]: train_id:{train_id}")

        if headers == {}:
            headers = self.session.headers
        # 请求url
        url = f"{self.address}/api/v1/adminbasicservice/adminbasic/trains"

        # 请求载荷
        payload = {
            "id": train_id,
            "economyClass": economy_class,
            "confortClass": confort_class,
            "averageSpeed": average_speed
        }

        # 发送请求、获取响应
        # 重复添加同一个trainType无影响
        response = self.session.post(url=url, headers=headers, json=payload)

        if response.status_code != 200:  # 响应错误则忽略并打印日志
            logger.warning(f"request for {url} failed. response data is {response.text}")
            return None

        # 返回值新增车型的信息，若为新增的车型则返回None,若新增的车型已经存在则返回train的具体信息
        data = response.json().get("data")  # 用string形式返回
        print(data)
        return data

    def trains_get(self, headers: dict = {}) -> str:
        """
        获取所有车型
        :param headers: 请求头
        :return
        """
        logger.info(f"[trains_get]: admin_get")

        if headers == {}:
            headers = self.session.headers
        # 请求url
        url = f"{self.address}/api/v1/adminbasicservice/adminbasic/trains"

        # 发送请求、获取响应
        response = self.session.get(url=url, headers=headers)

        if response.status_code != 200 or response.json().get("data") is None:  # 响应错误则忽略并打印日志
            logger.warning(f"request for {url} failed. response data is {response.text}")
            return None

        data = response.json().get("data")  # 用string形式返回
        print(data)
        return data

    def trains_put(self, train_id: str = "ManSu", economy_class: int = 2147483647,
                   confort_class: int = 2147483647, average_speed: int = 50,
                   headers: dict = {}) -> str:
        """
        修改某一车型信息
        :param train_id: 新增train的id (需要输入)
        :param economy_class: 经济座
        :param confort_class: 商务座
        :param average_speed:平均速度
        :param headers: 请求头
        :return
        """
        logger.info(f"[trains_put]: train_id:{train_id}")

        if headers == {}:
            headers = self.session.headers
        # 请求url
        url = f"{self.address}/api/v1/adminbasicservice/adminbasic/trains"

        # 请求载荷，对应@requestbody注解
        payload = {
            "id": train_id,
            "economyClass": economy_class,
            "confortClass": confort_class,
            "averageSpeed": average_speed
        }

        # 发送请求、获取响应
        # 对于此put请求而言，如果输入的payload代表的联系人(由id决定)不存在则返回值为false，若修改成功则返回值为true
        response = self.session.put(url=url, headers=headers, json=payload)

        if response.status_code != 200 or response.json().get("data") is None:  # 响应错误则忽略并打印日志
            logger.warning(f"request for {url} failed. response data is {response.text}")
            return None

        # 返回值为true/false
        data = response.json().get("data")  # 用string形式返回
        print(data)
        return data

    def trains_delete(self, train_id: str = "ManSu", headers: dict = {}) -> bool:
        """
        删除某一车型信息
        :param train_id: 删除contact的id
        :param headers: 请求头
        :return
        """
        logger.info(f"[trains_delete]: train_id:{train_id}")

        if headers == {}:
            headers = self.session.headers
        # 请求url
        url = f"{self.address}/api/v1/adminbasicservice/adminbasic/trains" + "/" + train_id

        # 发送请求、获取响应
        # 对于此delete请求而言，如果输入id代表的train不存在会抛出异常
        # {"status":0,"msg":"there is no train according to id","data":null}
        response = self.session.delete(url=url, headers=headers)

        if response.status_code != 200 or response.json().get("data") is None:  # 响应错误则忽略并打印日志
            logger.warning(f"request for {url} failed. response data is {response.text}")
            return None

        # 删除成功 返回值为true
        data = response.json().get("data")  # 用string形式返回
        print(data)
        return data

    # configs相关增删改查
    def configs_post(self, name: str = "ConfigTest", value: str = "0.5",
                     description: str = "ConfigTest Description", headers: dict = {}) -> str:
        """
        添加配置信息config
        :param name: 新增config的名称
        :param value: 值
        :param description: 描述信息
        :param headers: 请求头
        :return
        """
        logger.info(f"[configs_post]: name:{name}")

        if headers == {}:
            headers = self.session.headers
        # 请求url
        url = f"{self.address}/api/v1/adminbasicservice/adminbasic/configs"

        # 请求载荷
        payload = {
            "name": name,
            "value": value,
            "description": description
        }

        # 发送请求、获取响应
        # 重复添加同一个config会抛出异常
        # {"status":0,"msg":"Config ConfigTest already exists.","data":null}
        response = self.session.post(url=url, headers=headers, json=payload)

        if response.status_code != 200 or response.json().get("data") is None:  # 响应错误则忽略并打印日志
            logger.warning(f"request for {url} failed. response data is {response.text}")
            return None

        # 返回值新增配置的信息
        data = response.json().get("data")  # 用string形式返回
        print(data)
        return data

    def configs_get(self, headers: dict = {}) -> str:
        """
        获取所有配置信息
        :param headers: 请求头
        :return
        """
        logger.info(f"[configs_get]: admin_get")

        if headers == {}:
            headers = self.session.headers
        # 请求url
        url = f"{self.address}/api/v1/adminbasicservice/adminbasic/configs"

        # 发送请求、获取响应
        response = self.session.get(url=url, headers=headers)

        if response.status_code != 200 or response.json().get("data") is None:  # 响应错误则忽略并打印日志
            logger.warning(f"request for {url} failed. response data is {response.text}")
            return None

        data = response.json().get("data")  # 用string形式返回
        print(data)
        return data

    def configs_put(self, name: str = "ConfigTest", value: str = "1",
                    description: str = "ConfigTest Description", headers: dict = {}) -> str:
        """
        添加配置信息config
        :param name: 新增config的名称
        :param value: 值
        :param description: 描述信息
        :param headers: 请求头
        :return
        """
        logger.info(f"[configs_put]: name:{name}")

        if headers == {}:
            headers = self.session.headers
        # 请求url
        url = f"{self.address}/api/v1/adminbasicservice/adminbasic/configs"

        # 请求载荷，对应@requestbody注解
        payload = {
            "name": name,
            "value": value,
            "description": description
        }

        # 发送请求、获取响应
        # 对于此put请求而言，如果输入的payload代表的config(由name决定)不存在则抛出异常
        # {"status":0,"msg":"Config ConfigTest11 doesn't exist.","data":null}
        response = self.session.put(url=url, headers=headers, json=payload)

        if response.status_code != 200 or response.json().get("data") is None:  # 响应错误则忽略并打印日志
            logger.warning(f"request for {url} failed. response data is {response.text}")
            return None

        # 返回值为修改后的配置信息
        data = response.json().get("data")  # 用string形式返回
        print(data)
        return data

    def configs_delete(self, name: str = "ConfigTest", headers: dict = {}) -> bool:
        """
        删除某一配置信息
        :param name: 删除config的name
        :param headers: 请求头
        :return
        """
        logger.info(f"[configs_delete]: name:{name}")

        if headers == {}:
            headers = self.session.headers
        # 请求url
        url = f"{self.address}/api/v1/adminbasicservice/adminbasic/configs" + "/" + name

        # 发送请求、获取响应
        # 对于此delete请求而言，如果输入id代表的config不存在会抛出异常
        # {"status":0,"msg":"Config ConfigTest11 doesn't exist.","data":null}
        response = self.session.delete(url=url, headers=headers)

        if response.status_code != 200 or response.json().get("data") is None:  # 响应错误则忽略并打印日志
            logger.warning(f"request for {url} failed. response data is {response.text}")
            return None

        # 删除成功 返回值被删除的配置信息
        data = response.json().get("data")  # 用string形式返回
        print(data)
        return data

    # prices相关增删改查
    def prices_post(self, train_type: str = "DongCheOne",
                    route_id: str = "f3d4d4ef-693b-4456-8eed-59c0d717dd08", basic_price_rate: float = 0.5,
                    first_class_price_rate: float = 1, headers: dict = {}) -> str:
        """
        添加价格price
        # :param price_id: 新增price的id(不需要输入，在创建时自动生成)
        :param train_type: 车型
        :param route_id: 对应route的id
        :param basic_price_rate
        :param first_class_price_rate
        :param headers: 请求头
        :return
        """
        logger.info(f"[prices_post]: train_type:{train_type}")

        if headers == {}:
            headers = self.session.headers
        # 请求url
        url = f"{self.address}/api/v1/adminbasicservice/adminbasic/prices"

        # 请求载荷
        payload = {
            "trainType": train_type,
            "routeId": route_id,
            "basicPriceRate": basic_price_rate,
            "firstClassPriceRate": first_class_price_rate,
        }

        # 发送请求、获取响应
        # 重复添加train_type route_id相等的price会重复添加，因为生成的id不同
        response = self.session.post(url=url, headers=headers, json=payload)

        if response.status_code != 200 or response.json().get("data") is None:  # 响应错误则忽略并打印日志
            logger.warning(f"request for {url} failed. response data is {response.text}")
            return None

        # 返回值新增配置的信息
        data = response.json().get("data")  # 用string形式返回
        print(data)
        return data

    def prices_get(self, headers: dict = {}) -> str:
        """
        获取所有价格信息
        :param headers: 请求头
        :return
        """
        logger.info(f"[prices_get]: admin_get")

        if headers == {}:
            headers = self.session.headers
        # 请求url
        url = f"{self.address}/api/v1/adminbasicservice/adminbasic/prices"

        # 发送请求、获取响应
        response = self.session.get(url=url, headers=headers)

        if response.status_code != 200 or response.json().get("data") is None:  # 响应错误则忽略并打印日志
            logger.warning(f"request for {url} failed. response data is {response.text}")
            return None

        data = response.json().get("data")  # 用string形式返回
        print(data)
        return data

    def prices_put(self, price_id: str, train_type: str = "GaoTie2",
                   route_id: str = "1367db1f-461e-4ab7-87ad-2bcc05fd9cb7", basic_price_rate: float = 0.5,
                   first_class_price_rate: float = 1.2, headers: dict = {}) -> str:
        """
        添加价格price
        :param price_id: price的id(需要输入，用于索引)
        :param train_type: 车型
        :param route_id: 对应route的id
        :param basic_price_rate
        :param first_class_price_rate
        :param headers: 请求头
        :return
        """
        logger.info(f"[prices_put]: train_type:{train_type}")

        if headers == {}:
            headers = self.session.headers
        # 请求url
        url = f"{self.address}/api/v1/adminbasicservice/adminbasic/prices"

        # 请求载荷
        payload = {
            "id": price_id,
            "trainType": train_type,
            "routeId": route_id,
            "basicPriceRate": basic_price_rate,
            "firstClassPriceRate": first_class_price_rate,
        }

        # 发送请求、获取响应
        # 对于此put请求而言，如果输入的payload代表的config(由name决定)不存在则抛出异常
        # {"status":0,"msg":"No that config","data":null}
        response = self.session.put(url=url, headers=headers, json=payload)

        if response.status_code != 200 or response.json().get("data") is None:  # 响应错误则忽略并打印日志
            logger.warning(f"request for {url} failed. response data is {response.text}")
            return None

        # 返回值为修改后的price信息
        data = response.json().get("data")  # 用string形式返回
        print(data)
        return data

    def prices_delete(self, price_id: str, train_type: str = "GaoTie2",
                      route_id: str = "1367db1f-461e-4ab7-87ad-2bcc05fd9cb7", basic_price_rate: float = 0.5,
                      first_class_price_rate: float = 1.2, headers: dict = {}) -> str:
        """
        删除价格price
        :param price_id: price的id(需要输入，用于索引)
        :param train_type: 车型
        :param route_id: 对应route的id
        :param basic_price_rate
        :param first_class_price_rate
        :param headers: 请求头
        :return
        """
        logger.info(f"[prices_delete]: train_type:{train_type}")

        if headers == {}:
            headers = self.session.headers
        # 请求url
        url = f"{self.address}/api/v1/adminbasicservice/adminbasic/prices"

        # 请求载荷
        payload = {
            "id": price_id,
            "trainType": train_type,
            "routeId": route_id,
            "basicPriceRate": basic_price_rate,
            "firstClassPriceRate": first_class_price_rate,
        }

        # 发送请求、获取响应
        # 对于此delete请求而言，如果输入id代表的price不存在会抛出异常
        # {"status":0,"msg":"No that config","data":null}
        response = self.session.delete(url=url, headers=headers, json=payload)

        if response.status_code != 200 or response.json().get("data") is None:  # 响应错误则忽略并打印日志
            logger.warning(f"request for {url} failed. response data is {response.text}")
            return None

        # 删除成功 返回值被删除的配置信息
        data = response.json().get("data")  # 用string形式返回
        print(data)
        return data

    def admin_get_all_routes(self, headers: dict = {}):
        logger.info(f"[admin_get_all_routes]: admin_get")

        if headers == {}:
            headers = self.session.headers

        # 请求url
        url = f"{self.address}/api/v1/adminrouteservice/adminroute"

        # 发送请求、获取响应并出路
        response = self.session.get(url=url, headers=headers)

        if response.status_code != 200 or response.json().get("data") is None:  # 响应错误则忽略并打印日志
            logger.warning(f"request for {url} failed. response data is {response.text}")
            return None

        all_route_info = response.json()["data"]

        return all_route_info

    # 添加线路，车站列表和距离列表形式可以参见文件头部的example
    def admin_add_route(
            self,
            station_list: str = "",
            distance_list: str = "",
            start_station: str = "",
            end_station: str = "",
            headers: dict = {}):
        logger.info(f"[admin_add_route]: station_list:{station_list}")

        if headers == {}:
            headers = self.session.headers

        # 请求url
        url = f"{self.address}/api/v1/adminrouteservice/adminroute"

        payload = {
            "distanceList": f"{distance_list}",
            "endStation": f"{end_station}",
            "startStation": f"{start_station}",
            "stationList": f"{station_list}"
        }
        # 发送请求、获取响应并出路
        response = self.session.post(url=url, headers=headers, json=payload)

        if response.status_code != 200 or response.json().get("data") is None:  # 响应错误则忽略并打印日志
            logger.warning(f"request for {url} failed. response data is {response.text}")
            return None
        logger.info(f"route add success for!")
        return response.json()["data"]

    def admin_delete_route(
            self,
            routeId: str = "",
            headers: dict = {}):
        logger.info(f"[admin_delete_route]: routeId:{routeId}")

        if headers == {}:
            headers = self.session.headers

        # 请求url
        url = f"{self.address}/api/v1/adminrouteservice/adminroute/{routeId}"
        # 发送请求、获取响应并出路
        response = self.session.delete(url=url, headers=headers)

        if response.status_code != 200 or response.json().get("data") is None:  # 响应错误则忽略并打印日志
            logger.warning(f"request for {url} failed. response data is {response.text}")
            return None
        logger.info(f"route delete success for routeID {routeId}")

    def admin_get_all_users(self, headers: dict = {}):
        logger.info(f"[admin_get_all_users]: admin_get")

        if headers == {}:
            headers = self.session.headers

        # 请求url
        url = f"{self.address}/api/v1/adminuserservice/users"

        # 发送请求、获取响应并出路
        response = self.session.get(url=url, headers=headers)

        if response.status_code != 200 or response.json().get("data") is None:  # 响应错误则忽略并打印日志
            logger.warning(f"request for {url} failed. response data is {response.text}")
            return None

        all_user_info = response.json()["data"]

        return all_user_info

    # 添加新用户，其中gender为0和1，document_type选择1为身份证号
    def admin_add_user(
            self,
            document_type: str = "",
            document_num: str = "",
            email: str = "",
            password: str = "",
            username: str = "",
            gender: str = "",
            headers: dict = {}):
        logger.info(f"[admin_add_user]: username:{username}")

        if headers == {}:
            headers = self.session.headers

        # 请求url
        url = f"{self.address}/api/v1/adminuserservice/users"

        payload = {
            "userName": username,
            "password": password,
            "gender": gender,
            "email": email,
            "documentType": document_type,
            "documentNum": document_num
        }

        # 发送请求、获取响应并出路
        response = self.session.post(url=url, headers=headers, json=payload)

        if response.status_code != 200 or response.json().get("data") is None:  # 响应错误则忽略并打印日志
            logger.warning(f"request for {url} failed. response data is {response.text}")
            return None
        logger.info(f"travel add success for {username}!")
        return response.json()["data"]

    def admin_update_user(
            self,
            document_type: str = "",
            document_num: str = "",
            email: str = "",
            password: str = "",
            username: str = "",
            gender: str = "",
            headers: dict = {}):
        logger.info(f"[admin_update_user]: username:{username}")

        if headers == {}:
            headers = self.session.headers

        # 请求url
        url = f"{self.address}/api/v1/adminuserservice/users"

        payload = {
            "userName": username,
            "password": password,
            "gender": gender,
            "email": email,
            "documentType": document_type,
            "documentNum": document_num
        }

        # 发送请求、获取响应并出路
        response = self.session.put(url=url, headers=headers, json=payload)

        if response.status_code != 200 or response.json().get("data") is None:  # 响应错误则忽略并打印日志
            logger.warning(f"request for {url} failed. response data is {response.text}")
            return None
        logger.info(f"travel update success for {username}!")

    def admin_delete_user(
            self,
            user_id: str = "",
            headers: dict = {}):
        logger.info(f"[admin_delete_user]: user_id:{user_id}")

        if headers == {}:
            headers = self.session.headers

        # 请求url
        url = f"{self.address}/api/v1/adminuserservice/users/{user_id}"
        # 发送请求、获取响应并出路
        response = self.session.delete(url=url, headers=headers)

        if response.status_code != 200 or response.json().get("data") is None:  # 响应错误则忽略并打印日志
            logger.warning(f"request for {url} failed. response data is {response.text}")
            return None
        logger.info(f"travel delete success for {user_id}!")

    def admin_get_all_travels(self, headers: dict = {}):
        logger.info(f"[admin_get_all_travels]: admin_get")

        if headers == {}:
            headers = self.session.headers

        # 请求url
        url = f"{self.address}/api/v1/admintravelservice/admintravel"

        # 发送请求、获取响应并出路
        response = self.session.get(url=url, headers=headers)

        if response.status_code != 200 or response.json().get("data") is None:  # 响应错误则忽略并打印日志
            logger.warning(f"request for {url} failed. response data is {response.text}")
            return None

        all_travel_info = response.json()["data"]

        return all_travel_info

    def admin_add_travel(
            self,
            # login_id: str = "",
            trip_id: str = "",
            train_type_id: str = "",
            route_id: str = "",
            # start_station_id: str = "",
            # stations_id: str = "",
            # terminal_station_id: str = "",
            start_time: str = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()),
            # end_time: str = "",
            headers: dict = {}):
        logger.info(f"[admin_add_travel]: trip_id:{trip_id}")

        if headers == {}:
            headers = self.session.headers

        # 请求url
        url = f"{self.address}/api/v1/admintravelservice/admintravel"

        # 获取起始点站
        start_station_name = ""
        terminal_station_name = ""
        routes = self.admin_get_all_routes()
        for route in routes:
            if route.get("id") == route_id:
                start_station_name = route.get("startStation")
                terminal_station_name = route.get("endStation")

        payload = {                                 # 请求的载荷（时间、起始地、目的地）
            "routeId": route_id,
            "startTime": start_time,
            "trainTypeName": train_type_id,
            "tripId": trip_id,
            "startStationName": start_station_name,
            "terminalStationName": terminal_station_name,
        }

        # 发送请求、获取响应并出路
        response = self.session.post(url=url, headers=headers, json=payload)

        if response.status_code != 200:  # 响应错误则忽略并打印日志
            logger.warning(f"request for {url} failed. status code: {response.status_code} response data is {response.text}")
            return None
        logger.info(f"travel add success for {trip_id}!")
        return response.json()["data"]

    def admin_update_travel(
            self,
            # login_id: str = "",
            trip_id: str = "",
            train_type_id: str = "",
            route_id: str = "",
            # start_station_id: str = "",
            # stations_id: str = "",
            # terminal_station_id: str = "",
            start_time: str = "",
            # end_time: str = "",
            headers: dict = {}):
        logger.info(f"[admin_update_travel]: trip_id:{trip_id}")

        if headers == {}:
            headers = self.session.headers

        # 请求url
        url = f"{self.address}/api/v1/admintravelservice/admintravel"

        # 获取起始点站
        start_station_name = ""
        terminal_station_name = ""
        routes = self.admin_get_all_routes()
        for route in routes:
            if route.get("id") == route_id:
                start_station_name = route.get("startStation")
                terminal_station_name = route.get("endStation")

        payload = {  # 请求的载荷（时间、起始地、目的地）
            "routeId": route_id,
            "startTime": start_time,
            "trainTypeName": train_type_id,
            "tripId": trip_id,
            "startStationName": start_station_name,
            "terminalStationName": terminal_station_name,
        }

        # 发送请求、获取响应并出路
        response = self.session.put(url=url, headers=headers, json=payload)

        if response.status_code != 200 or response.json().get("data") is None:  # 响应错误则忽略并打印日志
            logger.warning(f"request for {url} failed. response data is {response.text}")
            return None
        logger.info(f"travel update success for {trip_id}!")

    def admin_delete_travel(
            self,
            trip_id: str = "",
            headers: dict = {}):
        logger.info(f"[admin_delete_travel]: trip_id:{trip_id}")

        if headers == {}:
            headers = self.session.headers

        # 请求url
        url = f"{self.address}/api/v1/admintravelservice/admintravel/{trip_id}"
        # 发送请求、获取响应并出路
        response = self.session.delete(url=url, headers=headers)

        if response.status_code != 200 or response.json().get("data") is None:  # 响应错误则忽略并打印日志
            logger.warning(f"request for {url} failed. response data is {response.text}")
            return None
        logger.info(f"travel delete success for {trip_id}!")

    # order相关增删改查
    def orders_post(self, account_id: str = "4d2a46c7-71cb-4cf1-b5bb-b68406d9da6f", bought_date: str = "1655783404439", travel_date: str = "1501257600000",
                    travel_time: str = "1367629320000",
                    contacts_name: str = "Contacts_One", document_type: int = 1,
                    contacts_document_number: str = "DocumentNumber_One", train_number: str = "G1237",
                    coach_number: int = 1, seat_class: int = 2, seat_number: str = "FirstClass-30",
                    order_from: str = "nanjing", order_to: str = "shanghaihongqiao", status: int = 0,
                    price: str = "100.0", headers: dict = {}) -> str:
        """
        添加订单
        # :param id;  (不需要输入，创建时生成)
        :param bought_date;
        :param travel_date;
        :param travel_time;
        :param account_id;   # Which Account Bought it
        :param contacts_name;     # Tickets bought for whom
        :param document_type;
        :param contacts_document_number;
        :param train_number;
        :param coach_number;
        :param seat_class;
        :param seat_number;
        :param order_from;
        :param order_to;
        :param status;
        :param price;
        :param headers: 请求头
        :return
        """
        logger.info(f"[orders_post]: account_id:{account_id}")

        if headers == {}:
            headers = self.session.headers

        # 请求url
        url = f"{self.address}/api/v1/adminorderservice/adminorder"

        if bought_date == "":
            bought_date = datestr

        if travel_date == "":
            travel_date = datestr

        if travel_time == "":
            travel_time = datestr

        # 请求载荷，对应@requestbody注解
        payload = {
            "boughtDate": bought_date,
            "travelDate": travel_date,
            "travelTime": travel_time,
            "accountId": account_id,
            "contactsName": contacts_name,
            "documentType": document_type,
            "contactsDocumentNumber": contacts_document_number,
            "trainNumber": train_number,
            "coachNumber": coach_number,
            "seatClass": seat_class,
            "seatNumber": seat_number,
            "from": order_from,
            "to": order_to,
            "status": status,
            "price": price
        }

        # 发送请求、获取响应
        response = self.session.post(url=url, headers=headers, json=payload)

        # 功能异常
        # {"timestamp":1655891248872,"status":500,"error":"Internal Server Error",
        # "exception":"org.springframework.web.client.HttpClientErrorException",
        # "message":"403 null","path":"/api/v1/adminorderservice/adminorder"}

        if response.status_code != 200 or response.json().get("data") is None:  # 响应错误则忽略并打印日志
            logger.warning(f"request for {url} failed. response data is {response.text}")
            return None

        data = response.json().get("data")
        print(data)
        return data

    def orders_get(self, headers: dict = {}) -> str:
        """
        获取所有订单信息
        :param headers: 请求头
        :return
        """
        logger.info(f"[orders_get]: admin_get")

        if headers == {}:
            headers = self.session.headers

        # 请求url
        url = f"{self.address}/api/v1/adminorderservice/adminorder"

        # 发送请求、获取响应
        response = self.session.get(url=url, headers=headers)

        if response.status_code != 200 or response.json().get("data") is None:  # 响应错误则忽略并打印日志
            logger.warning(f"request for {url} failed. response data is {response.text}")
            return None

        data = response.json().get("data")  # 用string形式返回
        return data

    def orders_put(self, order_id: str, bought_date: str = "1655783404439", travel_date: str = "1501257600000",
                   travel_time: str = "1367629320000", account_id: str = "4d2a46c7-71cb-4cf1-b5bb-b68406d9da6f",
                   contacts_name: str = "Contacts_Two", document_type: int = 2,
                   contacts_document_number: str = "DocumentNumber_One", train_number: str = "G1237",
                   coach_number: int = 1, seat_class: int = 2, seat_number: str = "FirstClass-30",
                   order_from: str = "nanjing", order_to: str = "shanghaihongqiao", status: int = 0,
                   price: str = "100.0", headers: dict = {}) -> str:
        logger.info(f"[orders_put]: order_id:{order_id}")

        # 请求url
        url = f"{self.address}/api/v1/adminorderservice/adminorder"

        # 请求载荷，对应@requestbody注解
        payload = {
            "id": order_id,
            "boughtDate": bought_date,
            "travelDate": travel_date,
            "travelTime": travel_time,
            "accountId": account_id,
            "contactsName": contacts_name,
            "documentType": document_type,
            "contactsDocumentNumber": contacts_document_number,
            "trainNumber": train_number,
            "coachNumber": coach_number,
            "seatClass": seat_class,
            "seatNumber": seat_number,
            "from": order_from,
            "to": order_to,
            "status": status,
            "price": price
        }

        # 发送请求、获取响应
        # 功能不可用
        response = self.session.put(url=url, headers=headers, json=payload)

        if response.status_code != 200 or response.json().get("data") is None:  # 响应错误则忽略并打印日志
            logger.warning(f"request for {url} failed. response data is {response.text}")
            return None

        # 返回值为修改后的车站信息
        data = response.json().get("data")  # 用string形式返回
        print(data)
        return data

    def orders_delete(self, order_id: str = "", train_number: str = "", headers: dict = {}) -> str:
        """
        删除某一订单信息
        :param order_id: 删除order的id
        :param train_number: 删除order的车型，通过是D/G/K等来判断从order(G/D)还是order_other(K)处理
        :param headers: 请求头
        :return
        """
        logger.info(f"[orders_delete]: order_id:{order_id}")

        if headers == {}:
            headers = self.session.headers

        # 请求url
        url = f"{self.address}/api/v1/adminorderservice/adminorder/{order_id}/{train_number}"

        # 发送请求、获取响应
        # 对于此delete请求而言，order_id为主，train_number中的首字母即D K G等需要正确（其后的数字不正确无影响）
        # order_id不存在或order与对应的车型不匹配 则{"status":0,"msg":"Order Not Exist.","data":null}
        # {"status": 0, "msg": "Station not exist", "data": null}
        response = self.session.delete(url=url, headers=headers)

        if response.status_code != 200 or response.json().get("data") is None:  # 响应错误则忽略并打印日志
            logger.warning(f"request for {url} failed. response data is {response.text}")
            return None

        # 返回值为删除order的信息
        data = response.json().get("data")  # 用string形式返回
        logger.info(data)
        return data


