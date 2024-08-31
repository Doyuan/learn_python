import requests

try:
    resp = requests.get('https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png', verify=True)
    resp.raise_for_status()  # ��������Ƿ�ɹ�
except requests.exceptions.RequestException as e:
    print(f"��������ʧ��: {e}")
else:
    try:
        with open('baidu.png', 'wb') as file:
            file.write(resp.content)
    except IOError as e:
        print(f"�ļ�д��ʧ��: {e}")

