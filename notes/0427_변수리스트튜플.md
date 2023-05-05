# ✅ [4/27] 지역 변수, 전역 변수, 리스트, 튜플

> - CS101 Lecture 8. 매개 변수와 반환값을 가진 함수
> - CS101 Lecture 9. 함수를 사용한 로봇 조종 및 디지털 사진 변환 프로그램
> - CS101 Lecture 10. 함수 인자와 매개 변수
> - 실습1. 매개 변수와 반환값을 가진 함수
> - 실습2. 함수를 사용한 로봇 조종 및 디지털 사진 변환 프로그램
> - 실습3. 함수 인자와 매개 변수
> - 실습4. 함수가 사용하는 지역 변수와 전역 변수



---



#### 실습1. 매개 변수와 반환값을 가진 함수

```python
name = input("What is your name? ")
print("Welcome to CS101, " + name)

raw_n = input("Enter a positive integer> ")
n = int(raw_n)
for i in range(n):
  print( "*" * i)
```



#### 실습2. 함수를 사용한 로봇 조종 및 디지털 사진 변환 프로그램

```python
from cs1media import *

def luma(p):
  r, g, b = p
  return int(0.299 * r + 0.587 * g + 0.114 * b) 

white = (255, 255, 255)
black = (0, 0, 0)

def blackwhite(img, threshold):
  w, h = img.size()
  for y in range(h):
    for x in range(w):
      v = luma(img.get(x, y))
      if v > threshold:
        img.set(x, y, white)
      else:
        img.set(x, y, black)

pict = load_picture("./photos/yuna1.jpg")
blackwhite(pict, 100)
pict.show()
```



#### 실습3. 함수 인자와 매개 변수

```python
def swap(a, b):
  a, b = b, a
  
x, y = 123, 456
swap(x, y)
print(x, y)


'''
출력값
123 456
'''
```



#### 실습4. 함수가 사용하는 지역 변수와 전역 변수

```python
a = "Letter a"

def f(a):
  print("A = ", a)
  
def g():
  a = 7
  f(a + 1)
  print("A = ", a)
  
print("A = ", a)
f(3.14)
print("A = ", a)
g()
print("A = ", a)


'''
출력값
A = Letter a
A = 3.14
A = Letter a
A = 8
A = 7
A = Letter a
'''
```



---



휴보 코드 실습

- 객체는 이름 여러개를 가질 수 있음
- 이름은 여러 객체를 가리킬 순 없음

```python
from cs1robots import *
import time

create_world(avenues = 5, streets = 5)
sleep_time = 0.5

hubo = Robot("yellow")
time.sleep(sleep_time)
hubo.move()
ami = hubo  # <- ami, hubo 는 동일한 객체
time.sleep(sleep_time)
ami.turn_left()
time.sleep(sleep_time)
hubo.move()

time.sleep(sleep_time)
hubo = Robot("blue")  # 
time.sleep(sleep_time)
hubo.move()
time.sleep(sleep_time)
ami.turn_left()
time.sleep(sleep_time)
ami.move()
```

