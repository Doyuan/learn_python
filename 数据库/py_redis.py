# redis 案列
import random
import string

import redis


def generate_random_string(length):
    coupon = random.sample(string.digits + string.ascii_letters, length)
    return ''.join(coupon)


coupons = list()
for i in range(10):
    single_result = generate_random_string(20)
    coupons.append(single_result)

# 打开redis数据库连接
pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)

nos = list(range(1, len(coupons) + 1))

for i, j in zip(nos, coupons):
    r.set(str(i), str(j))

for i in nos:
    print(r.get(str(i)))
