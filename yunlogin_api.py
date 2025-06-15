import requests
from typing import Dict, List, Optional, Union
from requests.exceptions import RequestException

class YunLoginAPIClient:
    """
    封装 YunLogin API 的客户端类

    示例用法:
    >>> client = YunLoginAPIClient(base_url="https://api.yunlogin.com")
    >>> posts = client.get_posts()
    >>> user = client.get_user(1)
    """

    def __init__(self, base_url: str = "https://api.yunlogin.com", timeout: int = 10):
        """
        初始化 API 客户端
        
        :param base_url: API 基础地址
        :param timeout: 请求超时时间(秒)
        """
        self.base_url = base_url.rstrip('/')
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        })
    
    def _request(self, method: str, endpoint: str, **kwargs) -> Union[Dict, List]:
        """
        内部请求方法，处理所有 API 请求
        
        :param method: HTTP 方法 (get, post, put, delete)
        :param endpoint: API 端点路径
        :param kwargs: 其他 requests 参数
        :return: 解析后的 JSON 响应
        :raises: APIError 当请求失败时
        """
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        
        try:
            response = self.session.request(
                method=method,
                url=url,
                timeout=self.timeout,
                **kwargs
            )
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            raise APIError(f"API 请求失败: {str(e)}") from e
    
    def check_api_status(self) -> Dict[str, Union[int, str]]:
        """
        检查API接口的可用性

        请求示例:
        http://localhost:50213/status
        
        执行成功:
        {
            "code": 0,
            "msg": "success"
        }
        """
        return self._request('get', '/status')
    
    def start_browser(self, account_id: str, headless: Optional[bool] = None) -> Dict:
        """
        启动环境对应的浏览器
        
        :param account_id: 环境ID，环境导入成功后生成的唯一ID
        :param headless: 是否使用无头模式 (不传:否 1:是	)，可选
        :return: 包含浏览器调试信息的字典

        请求示例:
        http://localhost:50213/api/v2/browser/start?account_id=d03ca5de08ec8e02c4b78558ee84d7fc
        
        执行成功:
        {
            "code": 0,
            "data": {
                "ws": {
                    "selenium": "127.0.0.1:xxxx",
                    "puppeteer": "ws://127.0.0.1:xxxx/devtools/browser/xxxxxx"
                },
                "debuggingPort": "xxxx",
                "webdriver": "C:\\xxxx\\chromedriver.exe"
            },
            "msg": "success"
        }

        执行失败:
        {
            "code": -1,
            "data": {},
            "msg": "failed"
        }
        """
        params = {
            'account_id': account_id
        }
        
        if headless is not None:
            params['headless'] = '1' if headless else ''
        
        return self._request('get', '/api/v2/browser/start', params=params)
    
    def stop_browser(self, account_id: str) -> Dict[str, Union[int, str]]:
        """
        关闭环境对应的浏览器
    
        :param account_id: 环境ID，环境导入成功后生成的唯一ID
        :return: 包含执行状态的字典
    
        请求示例:
        http://localhost:50213/api/v2/browser/stop?account_id=d03ce5de86ec8e02c4b78558ee84d7fc
    
        执行成功:
        {
            "code":0,
            "msg":"success"
        }

        执行失败:
        {
            "code":-1,
            "data":{},
            "msg":"failed"
        }
        """
        params = {
            'account_id': account_id
        }

        return self._request('get', '/api/v2/browser/stop', params=params)
    
    def get_browser_status(self, account_id: str) -> Dict[str, Union[int, str, Dict]]:
        """
        获取环境浏览器的启动状态
    
        :param account_id: 环境ID，环境导入成功后生成的唯一ID
        :return: 包含浏览器状态的字典，结构为:
        {
            "code": 0,
            "msg": "success",
            "data": {
                    "status": "running"  # 可能的状态值
            }
        }
    
        请求示例:
        http://localhost:59213/api/v2/browser/status?account_id=69,8e6e9ecbe92c4d9355eeebd97fc
        """
        return self._request('get', '/api/v2/browser/status', params={'account_id': account_id})

    def get_shop_id_list(self) -> Dict:
        """
        获取环境列表id

        请求示例:
        http://localhost:50213/api/v2/userapi/user/shopidlist

        执行成功:
        {
            "code": 0,
            "msg": "Success",
            "data": {
                "shopIds": [
                    "bfd0b654a605f9d53e5a5cdac939d74",
                    "fbd2bc962b08518cb6be1acb8ef00"
                ]
            }
        }

        执行失败:
        {
            "code": -1,
            "msg": "fail message",
            "data": {}
        }
        """
        return self._request('post', '/api/v2/userapi/user/shopidlist')

    def get_shop_serial_list(self) -> Dict:
        """
        获取环境序号列表

        请求示例:
        http://localhost:50213/api/v2/userapi/user/shopseriallist

        执行成功:
        {
            "code": 0,
            "msg": "Success",
            "data": {
                "list": [
                    {
                        "shopId": "b2a354395c06b5e16e",
                        "serial": 96
                    }
                ]
            }
        }

        执行失败:
        {
            "code": -1,
            "msg": "fail message",
            "data": {}
        }
        """
        return self._request('post', '/api/v2/userapi/user/shopseriallist')

    def get_shop_detail_list(self, browser_ids: List[str]) -> Dict:
        """
        获取环境详细信息

        :param browser_ids: 浏览器指纹窗口ID列表
        :return: 包含环境详细信息的字典

        请求示例:
        http://localhost:50213/api/v2/userapi/user/shopdetaillist

        执行成功:
        {
            "code": 0,
            "msg": "Success",
            "data": {
                "browser": [
                    {
                        "name": "测试窗口-1",
                        "browserid": "xxx",
                        "notes": "",
                        "group": {},
                        "label": [],
                        "proxy": {},
                        "accounts": {}
                    }
                ]
            }
        }
        """
        return self._request('post', '/api/v2/userapi/user/shopdetaillist', 
                            json={"browserid": browser_ids})

    def create_group(self, name: str) -> Dict:
        """
        创建新分组

        :param name: 分组名称(2-40个字符)
        :return: 包含创建状态的字典

        请求示例:
        http://localhost:50213/api/v2/userapi/group/create

        执行成功:
        {
            "code": 0,
            "msg": "Success",
            "data": {
                "groupid": "fdrgdgsfgsertgreaay34575422",
                "group": "指纹浏览器测试分组"
            }
        }
        """
        return self._request('post', '/api/v2/userapi/group/create', 
                            json={"name": name})

    def update_group(self, group_id: str, name: str) -> Dict:
        """
        更新分组信息

        :param group_id: 分组ID
        :param name: 分组名称
        :return: 包含更新状态的字典

        请求示例:
        http://localhost:50213/api/v2/userapi/group/update

        执行成功:
        {
            "code": 0,
            "msg": "Success"
        }
        """
        return self._request('post', '/api/v2/userapi/group/update',
                            json={"groupid": group_id, "name": name})

    def get_group_list(self, group: str = "", offer: int = 0, number: int = 20) -> Dict:
        """
        获取分组列表

        :param group: 分组名模糊查询
        :param offer: 开始位置
        :param number: 获取数量(最大20)
        :return: 包含分组列表的字典

        请求示例:
        http://localhost:50213/api/v2/userapi/group/list

        执行成功:
        {
            "code": 0,
            "msg": "Success",
            "data": {
                "group": [
                    {
                        "name": "指纹浏览器测试分组-1",
                        "gropid": "fdrgdgsfgsertgreaay34575422"
                    }
                ]
            }
        }
        """
        return self._request('post', '/api/v2/userapi/group/list',
                            json={"group": group, "offer": offer, "number": number})

    def create_self_proxy(self, proxy_config: Dict) -> Dict:
        """
        创建自有代理

        :param proxy_config: 代理配置信息
        :return: 包含创建状态的字典

        请求示例:
        http://localhost:50213/api/v2/userapi/selfproxy/create

        执行成功:
        {
            "code": 0,
            "msg": "Success"
        }
        """
        return self._request('post', '/api/v2/userapi/selfproxy/create',
                            json={"proxy": proxy_config})

    def delete_self_proxy(self, device_ids: List[str]) -> Dict:
        """
        删除自有代理

        :param device_ids: 代理ID列表
        :return: 包含删除状态的字典

        请求示例:
        http://localhost:50213/api/v2/userapi/selfproxy/delete

        执行成功:
        {
            "code": 0,
            "msg": "Success"
        }
        """
        return self._request('post', '/api/v2/userapi/selfproxy/delete',
                            json={"deviceid": device_ids})

    def get_self_proxy_list(self, page: int, page_size: int, name: str = "") -> Dict:
        """
        获取自有代理列表

        :param page: 页码
        :param page_size: 每页大小
        :param name: 代理名称(可选)
        :return: 包含代理列表的字典

        请求示例:
        http://localhost:50213/api/v2/userapi/selfproxy/list

        执行成功:
        {
            "code": 0,
            "msg": "Success",
            "data": {
                "list": [
                    {
                        "deviceid": "cc12c5e1663e3efcb05e66088XX",
                        "createdat": "2024-04-12 15:58:06"
                    }
                ],
                "total": 1,
                "pageSize": 10,
                "currentPage": 1
            }
        }
        """
        return self._request('post', '/api/v2/userapi/selfproxy/list',
                            json={"page": page, "pageSize": page_size, "name": name})

    def update_self_proxy(self, proxy_config: Dict) -> Dict:
        """
        更新自有代理信息

        :param proxy_config: 代理配置信息，包含deviceid等字段
        :return: 包含更新状态的字典

        请求示例:
        http://localhost:50213/api/v2/userapi/selfproxy/update

        执行成功:
        {
            "code": 0,
            "msg": "Success"
        }
        """
        return self._request('post', '/api/v2/userapi/selfproxy/update',
                            json={"proxy": proxy_config})

    def get_group_plugin_list(self, page: int = 1, page_size: int = 10, sort: str = "") -> Dict:
        """
        获取插件分组列表

        :param page: 页码
        :param page_size: 每页大小
        :param sort: 排序方式(1:正序，非1:倒序)
        :return: 包含插件分组列表的字典

        请求示例:
        http://localhost:50213/api/v2/userapi/plugin/groupPluginList

        执行成功:
        {
            "code": 200,
            "data": {
                "globalPlugin": {
                    "list": [],
                    "count": 1,
                    "pageIndex": 1,
                    "pageSize": 10086
                },
                "userPlugin": {
                    "list": [],
                    "count": 1,
                    "pageIndex": 1,
                    "pageSize": 10086
                }
            },
            "msg": "ok"
        }
        """
        return self._request('post', '/api/v2/userapi/plugin/groupPluginList',
                            json={"page": page, "pageSize": page_size, "sort": sort})

    def bind_group_plugin(self, group_ids: List[str], account_ids: List[str]) -> Dict:
        """
        绑定插件到分组

        :param group_ids: 分组ID列表
        :param account_ids: 环境ID列表
        :return: 包含绑定状态的字典

        请求示例:
        http://localhost:50213/api/v2/userapi/plugin/bindGroupPlugin

        执行成功:
        {
            "code": 200,
            "data": {},
            "msg": "ok"
        }
        """
        return self._request('post', '/api/v2/userapi/plugin/bindGroupPlugin',
                            json={"groupId": group_ids, "accountIds": account_ids})

    def upsert_cookie(self, shop_id: str, cookies: List[Dict]) -> Dict:
        """
        更新或插入Cookie

        :param shop_id: 环境ID
        :param cookies: Cookie配置列表
        :return: 包含更新状态的字典

        请求示例:
        http://localhost:50213/api/v2/userapi/cookie/upsert

        执行成功:
        {
            "code": 0,
            "msg": "Success"
        }
        """
        return self._request('post', '/api/v2/userapi/cookie/upsert',
                            json={"shopid": shop_id, "cookies": cookies})

    def clear_cookie(self, shop_id: str) -> Dict:
        """
        清除Cookie

        :param shop_id: 环境ID
        :return: 包含清除状态的字典

        请求示例:
        http://localhost:50213/api/v2/userapi/cookie/clear

        执行成功:
        {
            "code": 0,
            "msg": "Success"
        }
        """
        return self._request('post', '/api/v2/userapi/cookie/clear',
                            json={"shopid": shop_id})
        
class APIError(Exception):
    """YunLogin API 异常类
    
    用于封装 API 请求过程中发生的错误，包含错误代码和错误消息。
    
    Attributes:
        code (int): 错误代码，0 表示成功，非 0表示失败
        message (str): 错误消息
        data (dict): 附加的错误数据
    """
    
    def __init__(self, message: str, code: int = -1, data: dict = None):
        """
        初始化 APIError 实例
        
        Args:
            message (str): 错误消息
            code (int, optional): 错误代码. 默认为 -1
            data (dict, optional): 附加的错误数据. 默认为 None
        """
        super().__init__(message)
        self.code = code
        self.message = message
        self.data = data or {}
    
    def __str__(self) -> str:
        """返回格式化的错误信息
        
        Returns:
            str: 格式化的错误字符串，包含错误代码和消息
        """
        return f"[错误码:{self.code}] {self.message}"

# 使用示例
if __name__ == "__main__":
    # 创建客户端实例
    client = YunLoginAPIClient(base_url="http://localhost:50213")
    
    try:
        # 检查API状态
        status = client.check_api_status()
        print(f"API状态: {status}")
        
        # 获取环境ID列表
        shop_ids = client.get_shop_id_list()
        print(f"环境ID列表: {shop_ids}")
        
        if shop_ids.get('data', {}).get('shopIds'):
            account_id = shop_ids['data']['shopIds'][0]
            
            # 启动浏览器
            browser = client.start_browser(account_id)
            print(f"浏览器启动状态: {browser}")
            
            # 获取浏览器状态
            status = client.get_browser_status(account_id)
            print(f"浏览器状态: {status}")
            
            # 创建测试分组
            group = client.create_group("测试分组")
            print(f"创建分组结果: {group}")
            
            # 获取分组列表
            groups = client.get_group_list()
            print(f"分组列表: {groups}")
            
            # 关闭浏览器
            stop = client.stop_browser(account_id)
            print(f"浏览器关闭状态: {stop}")
            
    except APIError as e:
        print(f"API 错误: {e}")
    except Exception as e:
        print(f"发生错误: {e}")