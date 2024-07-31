# 分析cvs文件
import pandas as pd


def get_python_coder(file):
    # 读取CVS文件
    df = pd.read_csv(file)

    # 将编程语言转换为小写 方便比较
    df['language'] = df['language'].str.lower()

    # 筛选出来使用python编程语言的数据
    python_high_users = df[(df['language'] == 'python') & (df['level'] >= 4)]

    print(python_high_users)


# 传入cvs文件的路径
file_path = 'files/language.csv'

# 调用函数
get_python_coder(file_path)
