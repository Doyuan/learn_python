import os

import requests
from lxml import etree

url = "https://www.tooopen.com/art/view/63a1ed861a87400960f47bf3.html"

response = requests.get(
    url=url, headers={"User-Agent": "Mozilla/5"}, verify=False
)

save_path = 'images'
os.makedirs(save_path, exist_ok=True)

tree = etree.HTML(response.text)

images = tree.xpath("//div[@class='w-det-con']/p/img/@src")
titles = tree.xpath("//div[@class='w-det-con']/p/img/@alt")

for image, title in zip(images, titles):
    img_response = requests.get(image, headers={"User-Agent": "Mozilla/5"}, verify=False)
    img_save_path = os.path.join(save_path, title + ".jpg")
    with open(img_save_path, "wb") as f:
        f.write(img_response.content)
