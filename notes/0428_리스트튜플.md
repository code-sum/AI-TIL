# ✅ [4/28] 리스트, 튜플, 문자열, 사전, 집합



어제 "리스트와 튜플" 슬라이드에서 실습(2) 못 풀었던 것 오늘 풀이 (6:22~6:32)



#### 미션3. 튜플의 평균 구하기

> 숫자가 들어있는 튜플을 지시사항에 맞게 계산하고 그 결과를 출력하세요.
>
> 주어진 `numbers` 튜플을 풀어서 세 원소의 평균을 구해서 출력하세요.
>
> (소수점 첫자리까지 출력해주세요.)

```python
numbers = (3,6,3)

avg = sum(numbers) / len(numbers)

print("{:.1f}".format(avg))
```



#### 미션5. 소수 중 3k-1 꼴인 수

> n을 입력받고, n 이하의 소수 중 3k-1(k는 1이상의 자연수) 꼴인 수를 포함하는 **리스트**를 만들고 출력하세요. ( **리스트는 작은 수 부터 오름차순으로 정렬되어 있어야 합니다.** )
>
> 예를 들어, n = 10 인 경우 2,5가 리스트에 차례로 들어 있어야 합니다.

```python
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
```

