# 소수 : 1과 자기 자신만을 약수로 갖는 수

import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

n = int(input())
prime_and_3k_1 = []

for i in range(2, n+1):
    if is_prime(i) and (i % 3 == 2):
        prime_and_3k_1.append(i)
    
print(prime_and_3k_1)