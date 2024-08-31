import os
import re

from lxml import etree

import requests

url = 'https://www.tooopen.com/art/beauty-photo.html?page=2'

chinese_punctuation_pattern = r'[<>:"/\\|?*]'

resp = requests.get(
    url=url,
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/58.0.3029.110 Safari/537.36'
    }, verify=False
)

tree = etree.HTML(resp.text)
titles = tree.xpath('//div[@class="w-img"]/img/@alt')
urls = tree.xpath('//div[@class="w-img"]/a/@href')

save_path = 'girls/'

for title, url in zip(titles, urls):
    title = re.sub(chinese_punctuation_pattern, '', title)
    pic_path = save_path + title
    os.makedirs(pic_path, exist_ok=True)

    response = requests.get(url=url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                                                            'AppleWebKit/537.36 (KHTML, like Gecko) '
                                                            'Chrome/58.0.3029.110 Safari/537.36'}, verify=False)
    content = etree.HTML(response.text)
    images = content.xpath("//div[@class='w-det-con']/p/img/@src")
    image_titles = content.xpath("//div[@class='w-det-con']/p/img/@alt")
    for image_title, image in zip(image_titles, images):
        image_title = re.sub(chinese_punctuation_pattern, '', image_title)
        img_response = requests.get(url=image, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                                                                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                                                                      'Chrome/58.0.3029.110 Safari/537.36'}, verify=False)
        with open(os.path.join(pic_path, image_title + '.jpg'), 'wb') as f:
            f.write(img_response.content)
