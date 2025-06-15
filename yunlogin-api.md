基础信息
GET /status

接口描述：用于检查API接口的可用性。

请求示例
http://localhost:50213/status
返回数据
参数	说明	类型	可选值	默认值
code	执行状态码	int	0:成功 -1:输入格式错误 -2:获取数量异常 -4:账号登录异常	
msg	返回成功或者失败消息	string		
执行成功

{
  "code": 0,
  "msg": "success"
}








基础信息
GET /api/v2/browser/start

接口描述：用于启动环境对应的浏览器，需要指定环境ID，启动成功后可以获取浏览器debug接口用于执行 selenium 和 puppeteer自动化。 Selenium 需要使用到对应内核版本匹配的 Webdriver。启动浏览器后可在返回值中拿到对应的 Webdriver 的路径。

请求参数
参数	说明	类型	必填	可选值	默认值
account_id	环境ID，环境导入成功后生成的唯一ID	string	是		
headless	是否无头浏览器	number	否	不传:否 1:是	不传
请求示例
http://localhost:50213/api/v2/browser/start?account_id=d03ca5de08ec8e02c4b78558ee84d7fc
返回数据
参数	说明	类型	可选值	默认值
code	执行状态码	int	0:成功 -1:输入格式错误 -2:获取数量异常 -4:账号登录异常 -6:未实名认证	
msg	返回成功或者失败消息	string		
data	返回数据	object		
data结构体配置

参数	说明	类型	可选值	默认值
debuggingPort	测试端口	string		
webdriver	浏览器程序位置	string		
ws	websocket信息	object		
ws结构体配置

参数	说明	类型	可选值	默认值
selenium	浏览器debug接口，可用于selenium自动化	string		
puppeteer	浏览器debug接口，可用于puppeteer自动化	string		
执行成功

{
    "code":0,
    "data":{
        "ws":{
            "selenium":"127.0.0.1:xxxx",
            "puppeteer":"ws://127.0.0.1:xxxx/devtools/browser/xxxxxx"
        },
        "debuggingPort":"xxxx",
        "webdriver":"C:\xxxx\chromedriver.exe"
    },
    "msg":"success"
}
执行失败

{
    "code":-1,
    "data":{},
    "msg":"failed"
}










基础信息
GET /api/v2/browser/stop

接口描述：用于关闭环境对应的浏览器，需要指定环境ID。

请求参数
参数	说明	类型	必填	可选值	默认值
account_id	环境ID，环境导入成功后生成的唯一ID	string	是		
请求示例
http://localhost:50213/api/v2/browser/stop?account_id=d03ca5de08ec8e02c4b78558ee84d7fc
返回数据
参数	说明	类型	可选值	默认值
code	执行状态码	int	0:成功 -1:输入格式错误 -2:获取数量异常 -4:账号登录异常	
msg	返回成功或者失败消息	string		
执行成功

{
    "code":0,
    "msg":"success"
}
执行失败

{
    "code":-1,
    "data":{},
    "msg":"failed"
}











基础信息
GET /api/v2/browser/status

接口描述：用于环境浏览器的启动状态，需要指定环境ID。

请求参数
参数	说明	类型	必填	可选值	默认值
account_id	环境ID，环境导入成功后生成的唯一ID	string	是		
请求示例
http://localhost:50213/api/v2/browser/status?account_id=d03ca5de08ec8e02c4b78558ee84d7fc
返回数据
参数	说明	类型	可选值	默认值
code	执行状态码	int	0:成功 -1:输入格式错误 -2:获取数量异常 -4:账号登录异常	
msg	返回成功或者失败消息	string		
data	返回成功数据	object		
data结构体配置

参数	说明	类型	可选值	默认值
status	浏览器状态	string	“Active”:浏览器已打开运行中 “Inactive”:浏览器未打开	
ws	websocket信息	object		
ws结构体配置

参数	说明	类型	可选值	默认值
selenium	浏览器debug接口，可用于selenium自动化	string		
puppeteer	浏览器debug接口，可用于puppeteer自动化	string		
执行成功

{
    "code":0,
    "data":{
        "status":"Active",
        "ws":{
            "selenium":"127.0.0.1:xxxx",
            "puppeteer":"ws://127.0.0.1:xxxx/devtools/browser/xxxxxx"
        }
    }
}
执行失败

{
    "code":-1,
    "data":{},
    "msg":"failed"
}










基础信息
POST /api/v2/userapi/user/shopidlist

请求参数
无

请求示例
http://localhost:50213/api/v2/userapi/user/shopidlist
返回数据
参数	说明	类型	可选值	默认值
code	执行状态码	int	0:成功 -1:输入格式错误 -2:获取数量异常 -4:账号登录异常	
msg	返回成功或者失败消息	string		
shopIds	返回的环境列表id	[]string		
执行成功

{
    "code": 0,
    "msg": "Success",
    "data": {
        "shopIds": [
            "bfd0b654a605f9d53e5a5cdac939d74",
            "fbd2bc962b08518cb6be1acb8ef00",
            "b0d6326c9f05c91dccb72e59f083",
            "0d5fcf6d3df35b2bbfcdd5abd8b9",
            "24b6eed92e3a88e8d7f5a71ab0dc",
            "a75e5c7346650f4baa1cc8176e613",
            "a3c9a8923268f77637ef2cbd4a1e7"
        ]
    }
}
执行失败

{
    "code": -1,
    "msg": "fail message",
    "data": {}
}
















基础信息
POST /api/v2/userapi/user/shopseriallist

请求参数
无

请求示例
http://localhost:50213/api/v2/userapi/user/shopseriallist
返回数据
参数	说明	类型	可选值	默认值
code	执行状态码	int	0:成功 -1:输入格式错误 -2:获取数量异常 -4:账号登录异常	
msg	返回成功或者失败消息	string		
shopId	返回的环境id	string		
serial	返回的环境序号	int		
执行成功

{
    "code": 0,
    "msg": "Success",
    "data": {
        "list": [
            {
                "shopId": "b2a354395c06b5e16e",
                "serial": 96
            },
            {
                "shopId": "ebf96c272b708c944ef1a16",
                "serial": 89
            },
            {
                "shopId": "e7fd6d69588b5de2dffdd3f2",
                "serial": 88
            },
            {
                "shopId": "d4a41c1f5329addd406c5b4",
                "serial": 10
            }
        ]
    }
}
执行失败

{
    "code": -1,
    "msg": "fail message",
    "data": {}
}

















基础信息
POST /api/v2/userapi/user/shopdetaillist

请求参数
参数	说明	类型	必填	可选值	默认值
browserid	浏览器指纹窗口ID	[]string	是		
请求示例
http://localhost:50213/api/v2/userapi/user/shopdetaillist
请求体
{
    "browserid": [
        "d03ca5de08ec8e02c4b78558ee84d7fc",
        "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    ]
}
返回数据
参数	说明	类型	可选值	默认值
code	执行状态码	int	0:成功 -1:输入格式错误 -2:获取数量异常 -4:账号登录异常	
msg	返回成功或者失败消息	string		
data	返回成功数据	object		
browser	浏览器指纹窗口列表	[]object		
browser 结构体数组：

参数	说明	类型	可选值	默认值
name	指纹浏览器的名称	string		
browserid	要修改浏览器窗口的ID号	string		
notes	备注	string		
is_star_tag	是否星标	int	1:星标 0:未星标	0
serial	序号	int		
cookie	cookie json字符串	string		
group	分组 详见group结构体配置	object		
label	标签 详见label结构体配置	object		
proxy	代理信息（详见proxy结构体配置）	object		
accounts	详见accounts结构体配置	object		
fingerprint	详见fingerprint结构体配置	object		
group结构体配置：

参数	说明	类型	可选值	默认值
name	分组名	string		
groupid	分组id	string		
label结构体配置：

参数	说明	类型	可选值	默认值
name	标签名	string		
id	标签id	string		
proxy结构体配置：

参数	说明	类型	可选值	默认值
inlie	代理类型	string	official:代理类型 self:自有代理 official:官方代理 local:本地 general:通用代理	local
uuid	设备ID	string		
type	协议类型	string	http、https、socks5	socks5
product	inlie 设置为 official 时设置这个选项	int	0:无 1:云平台 2:家庭宽带, 3:国内动态 4:海外动态	0
PublicIP	您的代理公网出口 IP 用于定位使用的 IP，如果为空会无法进行 IP 定位择优配置浏览器指纹信息	string		
socks5	socks5代理（详见socks5结构体配置）	object		
http	http代理（详见http结构体配置）	object		
https	https代理（详见https结构体配置）	object		
socks5结构体配置：

参数	说明	类型	可选值	默认值
Addr	代理地址	string		
User	用户名	string		
Passwd	密码	string		
http 结构体配置：

参数	说明	类型	可选值	默认值
Addr	代理地址	string		
User	用户名	string		
Passwd	密码	string		
https 结构体配置：

参数	说明	类型	可选值	默认值
Addr	代理地址	string		
User	用户名	string		
Passwd	密码	string		
accounts结构体配置：

参数	说明	类型	可选值	默认值
url	浏览器打开时访问的其他url地址	[]string		
name	网址或者名称	string		
user	平台账号	string		
passwd	平台密码	string		
lock	锁定账号	int	1:锁定 0:不锁定	0
enableself	是否是用户自定义平台	int	0:平台提供的 1:用户自定义的	0
loginurl	平台提供的网站访问地址	string		
finger 结构体配置：

参数	说明	类型	可选值	默认值
kernel	浏览器信息	string	Chrome	Chrome
kernelversion	浏览器内核版本	string	107，119，122	122
UAversion	浏览器本号	int		
system	操作系统版本	string		
ua	UserAgent 信息	string		
language	浏览器的语言	[]string		
zone	时区	string		
geographic	地理位置 （详见geographic结构体配置）	object		
dpi	平面分辨率	string	分隔符x(示例:1920x1080)	默认
fontfinger	字体列表	int	1	1
font	字体列表	object(详见font结构体配置)		
WebRTC	Chrome 即时通信组件	int	0:禁用,网站会拿不到IP 1:真实,网站会获取真实IP 2:替换,使用代理IP覆盖真实IP 3:转发,IP代理场景使用	0
WebRTCIP	内网ip；WebRTC设置为2时配置	string		
Canvas	浏览器canvas指纹开关	int	0:倾向一致性 1:关闭 2:倾向随机性	0
WebGl	浏览器webgl元数据指纹开关	int	1:隐身 2:真实	1
WebGlInfo	根据WebGl生成	int	0:关闭 1:真实 2:自定义 3:自动生成	2
WebGLVendor	根据WebGl生成	string	Google Inc. (Intel)、Google Inc. (AMD)、Google Inc. (NVIDIA)	Google Inc. (Intel)
WebGLRenderer	根据WebGl生成	string		
AudioContext	音频流	int	1:隐身 2:真实	1
SpeechVoices	SpeechVoices指纹	int	1:每个浏览器使用当前电脑默认的SpeechVoices 2:添加相应的噪音，同一电脑上为每个浏览器生成不同的SpeechVoices	1
mediadevice	媒体设备开关	int	1:关闭（每个浏览器使用当前电脑默认的媒体设备id）2:启用（使用相匹配的值代替您真实的媒体设备ID，噪声）	1
cpu	CPU 核心数量	int		
mem	内存参数	int		
devicename	计算机名	string		
mac	MAC 地址	string		
hardware	硬件加速	int	0:关闭 1:开启 2:默认	1
Bluetooth	蓝牙	int	0:关闭 1:开启	0
Donottrack	“请勿跟踪”浏览器设置	int	1:不启用 2:启用 3:默认	1
battery	电池	int	0:禁止 1:真实	1
enablescanport	端口扫描防护	int	1:开启 2:关闭	1
scanport	当EnableScanPort是1本地端口,白名单0~65535关闭状态不写	string		
enableCookie	Cookie共享设置	int	0:按用户 1:安环境	1
enableopen	多开设置	int	0:关闭 1:开启 2:跟随团队	1
enablenotice	网页通知	int	0:禁止通知 1:询问	1
enablepic	禁止加载图片	int	0:关闭 1:开启 2:跟随团队	0
picsize	图片大小	string		
Enablesound	禁止播放声音	int	0:关闭 1:开启 2:跟随团队	0
Enablevideo	禁止加载视频	int	0:关闭 1:开启 2:跟随团队	0
geographic 结构体配置：

参数	说明	类型	可选值	默认值
enable	地理位置设置	int	1:启用 2:询问 3:禁止	1
user	定位方式	int	1:使用ip定位 2:自定义	1
longitude	经度(当enable等于2且UseIP等于0时使用)	string	-180 - 180	
latitude	纬度(当enable等于2且UseIP等于0时使用)	string	-90 - 90	
accuracy	精度（米）(当enable等于2且UseIP等于0时使用)	string	10 - 5000	
font结构体配置：

参数	说明	类型	可选值	默认值
enable	字体保护	int	0:关闭 1:开启	1
list	字体列表当enable为0时设置,可选值往数组中添加	[]string	“Roboto”,“Tahoma”,“Google Sans”,“Helvetica”,“arial”,“default”,“sans-serif”,“serif”,“cursive”,“monospace”…	[“Arial”,“Calibri”,“Cambria Math”,“Cambria”,“Candara”,“Comic Sans MS”,“Consolas”,“Constantia”,“Corbel”,“Courier New”,“Ebrima”,“Franklin Gothic”,“Gabriola”,“Georgia”,“Impact”,“Lucida Console”,“Lucida Sans Unicode”,“MS Gothic”,“MS PGothic”,“MV Boli”,“Malgun Gothic”,“Marlett”,“Microsoft Himalaya”,“Microsoft JhengHei”,“Microsoft New Tai Lue”,“Microsoft PhagsPa”,“Microsoft Sans Serif”,“Microsoft YaHei”,“Microsoft Yi Baiti”,“MingLiU-ExtB”,“Mongolian Baiti”,“PMingLiU-ExtB”,“Palatino Linotype”,“Segoe Print”,“Segoe Script”,“Segoe UI Symbol”,“Segoe UI”,“SimSun”,“SimSun-ExtB”,“Sylfaen”,“Trebuchet MS”,“Verdana”,“Webdings”,“Gadugi”,“Javanese Text”,“Microsoft JhengHei UI”,“Myanmar Text”,“Sitka Small”,“Yu Gothic”,“MS UI Gothic”,“Microsoft Tai Le”,“MingLiU_HKSCS-ExtB”,“Symbol”,“Segoe UI Emoji”,“Bahnschrift”]
执行成功

{
    "code": 0,
    "msg": "Success",
    "data": {
        "browser": [
            {
                "browserid": "608b78e0c121e262712eaeaba1aa98e1",
                "name": "云登浏览器_3",
                "notes": "",
                "group": {
                    "name": "",
                    "groupid": ""
                },
                "label": [
                    {
                        "id": "3d4d05c941167a6e083ed7361a4c2167",
                        "name": "14654"
                    }
                ],
                "is_star_tag": 0,
                "proxy": {
                    "name": "",
                    "inlie": "local",
                    "uuid": "",
                    "type": "",
                    "product": 0,
                    "PublicIP": "",
                    "socks5": {
                        "Addr": "",
                        "User": "",
                        "Passwd": ""
                    },
                    "http": {
                        "Addr": "",
                        "User": "",
                        "Passwd": ""
                    },
                    "https": {
                        "Addr": "",
                        "User": "",
                        "Passwd": ""
                    }
                },
                "serial": 0,
                "cookie": "[]",
                "accounts": {
                    "loginurl": "",
                    "enableself": 1,
                    "url": [],
                    "name": "https://www.bilibili.com/",
                    "user": "",
                    "passwd": "",
                    "lock": 0
                },
                "fingerprint": {
                    "kernel": "Chrome",
                    "kernelversion": "107",
                    "system": "Windows 10",
                    "nextsystem": {
                        "Android": "",
                        "MacOS": "",
                        "IOS": "",
                        "Linux": ""
                    },
                    "UAversion": "106",
                    "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.60 Safari/537.36",
                    "language": [],
                    "uilanguage": null,
                    "zone": "",
                    "geographic": {
                        "enable": 1,
                        "user": 1,
                        "longitude": "",
                        "latitude": "",
                        "accuracy": ""
                    },
                    "dpi": "默认",
                    "widowssize": "默认",
                    "font": {
                        "enable": 1,
                        "list": []
                    },
                    "fontfinger": 1,
                    "WebRTC": 0,
                    "WebRTCIP": "",
                    "Canvas": 0,
                    "WebGl": 1,
                    "WebGlInfo": 2,
                    "WebGLVendor": "Google Inc. (Intel)",
                    "WebGLRenderer": "ANGLE (Intel, Intel(R) UHD Graphics 620 Direct3D11 vs_5_0 ps_5_0, D3D11-27.20.100.8984)",
                    "AudioContext": 1,
                    "SpeechVoices": 1,
                    "mediadevice": 1,
                    "cpu": 12,
                    "mem": 4,
                    "devicename": "DESKTOP-fRMTued",
                    "mac": "8C-04-BA-87-2A-5E",
                    "hardware": 1,
                    "Bluetooth": 0,
                    "Donottrack": 1,
                    "battery": 1,
                    "enablescanport": 1,
                    "scanport": "",
                    "enableCookie": 1,
                    "enableopen": 1,
                    "enablenotice": 1,
                    "enablepic": 0,
                    "picsize": "",
                    "Enablesound": 0,
                    "Enablevideo": 0
                }
            }
        ]
    }
}
执行失败

{
    "code": -1,
    "msg": "fail message",
    "data": {
        "browser": null
    }
}

















基础信息
POST /api/v2/userapi/group/create

请求参数
参数	说明	类型	必填	可选值	默认值
name	分组名称	string	是	2到40个长度字符	
请求示例
http://localhost:50213/api/v2/userapi/group/create
请求体
{
    "name": "xxx"
}
返回数据
参数	说明	类型	必填	可选值	默认值
code	执行状态码	int	0:成功 -1:输入格式错误 -2:分组名称太长或者太短 -3:这个组名已经创建了 -4:账号登录异常		
msg	返回成功或者失败消息	string			
data	返回数据	object			
data结构体配置

参数	说明	类型	必填	可选值	默认值
groupid	新建的分组ID	string			
group	新建的分组名	string			
执行成功

{
    "code":0,
    "msg":"Success",
    "data":{
        "groupid":"fdrgdgsfgsertgreaay34575422",
        "group":"指纹浏览器测试分组"
    }
}
执行失败

{
    "code": -1,
    "msg": "fail message",
    "data": {
        "groupid": "",
        "group": ""
    }
}


















基础信息
POST /api/v2/userapi/group/update

请求参数
参数	说明	类型	必填	可选值	默认值
groupid	分组ID	string	是		
name	分组名称	string	否	2到40个长度字符	
请求示例
http://localhost:50213/api/v2/userapi/group/update
请求体
{
    "groupid":"9d19597b113ac7ed81225af48c364881",
    "name":"分组测试"
}
返回数据
参数	说明	类型	可选值	默认值
code	执行状态码	int	0:成功 -1:输入格式错误 -2:分组名称太长或者太短 -4:账号登录异常	
msg	返回成功或者失败消息	string		
执行成功

{
  "code": 0,
  "msg": "Success"
}
执行失败

{
    "code": -2,
    "msg": "fail message",
}


















基础信息
POST /api/v2/userapi/group/list

请求参数
参数	说明	类型	必填	可选值	默认值
group	分组名模糊	string	否		
offer	从第offer条开始计算	int	是	offer最小是0	
number	需要提取的条数	int	是	最大不超过20	
请求示例
http://localhost:50213/api/v2/userapi/group/list
请求体
{
    "group": "xxx",
    "offer": 1,
    "number": 20
}
返回数据
参数	说明	类型	可选值	默认值
code	执行状态码	int	0:成功 -1:输入格式错误 -2:获取数量异常 -4:账号登录异常	
msg	返回成功或者失败消息	string		
name	分组名	string		
gropid	分组ID	string		
执行成功

{
    "code":0,
    "msg":"Success",
    "data":{
        "group":[
            {
                "name":"指纹浏览器测试分组-1",
                "gropid":"fdrgdgsfgsertgreaay34575422"
            },
            {
                "name":"指纹浏览器测试分组-2",
                "gropid":"fd2rgdgsfgsert3reaa44575424"
            }
        ]
    }
}
执行失败

{
    "code": -2,
    "msg": "fail message",
    "data": {
        "group": null
    }
}

























基础信息
POST /api/v2/userapi/user/create

请求参数
browser 结构体数组，要配置的参数信息（详见：browser）

browser 结构体数组，格式如下：

参数	说明	类型	必填	可选值	默认值
name	浏览器名称	string	是		
proxy	代理信息（详见proxy配置）	object	是		
accounts	账号相关信息（详见accounts配置）	object	否		
accountsv2	账号相关信息（详见accountsv2配置）	[]object	否		
finger	浏览器指纹信息（详见finger配置）	object	否		
proxy 结构体配置：

参数	说明	类型	必填	可选值	默认值
type	代理类型	string	是	self(自有代理)、general(代理API)、socks5、http、https、local(本地)	
uuid	代理ID号,当type是self、general的时候必填，可以从UI界面的自有代理、代理API列表中查看	string	否		
region	国家代号，当type是general的时候必填（详见 region 配置）	string	否		
PublicIP	你的代理公网出口 IP 用于定位使用的 IP，如果为空会无法进行 IP 定位择优配置浏览器指纹信息	string	否		
socks5	代理信息 当 type 设置为 socks5 时设置这个选项（详见 socks5 配置）	object	否		
http	代理信息 当 type 设置为 http 时设置这个选项（详见http 配置）	object	否		
https	代理信息 当 type 设置为 https 时设置这个选项（详见 https 配置）	object	否		
ipChannel	代理检测渠道，默认ipdata	string	否	海外代理：ip2location，国内代理：ipdata	
socks5 结构体配置：

参数	说明	类型	必填	可选值	默认值
Addr	代理地址	string	是		
User	用户名	string	否		
Passwd	密码	string	否		
http 结构体配置：

参数	说明	类型	必填	可选值	默认值
Addr	代理地址	string	是		
User	用户名	string	否		
Passwd	密码	string	否		
https 结构体配置：

参数	说明	类型	必填	可选值	默认值
Addr	代理地址	string	是		
User	用户名	string	否		
Passwd	密码	string	否		
accounts 结构体配置：

参数	说明	类型	必填	可选值	默认值
openurls	浏览器打开时访问的 url 地址	[]string	否		
groupid	分组 ID 创建的新指纹环境分组到指定的位置	string	否		
cookie	要打开环境的 cookie , 账号和 cookie 不能同时填写，此字段值为空时表示不存储cookie数据，如果需要同步cookie, 此字段必填, 请传"[]"	string	否		
accountsv2 结构体配置：

参数	说明	类型	必填	可选值	默认值
url	账号管理平台地址	string	否		
user	账号管理账号	string	否		
password	账号管理密码	string	否		
finger 结构体配置：

参数	说明	类型	必填	可选值	默认值
kernelversion	kernelversion 浏览器内核大版本号	string	否	107，119，122	107
UaVersion	浏览器大版本号	int	否	目前支持 100-117 不传自动生成	
System	操作系统版本	string	否	目前支持（Windows 7、Windows 8、Windows 8.1、Windows 10、Windows 11、IOS 14、IOS 15、IOS 16、Android 9、Android 10、Android 11、Android 12、Android 13、MacOS 10、MacOS 11、MacOS 12、MacOS 13) 不传会自动生成All Windows, “All Windows”:是在所有支持的Windows操作系统中自动生成; “All IOS”:在所有支持的IOS系统中生成; “All Android”:在所有Android系统中随机 All MacOS:在所有MacOS中随机。	
UserAgent	UserAgent 不写根据系统和浏览器版本自动生成	string	否		
Language	浏览器的语言 不传会根据代理 IP 地址自动生成 详细看支持的语言详细列表(如果是使用动态 IP 自动生成为中文)	[]string	否		
Zone	时区 不传会根据代理 IP 地址自动生成 详细查看时区支持的列表(如果是使用动态 IP 自动生成为北京时间)	string	否		
DPI	平面分辨率	string	否	分隔符x(示例:1920x1080),空自动生成	默认
FontList	字体列表 不传系统自动生成	[]string	否		
WebRTC	Chrome 即时通信组件	int	否	0:禁用,网站会拿不到IP 1:真实,网站会获取真实IP 2:替换,使用代理IP覆盖真实IP 3:转发,IP代理场景使用	0
WebRTCIP	内网ip；WebRTC设置为2时配置	string	否		
Canvas	浏览器canvas指纹开关	int	否	0:倾向一致性 1:关闭 2:倾向随机性	0
WebGl	浏览器webgl元数据指纹开关	int	否	1:隐身 2:真实	1
AudioContext	音频流	int	否	1:隐身 2:真实	1
SpeechVoices	SpeechVoices指纹	int	否	1:每个浏览器使用当前电脑默认的SpeechVoices 2:添加相应的噪音，同一电脑上为每个浏览器生成不同的SpeechVoices	1
MediaDevice	媒体设备开关	int	否	1:关闭（每个浏览器使用当前电脑默认的媒体设备id）2:启用（使用相匹配的值代替您真实的媒体设备ID，噪声）	1
Cpu	CPU 核心数量 不传会自动生成	int	否		
Mem	内存参数 不传会自动生成	float64	否		
DeviceName	计算机名	string	否	15个字符长度以内, 不传会自动生成	
Mac	MAC 地址 不传会自动生成	string	否		
Hardware	硬件加速	int	否	0:关闭 1:开启 2:默认	1
Bluetooth	蓝牙	int	否	0:关闭 1:开启	0
DoNotTrack	“请勿跟踪”浏览器设置	int	否	1:不启用 2:启用 3:默认	1
EnableScanPort	端口扫描防护	int	否	1:开启 2:关闭	1
ScanPort	白名单 0~65535 关闭状态不写 当 EnableScanPort 是 1 时这里为空会自动生成本地端口	[]int	否		
geographic	地理位置 （默认使用 IP 定位 动态代理 IP 不支持次选项为禁止）	object	否		
geographic 结构体配置：

参数	说明	类型	必填	可选值	默认值
enable	地理位置设置	int	否	1:启用 2:询问 3:禁止	1
user	定位方式	int	否	1:使用ip定位 2:自定义	1
longitude	经度(当enable等于2且UseIP等于0时使用)	string	否	-180 - 180	
latitude	纬度(当enable等于2且UseIP等于0时使用)	string	否	-90 - 90	
accuracy	精度（米）(当enable等于2且UseIP等于0时使用)	string	否	10 - 5000	
region 结构体配置：

大洲	国家及代号
亚洲	中国 (CN)、中国台湾（TW）、中国香港（HK）、中国澳门（MO）、日本 (JP)、韩国 (KR)、印度 (IN)、伊朗 (IR)、伊拉克 (IQ)、沙特阿拉伯 (SA)、阿联酋 (AE)、以色列 (IL)、卡塔尔 (QA)、阿曼 (OM)、也门 (YE)、叙利亚 (SY)、黎巴嫩 (LB)、约旦 (JO)、巴勒斯坦 (PS)、土耳其 (TR)、塞浦路斯 (CY)、格鲁吉亚 (GE)、亚美尼亚 (AM)、阿塞拜疆 (AZ)、阿富汗 (AF)、巴基斯坦 (PK)、孟加拉 (BD)、不丹 (BT)、尼泊尔 (NP)、斯里兰卡 (LK)、马尔代夫 (MV)、缅甸 (MM)、泰国 (TH)、老挝 (LA)、柬埔寨 (KH)、越南 (VN)、马来西亚 (MY)、新加坡 (SG)、印度尼西亚 (ID)、文莱 (BN)、菲律宾 (PH)、东帝汶 (TL)
欧洲	英国 (GB)、法国 (FR)、德国 (DE)、意大利 (IT)、西班牙 (ES)、葡萄牙 (PT)、荷兰 (NL)、比利时 (BE)、卢森堡 (LU)、瑞士 (CH)、奥地利 (AT)、匈牙利 (HU)、捷克 (CZ)、斯洛伐克 (SK)、波兰 (PL)、罗马尼亚 (RO)、保加利亚 (BG)、希腊 (GR)、塞尔维亚 (RS)、黑山 (ME)、克罗地亚 (HR)、斯洛文尼亚 (SI)、北马其顿 (MK)、波黑 (BA)、阿尔巴尼亚 (AL)、冰岛 (IS)、丹麦 (DK)、挪威 (NO)、瑞典 (SE)、芬兰 (FI)、爱尔兰 (IE)、摩纳哥 (MC)、列支敦士登 (LI)、圣马力诺 (SM)、梵蒂冈 (VA)、爱沙尼亚 (EE)、拉脱维亚 (LV)、立陶宛 (LT)、摩尔多瓦 (MD)
非洲	埃及 (EG)、利比亚 (LY)、突尼斯 (TN)、阿尔及利亚 (DZ)、摩洛哥 (MA)、毛里塔尼亚 (MR)、塞内加尔 (SN)、冈比亚 (GM)、几内亚 (GN)、几内亚比绍 (GW)、塞拉利昂 (SL)、利比里亚 (LR)、科特迪瓦 (CI)、加纳 (GH)、多哥 (TG)、贝宁 (BJ)、尼日尔 (NE)、尼日利亚 (NG)、喀麦隆 (CM)、赤道几内亚 (GQ)、乍得 (TD)、中非 (CF)、苏丹 (SD)、南苏丹 (SS)、埃塞俄比亚 (ET)、厄立特里亚 (ER)、索马里 (SO)、吉布提 (DJ)、肯尼亚 (KE)、坦桑尼亚 (TZ)、乌干达 (UG)、卢旺达 (RW)、布隆迪 (BI)、塞舌尔 (SC)、毛里求斯 (MU)、马达加斯加 (MG)、科摩罗 (KM)、莫桑比克 (MZ)、马拉维 (MW)、赞比亚 (ZM)、津巴布韦 (ZW)、博茨瓦纳 (BW)、纳米比亚 (NA)、南非 (ZA)、斯威士兰 (SZ)、莱索托 (LS)、圣多美和普林西比 (ST)、佛得角 (CV)
美洲	加拿大 (CA)、美国 (US)、墨西哥 (MX)、危地马拉 (GT)、伯利兹 (BZ)、萨尔瓦多 (SV)、洪都拉斯 (HN)、尼加拉瓜 (NI)、哥斯达黎加 (CR)、巴拿马 (PA)、巴哈马 (BS)、古巴 (CU)、牙买加 (JM)、海地 (HT)、多米尼加 (DO)、圣基茨和尼维斯 (KN)、安提瓜和巴布达 (AG)、多米尼克 (DM)、圣卢西亚 (LC)、圣文森特和格林纳丁斯 (VC)、格林纳达 (GD)、巴巴多斯 (BB)、特立尼达和多巴哥 (TT)、哥伦比亚 (CO)、委内瑞拉 (VE)、圭亚那 (GY)、苏里南 (SR)、法属圭亚那 (GF)、厄瓜多尔 (EC)、秘鲁 (PE)、巴西 (BR)、玻利维亚 (BO)、智利 (CL)、阿根廷 (AR)、乌拉圭 (UY)、巴拉圭 (PY)
大洋洲	澳大利亚 (AU)、新西兰 (NZ)、巴布亚新几内亚 (PG)、所罗门群岛 (SB)、瓦努阿图 (VU)、斐济群岛 (FJ)、基里巴斯 (KI)、密克罗尼西亚联邦 (FM)、马绍尔群岛 (MH)、帕劳 (PW)、图瓦卢 (TV)、萨摩亚 (WS)、汤加 (TO)、法属波利尼西亚 (PF)、新喀里多尼亚 (NC)、瓦利斯和富图纳 (WF)、美属萨摩亚 (AS)、关岛 (GU)、北马里亚纳群岛 (MP)、荷属加勒比区 (BQ)、库拉索 (CW)、阿鲁巴 (AW)、荷属圣马丁 (SX)、法属圣马丁 (MF)、奥兰群岛 (AX)、根西岛 (GG)、泽西岛 (JE)、马恩岛 (IM)、直布罗陀 (GI)、格陵兰 (GL)、法罗群岛 (FO)、安圭拉 (AI)、百慕大 (BM)、开曼群岛 (KY)、特克斯和凯科斯群岛 (TC)
请求示例
http://localhost:50213/api/v2/userapi/user/create
请求体
注意：如果需要同步cookie, 此字段必填, 请传"[]"

{
  "browser": [
    {
      "name": "指纹浏览器",
      "proxy": {
        "uuid": "",
        "PublicIP": "",
        "type": "local",
        "region": "",
        "https": {
          "Addr": ""
        }
      },
      "accounts": {
        "openurls": [
          ""
        ],
        "groupid": "",
        "cookie": ""
      },
      "accountsv2": [
        {
          "url": "",
          "password": "",
          "user": ""
        }
      ],
      "finger": {
        "kernelversion": "107",
        "UAversion": 107,
        "System": "windows 10",
        "UserAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6237.0 Safari/537.36",
        "Language": [],
        "Zone": "",
        "DPI": "随机",
        "FontList": [],
        "WebRTCIP": "",
        "Canvas": 2,
        "WebGl": 1,
        "WebGLVendor": "Google Inc. (NVIDIA)",
        "AudioContext": 1,
        "SpeechVoices": 1,
        "MediaDevice": 1,
        "Cpu": 8,
        "Mem": 2,
        "DeviceName": "",
        "Mac": "",
        "Hardware": 1,
        "Bluetooth": 1,
        "DoNotTrack": 1,
        "EnableScanPort": 1,
        "ScanPort": [
          155
        ],
        "geographic": {
          "enable": 1,
          "useip": 1
        }
      }
    }
  ]
}
返回数据
参数	说明	类型	可选值	默认值
code	执行状态码	int	0:成功 -1:输入格式错误 -2:获取数量异常 -4:账号登录异常 -5:自有代理创建失败，无法成功创建环境	
msg	返回成功或者失败消息	string		
name	窗口名称接口自你传的	string		
id	新的指纹窗口 id	string		
执行成功

{
  "code": 0,
  "msg": "Success",
  "data": {
    "browse": [
      {
        "id": "1b9f203c9d989a602e52fe1e1eb65025",
        "name": "指纹浏览器"
      }
    ]
  }
}
执行失败

{
  "code": -1,
  "msg": "fail message",
  "data": {
    "browse": null
  }
}




























基础信息
POST /api/v2/userapi/user/update

请求参数
browser 结构体数组，要配置的参数信息（详见：browser）

browser 结构体数组配置：

参数	说明	类型	必填	可选值	默认值
name	浏览器名称	string	否		
browserid	要修改浏览器窗口的ID号	string	是		
proxy	代理信息（详见proxy配置）	object	否		
accounts	账号相关信息（详见accounts配置）	object	否		
accountsv2	账号相关信息（详见accountsv2配置）	[]object	否		
finger	浏览器指纹信息（详见finger配置）	object	否		
proxy 结构体配置：

参数	说明	类型	必填	可选值	默认值
type	代理类型	string	否	self(自有代理)、general(代理API)、socks5、http、https、local(本地)	
uuid	代理ID号,当type是self、general的时候必填，可以从UI界面的自有代理、代理API列表中查看	string	否		
region	国家代号，当type是general的时候必填（详见 region 配置）	string	否		
PublicIP	你的代理公网出口 IP 用于定位使用的 IP，如果为空会无法进行 IP 定位择优配置浏览器指纹信息	string	否		
socks5	代理信息 当 type 设置为 socks5 时设置这个选项（详见 socks5 配置）	object	否		
http	代理信息 当 type 设置为 http 时设置这个选项（详见http 配置）	object	否		
https	代理信息 当 type 设置为 https 时设置这个选项（详见 https 配置）	object	否		
ipChannel	代理检测渠道，默认ipdata	string	否	海外代理：ip2location，国内代理：ipdata	
socks5 结构体配置：

参数	说明	类型	必填	可选值	默认值
Addr	代理地址	string	是		
User	用户名	string	否		
Passwd	密码	string	否		
http 结构体配置：

参数	说明	类型	必填	可选值	默认值
Addr	代理地址	string	是		
User	用户名	string	否		
Passwd	密码	string	否		
https 结构体配置：

参数	说明	类型	必填	可选值	默认值
Addr	代理地址	string	是		
User	用户名	string	否		
Passwd	密码	string	否		
accounts 结构体配置：

参数	说明	类型	必填	可选值	默认值
openurls	浏览器打开时访问的 url 地址	[]string	否		
groupid	分组 ID 创建的新指纹环境分组到指定的位置	string	否		
cookie	要打开环境的 cookie , 账号和 cookie 不能同时填写，此字段值为空时表示不存储cookie数据，如果需要同步cookie, 此字段必填, 请传"[]"	string	否		“[]”
accountsv2 结构体配置：

参数	说明	类型	必填	可选值	默认值
url	账号管理平台地址	string	否		
user	账号管理账号	string	否		
password	账号管理密码	string	否		
finger 结构体配置：

参数	说明	类型	必填	可选值	默认值
kernelversion	kernelversion 浏览器内核大版本号	string	否	107，119，122	107
UaVersion	浏览器大版本号	int	否	目前支持 100-117 不传自动生成	
System	操作系统版本	string	否	目前支持（Windows 7、Windows 8、Windows 8.1、Windows 10、Windows 11、IOS 14、IOS 15、IOS 16、Android 9、Android 10、Android 11、Android 12、Android 13、MacOS 10、MacOS 11、MacOS 12、MacOS 13) 不传会自动生成All Windows, “All Windows”:是在所有支持的Windows操作系统中自动生成; “All IOS”:在所有支持的IOS系统中生成; “All Android”:在所有Android系统中随机 All MacOS:在所有MacOS中随机。	
UserAgent	UserAgent 不写根据系统和浏览器版本自动生成	string	否		
Language	浏览器的语言 不传会根据代理 IP 地址自动生成 详细看支持的语言详细列表(如果是使用动态 IP 自动生成为中文)	[]string	否		
Zone	时区 不传会根据代理 IP 地址自动生成 详细查看时区支持的列表(如果是使用动态 IP 自动生成为北京时间)	string	否		
DPI	平面分辨率	string	否	分隔符x(示例:1920x1080),空自动生成	默认
FontList	字体列表 不传系统自动生成	[]string	否		
WebRTC	Chrome 即时通信组件	int	否	0:禁用,网站会拿不到IP 1:真实,网站会获取真实IP 2:替换,使用代理IP覆盖真实IP 3:转发,IP代理场景使用	0
WebRTCIP	内网ip；WebRTC设置为2时配置	string	否		
Canvas	浏览器canvas指纹开关	int	否	0:倾向一致性 1:关闭 2:倾向随机性	0
WebGl	浏览器webgl元数据指纹开关	int	否	1:隐身 2:真实	1
AudioContext	音频流	int	否	1:隐身 2:真实	1
SpeechVoices	SpeechVoices指纹	int	否	1:每个浏览器使用当前电脑默认的SpeechVoices 2:添加相应的噪音，同一电脑上为每个浏览器生成不同的SpeechVoices	1
MediaDevice	媒体设备开关	int	否	1:关闭（每个浏览器使用当前电脑默认的媒体设备id）2:启用（使用相匹配的值代替您真实的媒体设备ID，噪声）	1
Cpu	CPU 核心数量 不传会自动生成	int	否		
Mem	内存参数 不传会自动生成	float64	否		
DeviceName	计算机名	string	否	15个字符长度以内, 不传会自动生成	
Mac	MAC 地址 不传会自动生成	string	否		
Hardware	硬件加速	int	否	0:关闭 1:开启 2:默认	1
Bluetooth	蓝牙	int	否	0:关闭 1:开启	0
DoNotTrack	“请勿跟踪”浏览器设置	int	否	1:不启用 2:启用 3:默认	1
EnableScanPort	端口扫描防护	int	否	1:开启 2:关闭	1
ScanPort	白名单 0~65535 关闭状态不写 当 EnableScanPort 是 1 时这里为空会自动生成本地端口	[]int	否		
geographic	地理位置 （默认使用 IP 定位 动态代理 IP 不支持次选项为禁止）	object	否		
geographic 结构体配置：

参数	说明	类型	必填	可选值	默认值
enable	地理位置设置	int	否	1:启用 2:询问 3:禁止	1
user	定位方式	int	否	1:使用ip定位 2:自定义	1
longitude	经度(当enable等于2且UseIP等于0时使用)	string	否	-180 - 180	
latitude	纬度(当enable等于2且UseIP等于0时使用)	string	否	-90 - 90	
accuracy	精度（米）(当enable等于2且UseIP等于0时使用)	string	否	10 - 5000	
region 结构体配置：

大洲	国家及代号
亚洲	中国 (CN)、中国台湾（TW）、中国香港（HK）、中国澳门（MO）、日本 (JP)、韩国 (KR)、印度 (IN)、伊朗 (IR)、伊拉克 (IQ)、沙特阿拉伯 (SA)、阿联酋 (AE)、以色列 (IL)、卡塔尔 (QA)、阿曼 (OM)、也门 (YE)、叙利亚 (SY)、黎巴嫩 (LB)、约旦 (JO)、巴勒斯坦 (PS)、土耳其 (TR)、塞浦路斯 (CY)、格鲁吉亚 (GE)、亚美尼亚 (AM)、阿塞拜疆 (AZ)、阿富汗 (AF)、巴基斯坦 (PK)、孟加拉 (BD)、不丹 (BT)、尼泊尔 (NP)、斯里兰卡 (LK)、马尔代夫 (MV)、缅甸 (MM)、泰国 (TH)、老挝 (LA)、柬埔寨 (KH)、越南 (VN)、马来西亚 (MY)、新加坡 (SG)、印度尼西亚 (ID)、文莱 (BN)、菲律宾 (PH)、东帝汶 (TL)
欧洲	英国 (GB)、法国 (FR)、德国 (DE)、意大利 (IT)、西班牙 (ES)、葡萄牙 (PT)、荷兰 (NL)、比利时 (BE)、卢森堡 (LU)、瑞士 (CH)、奥地利 (AT)、匈牙利 (HU)、捷克 (CZ)、斯洛伐克 (SK)、波兰 (PL)、罗马尼亚 (RO)、保加利亚 (BG)、希腊 (GR)、塞尔维亚 (RS)、黑山 (ME)、克罗地亚 (HR)、斯洛文尼亚 (SI)、北马其顿 (MK)、波黑 (BA)、阿尔巴尼亚 (AL)、冰岛 (IS)、丹麦 (DK)、挪威 (NO)、瑞典 (SE)、芬兰 (FI)、爱尔兰 (IE)、摩纳哥 (MC)、列支敦士登 (LI)、圣马力诺 (SM)、梵蒂冈 (VA)、爱沙尼亚 (EE)、拉脱维亚 (LV)、立陶宛 (LT)、摩尔多瓦 (MD)
非洲	埃及 (EG)、利比亚 (LY)、突尼斯 (TN)、阿尔及利亚 (DZ)、摩洛哥 (MA)、毛里塔尼亚 (MR)、塞内加尔 (SN)、冈比亚 (GM)、几内亚 (GN)、几内亚比绍 (GW)、塞拉利昂 (SL)、利比里亚 (LR)、科特迪瓦 (CI)、加纳 (GH)、多哥 (TG)、贝宁 (BJ)、尼日尔 (NE)、尼日利亚 (NG)、喀麦隆 (CM)、赤道几内亚 (GQ)、乍得 (TD)、中非 (CF)、苏丹 (SD)、南苏丹 (SS)、埃塞俄比亚 (ET)、厄立特里亚 (ER)、索马里 (SO)、吉布提 (DJ)、肯尼亚 (KE)、坦桑尼亚 (TZ)、乌干达 (UG)、卢旺达 (RW)、布隆迪 (BI)、塞舌尔 (SC)、毛里求斯 (MU)、马达加斯加 (MG)、科摩罗 (KM)、莫桑比克 (MZ)、马拉维 (MW)、赞比亚 (ZM)、津巴布韦 (ZW)、博茨瓦纳 (BW)、纳米比亚 (NA)、南非 (ZA)、斯威士兰 (SZ)、莱索托 (LS)、圣多美和普林西比 (ST)、佛得角 (CV)
美洲	加拿大 (CA)、美国 (US)、墨西哥 (MX)、危地马拉 (GT)、伯利兹 (BZ)、萨尔瓦多 (SV)、洪都拉斯 (HN)、尼加拉瓜 (NI)、哥斯达黎加 (CR)、巴拿马 (PA)、巴哈马 (BS)、古巴 (CU)、牙买加 (JM)、海地 (HT)、多米尼加 (DO)、圣基茨和尼维斯 (KN)、安提瓜和巴布达 (AG)、多米尼克 (DM)、圣卢西亚 (LC)、圣文森特和格林纳丁斯 (VC)、格林纳达 (GD)、巴巴多斯 (BB)、特立尼达和多巴哥 (TT)、哥伦比亚 (CO)、委内瑞拉 (VE)、圭亚那 (GY)、苏里南 (SR)、法属圭亚那 (GF)、厄瓜多尔 (EC)、秘鲁 (PE)、巴西 (BR)、玻利维亚 (BO)、智利 (CL)、阿根廷 (AR)、乌拉圭 (UY)、巴拉圭 (PY)
大洋洲	澳大利亚 (AU)、新西兰 (NZ)、巴布亚新几内亚 (PG)、所罗门群岛 (SB)、瓦努阿图 (VU)、斐济群岛 (FJ)、基里巴斯 (KI)、密克罗尼西亚联邦 (FM)、马绍尔群岛 (MH)、帕劳 (PW)、图瓦卢 (TV)、萨摩亚 (WS)、汤加 (TO)、法属波利尼西亚 (PF)、新喀里多尼亚 (NC)、瓦利斯和富图纳 (WF)、美属萨摩亚 (AS)、关岛 (GU)、北马里亚纳群岛 (MP)、荷属加勒比区 (BQ)、库拉索 (CW)、阿鲁巴 (AW)、荷属圣马丁 (SX)、法属圣马丁 (MF)、奥兰群岛 (AX)、根西岛 (GG)、泽西岛 (JE)、马恩岛 (IM)、直布罗陀 (GI)、格陵兰 (GL)、法罗群岛 (FO)、安圭拉 (AI)、百慕大 (BM)、开曼群岛 (KY)、特克斯和凯科斯群岛 (TC)
请求示例
http://localhost:50213/api/v2/userapi/user/update
请求体
{
  "browser": [
    {
      "name": "指纹浏览器",
      "browserid":"fdrgdgsfgsertgreaay345754555",
      "proxy": {
        "uuid": "",
        "PublicIP": "",
        "type": "",
		    "region": "",
        "https": {
          "Addr": ""
        }
      },
      "accounts": {
        "openurls": [""],
        "groupid": "",
        "cookie": ""
      },
	    "accountsv2": [
        {
          "url": "",
          "password": "",
          "user": ""
        }
      ],
      "finger": {
        "kernelversion": "107",
        "UAversion": 107,
        "UserAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6237.0 Safari/537.36",
        "Language": [],
        "Zone": "",
        "DPI": "随机",
        "FontList": [],
        "WebRTCIP": "",
        "Canvas": 2,
        "WebGl": 1,
        "WebGLVendor": "Google Inc. (NVIDIA)",
        "AudioContext": 1,
        "SpeechVoices": 1,
        "MediaDevice": 1,
        "Cpu": 8,
        "Mem": 2,
        "DeviceName": "",
        "Mac": "",
        "Hardware": 1,
        "Bluetooth": 1,
        "DoNotTrack": 1,
        "EnableScanPort": 1,
        "ScanPort": [155],
        "geographic": {
          "enable": 1,
          "useip": 1
        }
      }
    }
  ]
}
返回数据
参数	说明	类型	可选值	默认值
code	执行状态码	int	0:成功 -1:输入格式错误 -2:获取数量异常 -4:账号登录异常	
msg	返回成功或者失败消息	string		
datas	返回数据(详见datas 结构体数组)	[]object		
datas 结构体数组：

参数	说明	类型	可选值	默认值
name	窗口名称接口自传的	string		
id	指纹窗口id	string		
code	执行状态码	int	0:成功 -1:没有找到对应浏览器	
执行成功

{
    "code":0,
    "msg":"",
    "datas": [
        {
            "id":"fdrgdgsfgsertgreaay345754555",
            "name":"指纹浏览器",
            "code":0
        }
    ]
}
执行失败

{
    "code": -1,
    "msg": "fail message",
    "data": {}
}































基础信息
POST /api/v2/userapi/user/list

请求参数
参数	说明	类型	必填	可选值	默认值
browserid	浏览器指纹窗口ID列表	[]string	是		
请求示例
http://localhost:50213/api/v2/userapi/user/list
请求体
{
    "browserid":[
        "08638991e03d59ccb9d26571bae80427",
        "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    ]
}
返回数据
参数	说明	类型	可选值	默认值
code	执行状态码	int	0:成功 -1:输入格式错误 -2:获取数量异常 -4:账号登录异常	
msg	返回成功或者失败消息	string		
data	返回数据	object		
apibrowser 结构体数组：

参数	说明	类型	可选值	默认值
Name	指纹浏览器的名称	string		
browserid	要修改浏览器窗口的ID号	string		
proxy	代理信息（详见proxy结构体配置）	object		
accounts	详见accounts结构体配置	object		
proxy结构体配置：

参数	说明	类型	可选值	默认值
type	代理类型	string	official（在我们官网购买的）、self(已经在自有代理列表的)、socks5、http、https、local（本地）	socks5
public_ip	ip地址	string		
uuid	代理设备id	string		
socks5	socks5代理（详见socks5结构体配置）	object		
http	http代理（详见http结构体配置）	object		
https	https代理（详见https结构体配置）	object		
zhima	zhima代理（详见zhima结构体配置）	object		
socks5结构体配置：

参数	说明	类型	可选值	默认值
Addr	代理地址	string		
User	用户名	string		
Passwd	密码	string		
http 结构体配置：

参数	说明	类型	可选值	默认值
Addr	代理地址	string		
User	用户名	string		
Passwd	密码	string		
https 结构体配置：

参数	说明	类型	可选值	默认值
Addr	代理地址	string		
User	用户名	string		
Passwd	密码	string		
zhima结构体配置：

参数	说明	类型	可选值	默认值
Url	提取地址	string		
Interval	提取间隔	number		0
accounts结构体配置：

参数	说明	类型	可选值	默认值
openurls	浏览器打开时访问的其他url地址列表	[]string		
groupid	分组ID	string		
user	平台账号	string		
passwd	平台密码	string		
cookie	账号或者cookie不能同时填写	string		
执行成功

{
    "code":0,
    "msg":"Success",
    "data":{
        "apibrowser":[
            {
                "Name":"测试窗口-1",
                "browserid":"08638991e03d59ccb9d26571bae80427",
                "proxy":{
                    "type":"socks5",
                    "uuid": "9261f478874c45ac989acb3ae317cb76",
                    "public_ip": "",
                    "socks5":{
                        "Addr":"89.2.3.1",
                        "User":"admin",
                        "Passwd":"123456"
                    },
                    "http": {
                        "Addr": "",
                        "User": "",
                        "Passwd": ""
                    },
                    "https": {
                        "Addr": "",
                        "User": "",
                        "Passwd": ""
                    },
                    "zhima": {
                        "Url": "",
                        "Interval": 0
                    }
                },
                "accounts":{
                    "openurls":["www.baidu.com"],
                    "groupid":"23984yoefjsoiroi4wqdfa",
                    "user":"admin",
                    "passwd":"adminrest",
                    "cookie":"erjagprtgjuwhgr;asgjresoi"
                }
            },
            {
                "Name":"测试窗口-2",
                "browserid":"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                "proxy":{
                    "type":"socks5",
                    "uuid": "9261f478874c45ac989acb3ae317cb76",
                    "public_ip": "",
                    "socks5":{
                        "Addr":"89.2.3.1",
                        "User":"admin",
                        "Passwd":"123456"
                    },
                    "http": {
                        "Addr": "",
                        "User": "",
                        "Passwd": ""
                    },
                    "https": {
                        "Addr": "",
                        "User": "",
                        "Passwd": ""
                    },
                    "zhima": {
                        "Url": "",
                        "Interval": 0
                    }
                },
                "accounts":{
                    "openurls":["www.baidu.com"],
                    "groupid":"23984yoefjsoiroi4wqdfa",
                    "user":"admin",
                    "passwd":"adminrest",
                    "cookie":"erjagprtgjuwhgr;asgjresoi"
                }
            }
        ]
    }
}
执行失败

{
    "code": -1,
    "msg": "fail message",
    "data": {
        "apibrowser": null
    }
}















基础信息
POST /api/v2/userapi/user/delete

请求参数
参数	说明	类型	必填	可选值	默认值
browserid	要删除的浏览器指纹窗口ID	[]string	是		
请求示例
http://localhost:50213/api/v2/userapi/user/delete
请求体
{
    "browserid": [
			"d03ca5de08ec8e02c4b78558ee84d7fc",
			"08638991e03d59ccb9d26571bae80427"
		]
}
返回数据
参数	说明	类型	可选值	默认值
code	执行状态码	int	0:成功 -1:输入格式错误 -2:获取数量异常 -4:账号登录异常	
msg	返回成功或者失败消息	string		
执行成功

{
	"code":0,
	"msg":"Success",
}
执行失败

{
    "code": -1,
    "msg": "failed"
}























基础信息
POST /api/v2/userapi/user/regroup

请求参数
参数	说明	类型	必填	可选值	默认值
browserid	要更换的浏览器指纹窗口ID	[]string	是		
groupid	更换的分组ID	string	是		
请求示例
http://localhost:50213/api/v2/userapi/user/regroup
请求体
{
    "browserid": [
        "d03ca5de08ec8e02c4b78558ee84d7fc",
        "08638991e03d59ccb9d26571bae80427"
	],
    "groupid": "xxx"
}
返回数据
参数	说明	类型	可选值	默认值
code	执行状态码	int	0:成功 -1:输入格式错误 -2:获取数量异常 -4:账号登录异常	
msg	返回成功或者失败消息	string		
执行成功

{
	"code":0,
	"msg":"Success",
}
执行失败

{
	"code": -1,
	"msg": "fail message"
}


































基础信息
POST /api/v2/userapi/selfproxy/create

请求参数
proxy 结构体数组，要配置的参数信息（详见：proxy）

proxy 结构体配置：

参数	说明	类型	必填	可选值	默认值
name	代理名称	string	是		
proxytype	代理类型	int	是	1:有用户名密码sock5协议 3:无用户名密码socks5协议 4:http协议 5:https协议 6:http有用户名密码协议 7：https有用户名密码协议	
proxyaddr	代理地址	string	是		
proxyu	登录账号	string	否		
proxyp	登录密码	string	否		
notes	备注	string	否		
请求示例
http://localhost:50213/api/v2/userapi/selfproxy/create
请求体
{
    "proxy": {
        "name": "代理1",
        "proxytype": 1,
        "proxyaddr": "1.1.1.1:2333",
        "proxyp": "7777777",
        "proxyu": "8888888",
        "notes": "代理"
    }
}
返回数据
参数	说明	类型	可选值	默认值
code	执行状态码	int	0:成功 -1:输入格式错误 -2:获取数量异常 -4:账号登录异常	
msg	返回成功或者失败消息	string		
执行成功

{
    "code": 0,
    "msg": "Success"
}
执行失败

{
    "code": -1,
    "msg": "fail message"
}




































基础信息
POST /api/v2/userapi/selfproxy/delete

请求参数
参数	说明	类型	必填	可选值	默认值
deviceid	代理id	[]string	是		
请求示例
http://localhost:50213/api/v2/userapi/selfproxy/delete
请求体
{
    "deviceid": [
        "9a8cc12c5e1663e3efcb05e6608869dc",
        "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    ]
}
返回数据
参数	说明	类型	可选值	默认值
code	执行状态码	int	0:成功 -1:输入格式错误 -2:获取数量异常 -4:账号登录异常	
msg	返回成功或者失败消息	string		
执行成功

{
    "code": 0,
    "msg": "Success"
}
执行失败

{
    "code": -1,
    "msg": "fail message"
}























基础信息
POST /api/v2/userapi/selfproxy/list

请求参数
参数	说明	类型	必填	可选值	默认值
page	页码	int	是		
pageSize	每页大小	int	是		
name	代理名称	string	否		
请求示例
http://localhost:50213/api/v2/userapi/selfproxy/list
请求体
{
    "page": 1,
    "pageSize": 10,
    "name": ""
}
返回数据
参数	说明	类型	可选值	默认值
code	执行状态码	int	0:成功 -1:输入格式错误 -2:获取数量异常 -4:账号登录异常	
msg	返回成功或者失败消息	string		
deviceid	代理id	string		
companyid	团队id	string		
name	代理名称	string		
proxytype	代理类型	int	1:有用户名密码sock5协议 3:无用户名密码socks5协议 4:http协议 5:https协议 6:http有用户名密码协议 7:https有用户名密码协议	
proxyaddr	代理地址	string		
user	登录账号	string		
passwd	登录密码	string		
notes	备注	string		
createdat	创建时间	string		
执行成功

{
    "code": 0,
    "msg": "Success",
    "data": {
        "list": [
            {
                "deviceid": "cc12c5e1663e3efcb05e66088XX",
                "companyid": "e9b455594c05b52210226XX",
                "name": "代理修改",
                "proxyaddr": "1.1.1.1:2333",
                "proxytype": 1,
                "user": "99999",
                "passwd": "55555",
                "notes": "修改1",
                "createdat": "2024-04-12 15:58:06"
            }
        ],
        "total": 1,
        "pageSize": 10,
        "currentPage": 1
    }
}
执行失败

{
    "code": -1,
    "msg": "fail message"
}


















基础信息
POST /api/v2/userapi/selfproxy/update

请求参数
proxy 结构体数组，要配置的参数信息（详见：proxy）

proxy 结构体配置：

参数	说明	类型	必填	可选值	默认值
deviceid	代理id	string	是		
name	代理名称 如果传空表示不修改	string	否		
proxytype	代理类型	int	否	0:表示不修改 1:有用户名密码sock5协议 3:无用户名密码socks5协议 4:http协议 5:https协议 6:http有用户名密码协议 7:https有用户名密码协议	
proxyaddr	代理地址 如果传空表示不修改	string	否		
proxyu	登录账号 如果传空表示不修改	string	否		
proxyp	登录密码 如果传空表示不修改	string	否		
notes	备注 如果传空表示不修改	string	否		
请求示例
http://localhost:50213/api/v2/userapi/selfproxy/update
请求体
{
    "proxy": {
        "name": "代理修改",
        "proxytype": 0,
        "proxyaddr": "",
        "deviceid": "XXXX5e1663e3efcb05e66XXXXc",
        "notes": "修改",
        "proxyu": "99999",
        "proxyp": "55555"
    }
}
返回数据
参数	说明	类型	可选值	默认值
code	执行状态码	int	0:成功 -1:输入格式错误 -2:获取数量异常 -4:账号登录异常	
msg	返回成功或者失败消息	string		
执行成功

{
    "code": 0,
    "msg": "Success"
}
执行失败

{
    "code": -1,
    "msg": "fail message"
}



































基础信息：POST /api/v2/userapi/plugin/groupPluginList

请求参数

参数	说明	类型	必填	可选值	默认值
page	页码	int	是		
pageSize	每页大小	int	是		
sort	排序	string	否	1：正序，非1：倒叙	倒叙
请求示例

http://localhost:50213/api/v2/userapi/plugin/groupPluginList?pageIndex=1&pageSize=10086
返回数据

参数	说明	类型	可选值	默认值
code	执行状态码	int		
msg	返回成功或者失败消息	string		
globalPlugin	全局插件	object		
userPlugin	个人插件	object		
globalPlugin结构体数组：

参数	说明	类型	可选值	默认值
pluginGroup	插件分组信息	object		
companies	插件信息	object		
pluginGroup结构体配置：

参数	说明	类型	可选值	默认值
CreatedAt	创建时间	string		
UpdatedAt	更新时间	string		
groupId	分组ID	string		
companyId	团队ID	string		
userId	用户ID	string		
groupName	分组名称	string		
isGlobal	是否全局模式	int	1 是全局 2 非全局	
groupType	分组类型	int	1：团队分组 2：个人分组	
remark	备注	string		
companies结构体配置：

参数	说明	类型	可选值	默认值
accountIds	授权账号	[]string		
pluginId	插件id	string		
uids	uids	[]string		
companyId	企业id	string		
uuid	uuid	string		
userName	用户登录名	string		
nickName	用户昵称	string		
version	版本	string		
pluginCompanyId	标识	string		
permissions	权限集合	string		
name	名称	string		
icon	图标	string		
card	卡片展示图	string		
brief	简介	string		
author	提供方	string		
catIds	分类id集合	string		
CreatedAt	创建时间	string		
lookNum	浏览量	int		
installNum	安装量	int		
sort	排序	int		
installStatus	安装状态	int		
kernel	插件内核：	int	1 谷歌 2 火狐 3 通用	
firefoxVersion	火狐插件版本	string		
firefoxPermissions	火狐权限集合	string		
firefoxUuid	火狐插件扩展ID	string		
userId	所有者	string		
uplinkId	上传人	string		
isGlobal	是否全局模式	int	1 是全局 2 非全局	
isTeam	是否团队可见	int	1 是可见 2 非可见	
groupId	分组ID	[]string		
groupName	分组名称	[]string		
pluginType	插件类型	int	1：官方插件 2：客户插件	
detail	介绍	string		
teamStatus	团队状态	int		
执行成功

{
    "code": 200,
    "data": {
        "globalPlugin": {
            "list": [
                {
                    "pluginGroup": {
                        "ID": 266,
                        "CreatedAt": "2025-03-31T10:46:23+08:00",
                        "UpdatedAt": "2025-03-31T10:46:23+08:00",
                        "groupId": "5b673cb47a1e4a9bbe755794b57830a8",
                        "companyId": "6d6327121940451d906a0abf283d0e1a",
                        "userId": "bfe030a73b4c4f4da3e30d9eea3a6f3e",
                        "groupName": "22222222",
                        "isGlobal": 2,
                        "groupType": 1,
                        "remark": ""
                    },
                    "companies": []
                }
            ],
            "count": 1,
            "pageIndex": 1,
            "pageSize": 10086
        },
        "userPlugin": {
            "list": [
                {
                    "pluginGroup": {
                        "ID": 265,
                        "CreatedAt": "2025-03-31T10:46:17+08:00",
                        "UpdatedAt": "2025-03-31T10:46:17+08:00",
                        "groupId": "c5ea2e88dfdf41deaeccb88488ae9357",
                        "companyId": "6d6327121940451d906a0abf283d0e1a",
                        "userId": "bfe030a73b4c4f4da3e30d9eea3a6f3e",
                        "groupName": "1111111111",
                        "isGlobal": 2,
                        "groupType": 2,
                        "remark": ""
                    },
                    "companies": [
                        {
                            "accountIds": null,
                            "pluginId": "016331ba5faf47db9f20f3f0ffe92400",
                            "uids": null,
                            "companyId": "6d6327121940451d906a0abf283d0e1a",
                            "uuid": "ckbdbmaijdhkbhkmkhkefjgekpacfbei",
                            "userName": "",
                            "nickName": "",
                            "version": "3.5.0",
                            "pluginCompanyId": "263ee25c838d47a8a9c435de4dc12ca5",
                            "permissions": null,
                            "name": "wxt-插件",
                            "icon": "",
                            "card": "",
                            "brief": "",
                            "author": "用户自主上传",
                            "catIds": "",
                            "CreatedAt": "2025-03-31T10:45:42+08:00",
                            "lookNum": 0,
                            "installNum": 0,
                            "sort": 99,
                            "installStatus": 1,
                            "kernel": 1,
                            "firefoxVersion": "",
                            "firefoxPermissions": null,
                            "firefoxUuid": "",
                            "userId": "bfe030a73b4c4f4da3e30d9eea3a6f3e",
                            "uplinkId": "bfe030a73b4c4f4da3e30d9eea3a6f3e",
                            "isGlobal": 2,
                            "isTeam": 2,
                            "groupId": [
                                "c5ea2e88dfdf41deaeccb88488ae9357"
                            ],
                            "groupName": [
                                "1111111111"
                            ],
                            "pluginType": 2,
                            "detail": "",
                            "teamStatus": 0
                        }
                    ]
                }
            ],
            "count": 1,
            "pageIndex": 1,
            "pageSize": 10086
        }
    },
    "msg": "ok",
    "requestId": ""
}



































基础信息

POST /api/v2/userapi/plugin/bindGroupPlugin

请求参数

参数	说明	类型	必填	可选值	默认值
groupId	分组id	[]string	是		
accountIds	环境id	[]string	是		
请求示例

http://localhost:50213/api/v2/userapi/plugin/bindGroupPlugin
请求体

{
    "groupId":[
        ""
    ],
    "accountIds":[
        ""
    ]  
}
返回数据

参数	说明	类型	可选值	默认值
code	执行状态码	int		
data				
msg	返回成功或者失败消息	string		
requestId				
执行成功

{
    "code": 200,
    "data": {},
    "msg": "ok",
    "requestId":""
}




























基础信息
POST /api/v2/userapi/cookie/upsert

请求参数
参数	说明	类型	必填	可选值	默认值
shopid	环境id	string	是		
cookies	标准cookie格式	cookies	是		
cookies 结构体配置：

参数	说明	类型	必填	可选值	默认值
name	名称	string	是		
value	值	string	是		
domain	有效域	string	是		
expirationDate	有效期	number	是		
hostOnly	域名完全匹配	boolean	是		
httpOnly	避免cookie被Javascript访问	boolean	是		
path	路径	string	是		
sameSite	限制第三方 Cookie	string	是	Strict:完全禁止 Lax:get请求除外 None:允许所有,必须同时设置Secure属性	
secure	安全属性	boolean	是		
session		boolean	是		
storeId		string	是		
port	端口	int	是		
请求示例
http://localhost:50213/api/v2/userapi/cookie/upsert
请求体
{
    "shopid": "900bc9bc9438f96654006add8e7d344b",
    "cookies": [
        {
            "domain": ".XXX.cn",
            "hostOnly": false,
            "httpOnly": false,
            "name": "Hm_lpvt_a73626d29XXX",
            "path": "/",
            "sameSite": "",
            "secure": false,
            "session": false,
            "storeId": "",
            "value": "1711004434",
            "port": 443
        }
    ]
}
返回数据
参数	说明	类型	可选值	默认值
code	执行状态码	int	0:成功 -1:输入格式错误 -2:获取数量异常 -4:账号登录异常	
msg	返回成功或者失败消息	string		
执行成功

{
    "code": 0,
    "msg": "Success"
}
执行失败

{
    "code": -1,
    "msg": "fail message"
}



































基础信息
POST /api/v2/userapi/cookie/clear

请求参数
参数	说明	类型	必填	可选值	默认值
shopid	环境id	string	是		
请求示例
http://localhost:50213/api/v2/userapi/cookie/clear
请求体
{
  "shopid": "900bc9bc9438f96654006add8e7d344b"
}
返回数据
参数	说明	类型	可选值	默认值
code	执行状态码	int	0:成功 -1:清理出错	
msg	返回成功或者失败消息	string		
执行成功

{
  "code": 0,
  "msg": "Success"
}
执行失败

{
  "code": -1,
  "msg": "fail message"
}





































