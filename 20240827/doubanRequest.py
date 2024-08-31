import requests
import re

top = 0

for page in range(1, 11):
    resp = requests.get(
        url=f'https://movie.douban.com/top250?start={(page - 1) * 25}',
        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 ('
                               'KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'}, verify=False
    )
    # title匹配正则规则
    title_pattern = re.compile(r'<span class="title">([^&]*?)</span>')
    titles = title_pattern.findall(resp.text)

    # rating_num 属性正则规则
    rating_pattern = re.compile(r'<span class="rating_num".*?>(.*?)</span>')
    ranks = rating_pattern.findall(resp.text)

    for title, rank in zip(titles, ranks):
        top = top + 1
        with open('豆瓣电影top250.txt', 'r+', encoding='utf-8') as file:
            content = file.read()
            content += f'第{top}名:《{title}》--{rank}\n'
            file.seek(0)
            file.write(content)
            file.truncate()

