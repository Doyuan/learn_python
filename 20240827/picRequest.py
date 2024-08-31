import os

from lxml import etree
from lxml import html
import requests

resp = requests.get(
    url='https://www.qqtn.com/article/article_320939_1.html',
    headers={'User-Agent': 'Mozilla/5'}, verify=False
)
tree = etree.HTML(resp.text)
pics = tree.xpath('//*[@id="zoom"]/p/img/@src')

save_path = 'images'
os.makedirs(save_path, exist_ok=True)

for i, pic in enumerate(pics):
    try:
        response = requests.get(
            url=pic,
            headers={'User-Agent': 'Mozilla/5'}, verify=False
        )
        response.raise_for_status()

        image_name = os.path.basename(pic)
        file_path = os.path.join(save_path, image_name)

        with open(file_path, 'wb') as file:
            file.write(response.content)
            print(f'第{image_name}张图片下载成功')
    except requests.exceptions.RequestException as e:
        print(f'第{i}张图片下载失败：{e}')
