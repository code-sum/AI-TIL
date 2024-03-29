# ✅ [5/9] 전체 복습 (4/24 ~ 5/7)

> 1. 기초 사용법, 출력, 데이터 타입, 변수, 주석
>
> 2. input
>
> 3. 반복문, 조건문
>
> 4. 함수
>
> 5. 리스트와 튜플
>
> 6. 사전형과 집합
>
> 7. 객체지향 프로그래밍



이 수업 + 수업자료에서 시험 출제 예정이니까, 실시간 수업 잘 듣기!

CS101 자료는 출제X

(⭐⭐⭐ 표기 슬라이드 출제 가능성 높음)



내일은 여태까지 출제된 실습, 미션 문제 전부 풀이 예정



---



## 1. 기초 사용법, 출력, 데이터 타입, 변수, 주석



- 1, 0 을 Boolean (`True`, `False`) 으로 사용할 수 있는가?

  ```python
  int_zero = 0
  int_non_zero = 2
  
  if int_non_zero:
      print("non-zero")
      
  # 0 == False 는 True
  # 1 == True 는 True
  # 그 외 0이 아닌 정수는 True 가 아님
  # print(1 == True)
  ```

- `+=`, `-=`, `*=`, `/=` 연산 방식이 지수에도 적용이 되는가?

  ```python
  a = 2
  for i in range(3):
      # a = a**2
      a **= 2
  print(a)
  # 256
  ```

  

## 2. input



- 반올림 표기법 차이

  ```python
  a = 1.783874
  
  # 1. 내장함수 round()
  print(round(a, 1))
  # 1.8
  
  # 2. 포매팅 .1f
  print(f'{a:.1f}')
  # 1.8
  
  '''
  결과적으로는 둘 다 동일
  print 이후 연산이 더 있다면 round() 쓰고,
  print 이후 연산이 없고 프린트값만 필요하면 f 포매팅!
  용도에 따라 적절히 선택해서 사용하기
  
  그러나 round() 는
  부동소수점 에러(floating point precision error)
  발생할 수 있으니, 정확한 결과가 필요하다면
  포매팅 활용하는 것을 추천
  ex) round(2.675, 2)
  '''
  ```

- 문자열 서식화 방법 3가지

  ```python
  a = 2.23525
  
  print(f'{a:.2f}')
  print("%.2f" %a)
  print("{:.2f}".format(a))
  
  # 2.24
  # 2.24
  # 2.24
  ```

  

## 3. 반복문, 조건문

> ⭐⭐⭐ For



- For 반복문은 어떤 객체를 순회하는가?

  ```python
  for a in (list):
      # list 자리는 리스트가 아니더라도, 
      # 순회 가능한(iterable) 자료형이면 무엇이든 들어갈 수 있음
      # tuple, set 다 가능
  
  # range() 의 타입이 리스트는 아니라는 점에 유의!
  range_ex = range(10)
  print(type(range_ex)) 
  # <class 'range'>
  ```



## 4. 함수

> ⭐⭐⭐ 함수의 재귀적 용법 (특히 `factorial`)



- 함수 호출 시 반드시 괄호가 필요하다

  > 아래 코드에서 반환된 `<function add at 0x000002987ED4D400>` 가 에러는 아니고, add 라는 함수가 어디에 저장되어 있는지를 보여주는건데 우리 수업 수준에서 이 경로를 사용하진 않을 것

  ```python
  def add(a, b):
      return a + b
  
  total = add(3, 4)
  
  print(total)      # 7
  print(add(5, 4))  # 9
  print(add)        # <function add at 0x000002987ED4D400>
  ```

- 반환값이 없는 함수(void function)

  > return 문이 없이 함수를 마치는 경우
  >
  > return 문이 없으면 자동으로 None 반환
  >
  > 아래 #1, #2 코드는 서로 같음

  ```python
  # 1
  def print_symbol(sym):
      for i in range(20):
          print(sym, end='')
      print('')
  
  # 2
  def print_symbol(sym):
      for i in range(20):
          print(sym, end='')
      print('')
      return None
  ```

- 명시적으로 return 을 선언하지 않는 모든 경우에 None 을 return

  ```python
  def foo():
      pass
  
  def goo():
      return None
  
  # 아래 2줄은 같은 결과(None) 반환
  print(foo())
  print(goo())
  ```

- 함수의 재귀적 용법

  > 함수 내에서 자기 자신을 호출 할 수 있는데, 이것을 함수의 재귀적 용법(recursion)이라 한다.
  >
  > 큰 문제를 작은 문제로 나누어 풀 때 이용한다.
  >
  > 종료 조건이 반드시 있어야 한다.

  ```python
  def factorial(n):
      if n == 1:  # 종료조건
          return 1
      return n*factorial(n-1)
  ```

  

## 5. 리스트와 튜플

> ⭐⭐⭐ 리스트와 튜플의 응용, 컴프리헨션(comprehension)
>
> (람다함수는 출제 X)



- 리스트 순서 거꾸로 뒤집는 3가지 방법

  > 1. `[::-1]`
  >
  > 2. `.reverse`
  >
  > 3. `.sort(reverse=True)` 

  ```python
  numbers = [1, 2, 3, 4, 5, 6, 7, 8]
  
  print(numbers[::-1])
  
  # [8, 7, 6, 5, 4, 3, 2, 1]
  ```

  ```python
  numbers = [1, 2, 3, 4, 5, 6, 7, 8]
  
  numbers.reverse()
  print(numbers)
  
  # [8, 7, 6, 5, 4, 3, 2, 1]
  ```

  ```python
  numbers = [1, 2, 3, 4, 5, 6, 7, 8]
  
  numbers.sort(reverse=True)
  print(numbers)
  
  # [8, 7, 6, 5, 4, 3, 2, 1]
  ```

- 튜플 unpacking

  > 튜플은 원소의 요소를 바꿀 수 없기 때문에, 2개 원소의 요소를 바꿔야 하는 작업에서 튜플 언패킹을 활용
  >
  > interable 객체는 모두 unpacking 가능

  ```python
  s1 = 'first'
  s2 = 'second'
  s1, s2 = s2, s1
  
  print(s1, s2)
  # second first
  ```

- 리스트 unpacking

  > 매개변수에서 *을 붙이는게 아니라
  >
  > 인자 앞에 *을 붙여서 활용

  ```python
  def sum(a, b, c):
      return a + b + c
  
  numbers = [1, 2, 3]
  sum(numbers)  # error
  
  print(sum(*numbers))  # 6
  ```


- 얕은 복사, 깊은 복사

  ```python
  # 얕은 복사란?
  
  import copy
  
  a = [1, 2]
  b = copy.copy(a)
  or
  b = a[:]
  
  '''
  위 얕은 복사의 경우, b 또는 a 값을 수정하면
  양쪽이 모두 변한다는 문제점이 있다.
  
  list 와 같은 mutable 객체가 중첩되어 있을 때
  얕은 복사의 문제가 발생한다.
  '''
  ```

  ```python
  a = [11, 22, [1, 2]]  # nested list
  b = a[:]
  
  print(a is b)  # False
  print(id(a), id(b))  # id 도 서로 다름
  
  b[2].append(9)
  print("b: ", b)  # b:  [11, 22, [1, 2, 9]]
  print("a: ", a)  # a:  [11, 22, [1, 2, 9]]
  ```

  ```python
  # 위 문제를 피하기 위해 깊은 복사 코드 작성
  
  import copy
  
  a = [[1, 2], [3, 4]]
  
  b = copy.deepcopy(a)
  ```

- `sum()` 함수는 산술 연산 '+' 가 가능한 시퀀스 자료의 합을 구해준다

  > 문자열(`str`), 리스트(`list`)끼리의 합은 구할 수 없음



## 6. 사전형과 집합

> ⭐⭐⭐ 중복을 허용하는 자료형, 순서가 있는 자료형, 가변적인 자료형인지 ~ 집합, 사전, 문자열, 리스트, 튜플들 특성 전부 정리하기 (시험출제)



## 7. 객체지향 프로그래밍

> ⭐⭐⭐ 모델 가져오기, 모델의 매서드 가져오기에 유의, 오버라이딩, 추상 클래스(4지 선다형 개념문제 - 왜 사용할까? 에 유의)



- 오버라이딩

  > 클래스 기반의 라이브러리를 사용할 때, 오버라이딩에 주의해야 하는 경우가 많기 때문에 시험 출제예정
  >
  > `super()` 도 출제예정

  ```python
  # 상위 클래스의 .eat() 을 불러오려면 super()
  
  class Animal():
      def eat(self):
          print('animal: eat')
  
  class Dog(Animal):
      def eat(self):
          print('dog: eat')
      def parent_eat(self):
          super.eat()
  ```

  
