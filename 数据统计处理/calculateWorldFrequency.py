# 统计出现的单词数量
import re
from collections import Counter

# 打开文件
f = open('files/abc.text')

# 匹配大小写字母的正则表达式
letters = re.compile('[a-zA-Z]+')

# 初始化存储单词的列表
words = list()

# 逐行读取文件的内容
line = f.readline()
while line:
    # 使用正则表达式找到每行中的单词
    found_world = letters.findall(line)

    # 将找到的单词添加到存储单词的列表中
    words.extend(found_world)

    # 读取下一行
    line = f.readline()

# 关闭文件
f.close()

# 使用Counter 对单词进行计数
word_count = Counter(words)

# 输出每个单词出现次数
print(word_count)