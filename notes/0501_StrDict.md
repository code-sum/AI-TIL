# ✅ [5/1] 문자열, 집합, 사전, 모듈, 그래픽 객체





#### 실습1. 점수표

> 학생들의 수학, 영어 점수를 입력받아 이를 모아둔 점수표를 출력하세요.

```python
# 학생 수 입력
n = int(input('Number of Students: '))

score = {}

for i in range(n):
    name = input('Name: ')
    math = int(input('Math: '))
    english = int(input('English: '))

    # score에 넣어봅시다.
    score[name]=[math, english]

# 내림차순 정렬
# sorted 함수 사용 예시
# result = sorted(list.items(), reverse = False)
# reverse가 False이면 오름차순, True이면 내림차순으로 사용할 수 있습니다.

score=sorted(score.items(), reverse=True)

print('==========ScoreList==========')
print(score)
```



#### 실습2. 중복없는 리스트 합치기

> 두 list를 입력받고, set을 사용하여 중복없는 list를 만들어 출력하세요.
>
> 첫 줄에는 첫 list의 input 수를 입력받습니다.
> 이후 그 수만큼 input을 입력받습니다.
> 다음 줄에서는 두 번째 list의 input 수를 입력받습니다.
> 이후 그 수만큼 input을 입력받습니다.
>
> 두 리스트를 중복된 값은 한 번만 들어가도록 만든 후, 오름차순 정렬하여 출력하세요.

```python
n1 = int(input())
list1 = []

for i in range(n1):
    list1.append(int(input()))

n2 = int(input())
list2 = []

for i in range(n2):
    list2.append(int(input()))
    
# 두 list를 중복없는 리스트 result_list로 합친 후, 오름차순 정렬하여 출력하세요.
result_list = list(set(list1 + list2))
result_list.sort()

print(result_list)
```

