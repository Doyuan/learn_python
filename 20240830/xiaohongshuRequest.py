import requests

url = ('https://sns-webpic-qc.xhscdn.com/202408301748/a04c9789d4c8741f8e9d67a511399bcd'
       '/1040g008316pl0dh0k6005n3ai96k7e630ngt2fo!nd_dft_wlteh_webp_3')

image_response = requests.get(
    url=url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT'}, verify=False
)

with open('image.jpg', 'wb') as f:
    f.write(image_response.content)
