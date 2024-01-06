# ✅ [5/7] ClassA_Practice

> 1. Python OOP & Class
> 2. `/May7_Practice`
>
> 💡[OOP vs. functional programming](https://stackoverflow.com/questions/2984460/do-you-use-python-mostly-for-its-functional-or-object-oriented-features)
>
> 💡[Real Python: OOP in Python 3](https://realpython.com/python3-object-oriented-programming/)
>
> 💡[Real Python: Functional Programming in Python](https://realpython.com/python-functional-programming/)





---



## 1. Python OOP & Class

> 5/3 수요일 <객체지향 프로그래밍> 슬라이드 13page super (오버라이딩) 수업하다가 끝났던 부분 추가 설명 및 실습1 ~ 실습3  풀이

1. super

`Animal()` 클래스를 상속한 `Dog()` 클래스

`super().__init__()` --> 어떤 역할인지 [참조](https://jimmy-ai.tistory.com/79)



2. 추상 클래스



3. Quiz 1_클래스와 인스턴스에 관련된 설명으로 옳은 것을 모두 고르시오.
   1번 O, 2번 O, 3번 X, 4번 O -> 4번은 클래스를 사용하는 목적이기도 함
   그런데 만약에 3번에 모델명이 다르게 들어가면, 인스턴스만 다시 만들어야



4. Quiz 2_실습 자료에서 다시 볼 예정



5. Quiz3_상속, 오버라이딩, super, 추상 클래스에 관한 설명으로 옳지 않은 것을 모두 고르세요.
   1번 X, 2번 X(굳이 부르고자 하면, `super().__init__()`), 3번 O, 4번 X, 5번 O



5/3 자료중 미션4. 정답 1, 5번!



[실습1] Dog 클래스

```python
class Dog:
#Dog class 구현 ...
    def __init__(self, name_input, age_input, gender_input, owner_input):
        self.name=name_input
        self.age=age_input
        self.gender=gender_input
        self.owner=owner_input
        
    def get_older(self):
        self.age+=1
        
    def set_owner(self, owner_input):
        self.owner=owner_input

    def print_dog(self):
        print(self.name)
        print(self.age)
        print(self.gender)
        print(self.owner)

dog_instance = Dog('Puggy', 5, 'M', 'Tom')
dog_instance.print_dog()
dog_instance.get_older()
dog_instance.get_older()
dog_instance.print_dog()

dog_instance.set_owner('James')
dog_instance.print_dog()
```



[실습2] Person 클래스

> Tom과 Jerry는 아래와 같은 정보를 가지고 있다.
>
> name: Tom / Jerry
> age: 23 / 25
> gender: male / female
> sports: tennis / swim
> food: steak / noodle
> eat: “eat steak” / “eat noodle”을 출력하는 메서드
> old: 나이를 한 살씩 더하는 메서드
>
> 위의 조건을 모두 만족하는 person class를 만들고, Tom과 Jerry 인스턴스를 만드세요. (대소문자 주의)

```python
class Person:
    # 기본적인 상태
    def __init__(self, name, age, gender, sports, food):
        self.name=name
        self.age=age
        self.gender=gender
        self.sports=sports
        self.food=food
    def eat(self):
        print("eat "+self.food)
    def old(self):
        self.age += 1

Tom=Person('Tom', 23, 'male', 'tennis', 'steak')
Jerry=Person('Jerry', 25, 'female', 'swim', 'noodle')
```



[실습3] Account 클래스

> A은행의 계좌는 B옵션의 계좌와, C옵션의 계좌로 나뉜다.
>
> option: B / C
> interest_rate: 1 / 3
> withdraw: 잔고를 출금하는 메서드 (출금액을 매개 변수로 받으며 출금액 잔액보다 클 경우 ‘ERROR: insufficient balance’ 출력)
> deposit: 돈을 넣는 메서드
> interest: 이자가 더해지는 메서드
>
> 위의 조건을 모두 만족하는 account class에 상속되는 B, C class를 만들고, account1은 B은 인스턴스, account2와 account3는 C의 인스턴스가 되도록 구성하세요.

```python
class account:
    def withdraw(self, output_money):
        if(self.balance<output_money):
            print('ERROR: insufficient balance')
        else:
            self.balance-=output_money
    def deposit(self, input_money):
        self.balance += input_money
    # 만약 interest 매서드를 나중에라도 개발하도록 강제하려면?
    # 이 자리에 @abstractmethod 기입
    # @abstractmethod 안쓸거고 자식 클래스에서 interest 를 정의할거면
    # pass 부분 삭제해도 됨
    def interest(self):
        pass
class B(account):
    def __init__(self):
        self.interest_rate = 1  # 초기화
        self.balance=0  # 초기화
    def interest(self):
        self.balance *= 1+self.interest_rate/100.0
class C(account):
    def __init__(self):
        self.interest_rate = 3  # 초기화
        self.balance=0  # 초기화
    def interest(self):
        self.balance *= 1+self.interest_rate/100.0
account1 = B()
account2 = C()
account3 = C()
```



---



## 2. `/May7_Practice`

> 오늘 준비한 실습자료 8개 (`/May7_Practice/P1 ~ P8`)
>
> 엘리스 창에서 진행해도 되고, IDE 에서 진행해도 됨



#### 실습1. 다수 파일을 하나로 합치기

> 여러 파일을 하나의 파일로 병합하는 경우

```python
# 답안

import elice_utils

from time import sleep

def merge(input_filenames, output_filename):
    with open("./{}".format(output_filename), "w") as f:
        for fn in input_filenames:
            with open(fn, "r") as g:
                lines = g.readlines()
                f.writelines(lines)
    return

merge(['kaist1.txt', 'kaist2.txt', 'kaist3.txt'], 'output.txt')

sleep(0.5) # Wait 0.5 seconds before creating a download link.
elice_utils.send_file('output.txt')
```

```python
# 위 답안을 class 를 사용해서 다시 작성한다면?
# Merger() 라는 class 안에 여러가지 function 을 넣어서 필요할 때마다 

class Merger():
    def __init__(self):
        pass
    def merge(self, input_filenames, output_filename):
        with open("./{}".format(output_filename), "w") as f:
            for fn in input_filenames:
                with open(fn, "r") as g:
                	lines = g.readlines()
                    f.writelines(lines)
        return

my_merger = Merger()
my_merger.merge(['kaist1.txt', 'kaist2.txt', 'kaist3.txt'], 'output.txt')

sleep(0.5) # Wait 0.5 seconds before creating a download link.
elice_utils.send_file('output.txt')
```



#### 실습2. 파일로부터 좌표 정보 읽어오기

> [CSV 파일을 읽고 쓰려면?](https://wikidocs.net/121964)
>
> CSV : comma seperated values
>
> TSV : tab seperated values
>
> split 함수 인자의 이름이 sep (seperator)

```python
# 내 풀이
# $ pip install pandas
import pandas as pd

# 데이터 불러오기
df = pd.read_csv('average-latitude-longitude-countries.csv', encoding = 'cp949', index_col = 0)

# 문제1. 2개의 리스트를 만들어, 다음 튜플들을 프린트
A = df[('country code', 'country name')]
B = df[('country code', 'latitude, longitude')]
print(A)
print(B)

# 문제2. 적도 남단의 모든 국가명을 출력
# 적도 남단: 적도의 위도(latitude)는 정의상 0도
# Latitude 값이 0 미만인 모든 국가명을 출력
C = df['latitude'] < 0
print(C)

# 문제3. 사용자가 국가코드를 입력하면 국가명을 출력
user_input = input()
D = df['country code'] == user_input
print(D)
```

```python
# 답안

# 데이터 불러오기
# Korea, Rebulic 처럼 국가명 안에, 처리가 있는 경우 아래 코드를 어떻게 수정할지 고민

# 문제1. 2개의 리스트를 만들어, 다음 튜플들을 프린트
# 문제2. 적도 남단의 모든 국가명을 출력
# 문제3. 사용자가 국가코드를 입력하면 국가명을 출력

# 답안 코드는 문제3 을 먼저 풀고, 여기서 정의된 요소를 바탕으로 문제2 풀게끔 작성

listA = list()
listB = list()
header = True
with open("./average-latitude-longitude-countries.csv", "r") as f:
    
    for line in f:
        if header:
            header = False
            continue
        items = line.strip().split(",")
        listA.append((items[0].strip('"'), ",".join(items[1:-2]).strip('"')))
        listB.append((items[0].strip('"'), (items[-2], items[-1])))
        
print(listA)
print(listB)

# define ranges for countries within lat/long ranges
# return country codes

def zone_countries(lat_range(-90, 90), long_range(-180, 180)):
    return [code for code, loc in listB if float(loc[0]) >= lat_range[0] and
           float(loc[0]) <= lat_range[1] and
           float(loc[1]) >= long_range[0] and
           float(loc[1]) <= long_range[1]]
    
print(zone_countries(lat_range(36, 38), long_range(126, 128)))

# take country code/s and return country name

def get_country_name(code):
    if type(code) is list:
        return_list = list()
        for one_code in code:
            return_list += [cn for cc, cn in listA if cc == one_code]
            return return_list
    elif type(code) is str:
        # print("str")
        return [cn for cc, cn in listA if cc == code]
    else:
        return
        
print(get_country_name("KR"))

southern_country_codes = zone_countries((-90, 0))
print(southern_country_codes)
print(get_country_name(southern_country_codes))
```



#### 실습3. 파일로부터 기온 정보 읽어오기

> 영국의 월별 기온 데이터가 1723년부터 1970년까지 주어져있습니다.
>
> 1.  데이터를 읽어와 각 연도의 겨울 평균 기온과 여름 평균 기온을 출력하세요
>
>    - 겨울 평균 = ( 1월 + 2월 ) / 2
>
>    - 여름 = ( 7월 + 8월 ) / 2
>
>    - 문자열 서식화를 통해 각 연도의 연평균 기온, 겨울 평균 기온, 겨울 평균 기온을 출력하세요
>
> 2.  읽어온 정보를 다른 확장자의 파일로 저장해보세요
>
>    - 파일명 `tpmon.csv`.
>    - 연도와 12개 월별 평균 기온이 한 줄에 포함되도록 하세요
>    - CSV 형식으로 작성하세요 (i.e. 각 데이터를 쉼표로 구분하세요).
>    - 파일을 다운받아 내용물을 확인하세요 `elice_utils.send_file('tpmon.csv')`
>    - 받은 파일을 엑셀로 열어보세요
>
> [(참고자료1)](https://zephyrus1111.tistory.com/38) [(참고자료2)](https://dsbook.tistory.com/20)

```python
with open("tpmon.txt", "r") as temp_data:
    x = []
    lines = temp_data.readlines()[1:] # readlines() --> 각 줄을 원소로 가지는 리스트가 반환
    for line in lines: # 한 줄씩 보기
        new_line = line.strip().split() # 각 줄에서 양 끝 공백을 잘라내고, 띄어쓰기 기준으로 자릅니다
        x.append(new_line) # 각 줄을 띄어쓰기로 자르고, 그 결과물을 x에 넣기




    with open("tpmon.csv", "w") as write_csv:
        for i, year_info in enumerate(x): # year_info는 각 연도의 월별 기온이 원소로 들어있는 리스트


            current_year = 1723 + i
            print("{}:\t {:.1f} / {:.1f}".format(current_year, (float(year_info[0])+float(year_info[1]))/2, (float(year_info[6])+float(year_info[7]))/2))

            write_csv.write(f"{', '.join(year_info)}, {current_year}") # 한 줄 쓰기
            write_csv.write("\n")
```



