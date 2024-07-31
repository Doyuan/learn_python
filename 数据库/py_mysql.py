# 使用mysql案例
import random
import string
import pymysql


def generate_random_string(random_length):
    coupon = random.sample(string.digits + string.ascii_letters, random_length)
    return ''.join(coupon)


coupons = list()

for i in range(10):
    single_result = generate_random_string(20)
    coupons.append(single_result)

conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='root',
    db='py_test',
    charset='utf8mb4'
)

cursor = conn.cursor()

nos = list(range(1, len(coupons) + 1))

for i, j in zip(nos, coupons):
    cursor.executemany("INSERT INTO couponList (id, code) VALUES (%s, %s)", [(i, j)])
    conn.commit()
