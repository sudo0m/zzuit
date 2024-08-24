import requests

url = "https://xgxt.zzuit.edu.cn/GYWebApi/api/StuActive/SaveChooseBed"

headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9",
    "authorization": "", # 填写authorization
    "content-type": "application/x-www-form-urlencoded",
    "priority": "u=1, i",
    "sec-ch-ua": "\"Not)A;Brand\";v=\"99\", \"Google Chrome\";v=\"127\", \"Chromium\";v=\"127\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "cookie": "", # 填写cookie
    "Referer": "https://xgxt.zzuit.edu.cn/GYWeb/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
}

data = {
    'StudentId':'', # 学号
    'BedId':'' # 床位id    
}

# proxies = {
#     'http': 'http://127.0.0.1:10809',
#     'https': 'http://127.0.0.1:10809',
# }
# 如需代理 proxies=proxies 使用国外地址能够更快访问网站
def get_website():
    response = requests.post(url, headers=headers, data=data, proxies=proxies)
    print(response.status_code)  # 打印状态码
    print(response.json())  # 解析JSON响应体
    return response

flag = True

while flag:
    time.seelp(3)
    response = get_website()
    # if response.status_code == 200:
    #     print(response.json())
    #     flag = False
    # else:
    #     print(response.status_code)