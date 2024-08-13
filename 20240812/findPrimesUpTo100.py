# 寻找100以内的素数
import math


def primesUpTo(n):
    for num in range(2, n):
        is_prime = True
        for factor in range(2, int(math.sqrt(num)) + 1):
            if num % factor == 0:
                is_prime = False
                break;
        if is_prime:
            print(num, end=' ')


primesUpTo(100)
