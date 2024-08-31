import requests

try:
    resp = requests.get('https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png', verify=True)
    resp.raise_for_status()  # 检查请求是否成功
except requests.exceptions.RequestException as e:
    print(f"网络请求失败: {e}")
else:
    try:
        with open('baidu.png', 'wb') as file:
            file.write(resp.content)
    except IOError as e:
        print(f"文件写入失败: {e}")

