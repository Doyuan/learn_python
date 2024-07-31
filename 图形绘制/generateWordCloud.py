# 绘制词云
import jieba
import numpy
from PIL import Image
from matplotlib import pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator


def chinese_jieba(word):
    wordlist_jieba = jieba.cut(word)
    text_jieba = ' '.join(wordlist_jieba)
    return text_jieba


# 读取文本内容
with open('files/0731.text', 'r', encoding='utf-8') as fp:
    text = fp.read()
    # 对文本进行分词
    text = chinese_jieba(text)
    # 读入遮罩图层
    mask_pic = numpy.array(Image.open('files/11.png'))
    # 定义词云对象
    wordcloud = WordCloud(font_path='files/1.otf', background_color='white', max_font_size=120, mask=mask_pic,
                          max_words=120).generate(text)
    # 用图片和颜色填充词云的颜色
    image_colors = ImageColorGenerator(mask_pic)
    wordcloud.recolor(color_func=image_colors)

    # 生成图片
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()