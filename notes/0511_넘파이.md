# ✅ [5/11] NumPy 표준 데이터 타입

> 1. NumPy 설치
> 2. NumPy 표준 데이터 타입
>
> 
>
> 💡 [NumPy Docs](https://numpy.org/doc/stable/user/quickstart.html)
>
> 💡 [데이터 사이언스 스쿨: 넘파이 배열 프로그래밍](https://datascienceschool.net/01%20python/03.01%20%EB%84%98%ED%8C%8C%EC%9D%B4%20%EB%B0%B0%EC%97%B4.html)



- NumPy 란?
  - Number (Numbers/Numerical) Python
  - 행렬이나 대규모 다차원 배열을 쉽게 처리할 수 있도록 지원하는 Python Lib. 데이터 구조 외에도 수치 계산을 위해 효율적으로 구현된 기능을 제공



## 1. NumPy 설치

> Anaconda 없이 Python 만 설치된 경우에 준함 (Anaconda Prompt 활용하면 Numpy 를 별도로 설치할 필요없이 활용할 수 있음)



- 가상환경의 필요성

  - 의존성 충돌 문제를 피하기 위해 프로젝트마다 독립된 패키지 환경을 만들고(=가상환경 구축) Numpy 설치

    - Pandas 가 제공하는 데이터 타입 하부 구조의 상당 부분이 Numpy 에 의존하고 있기 때문에, 글로벌 영역에 특정 버전의 Numpy 가 설치되어 있는 경우 Pandas 설치 후에 아래와 같은 에러가 발생할 수 있음
    - 따라서 Python 가상환경을 먼저 구축하고, 필요한 Numpy, Pandas 설치하여 패키지 충돌 문제를 해결

    ```bash
    ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts. pandas 2.0.1 requires numpy>=1.20.3; python_version < "3.10", but you have numpy 1.17.3 which is incompatible.
    ```



- 가상환경 및 Numpy 설치

  - 가상환경 생성 및 실행

    ```bash
    # 생성
    $ python -m venv venv
    
    # 실행
    $ source venv/Scripts/activate
    (venv)
    
    # (참고) 가상환경 종료
    $ deactivate
    ```

  - Numpy 설치

    ```bash
    # upgrade pip
    $ python -m pip install --upgrade pip
    
    # Numpy 설치
    $ pip install numpy
    
    # 설치된 Numpy 버전 확인
    $ pip list
    ```

    

- Numpy 잘 설치되었는지 간단히 확인

  ```python
  # Numpy 활용 예시 코드
  
  import numpy as np
  
  a = np.array([1, 2, 3])
  
  print(a)
  # [1 2 3] 출력되는 것을 확인
  
  print(type(a))
  # <class 'numpy.ndarray'> 출력되는 것을 확인
  ```

  

## 2. NumPy 표준 데이터 타입



- ndarray

  - NumPy 대표 자료형

  - N-dimensional array (N차원 배열)

  - Python List 와의 차이점 [(link)](https://datascienceschool.net/01%20python/03.01%20%EB%84%98%ED%8C%8C%EC%9D%B4%20%EB%B0%B0%EC%97%B4.html)

    > "많은 숫자 데이터를 하나의 변수에 넣고 관리할 때 리스트는 속도가 느리고 메모리를 많이 차지하는 단점이 있다. 배열(array)을 사용하면 적은 메모리로 많은 데이터를 빠르게 처리할 수 있다. 배열은 리스트와 비슷하지만 다음과 같은 점에서 다르다."

    - "모든 원소가 같은 자료형이어야 한다."
    - "원소의 갯수를 바꿀 수 없다."

    |           | Python List                      | NumPy Array                             |
    | --------- | -------------------------------- | --------------------------------------- |
    | 기능 차이 | 속도가 느리고 메모리를 많이 차지 | 적은 메모리로 많은 데이터를 빠르게 처리 |

  - ndarray 장점

    > "넘파이의 배열 연산은 C로 구현된 내부 반복문을 사용하기 때문에 파이썬 반복문에 비해 속도가 빠르며 벡터화 연산(vectorized operation)을 이용하여 간단한 코드로도 복잡한 선형 대수 연산을 수행할 수 있다." [(link)](https://datascienceschool.net/01%20python/03.01%20%EB%84%98%ED%8C%8C%EC%9D%B4%20%EB%B0%B0%EC%97%B4.html)

    - 연속된 메모리에 원소들이 저장됨
    - 속도 최적화를 위한 개발진의 지속적인 노력, 업데이트
    - 다양한 편의기능 (ndarray 클래스의 메서드)



- ndarray 기초 : 1차원 배열 만들기

  - 리스트를 인자로 받아 ndarray 로 변환시켜주는 array 함수 호출

    - `first_array = np.array([1, 2, 3])`
    - 타입을 확인해보자

    ```python
    import numpy as np
    
    first_array = np.array([1, 2, 3])
    
    print(first_array)
    # [1 2 3] 출력되는 것을 확인
    
    print(type(first_array))
    # <class 'numpy.ndarray'> 출력되는 것을 확인
    ```



- ndarray 의 성질 : ndim

  - `ndarray.ndim`
  - "important attribute of an ndarray object" [(link)](https://numpy.org/doc/stable/user/quickstart.html#advanced-indexing-and-index-tricks)
  - "the number of axes (dimensions) of the array" [(link)](https://numpy.org/doc/stable/user/quickstart.html#advanced-indexing-and-index-tricks)
  - "배열의 차원 및 크기를 구하는 더 간단한 방법은 배열의 `ndim` 속성과 `shape` 속성을 이용하는 것" [(link)](https://datascienceschool.net/01%20python/03.01%20%EB%84%98%ED%8C%8C%EC%9D%B4%20%EB%B0%B0%EC%97%B4.html)

  ```python
  import numpy as np
  
  a = np.array([1, 2, 3])
  
  print(a.ndim)   # 1 출력
  print(a.shape)  # (3, ) 출력
  
  b = np.array([[0, 1, 2], [3, 4, 5]])
  print(b.ndim)   # 2 출력
  print(b.shape)  # (2, 3) 출력
  ```

  

- ndarray 의 기능 : 인덱싱

  - 정수 순번/주소/위치로 특정 원소에 접근

    - "일차원 배열의 인덱싱은 리스트의 인덱싱과 같다" [(link)](https://datascienceschool.net/01%20python/03.01%20%EB%84%98%ED%8C%8C%EC%9D%B4%20%EB%B0%B0%EC%97%B4.html)

    ```python
    import numpy as np
    
    a = np.array([0, 1, 2, 3, 4])
    
    print(a[2])   # 2 출력
    print(a[-1])  # 4 출력
    ```

    - "다차원 배열일 때는 다음과 같이 콤마(comma ,)를 사용하여 접근할 수 있다. 콤마로 구분된 차원을 축(axis)이라고도 한다. 그래프의 x축과 y축을 떠올리면 될 것이다." [(link)](https://datascienceschool.net/01%20python/03.01%20%EB%84%98%ED%8C%8C%EC%9D%B4%20%EB%B0%B0%EC%97%B4.html)

    ```python
    import numpy as np
    
    a = np.array([[0, 1, 2], [3, 4, 5]])
    
    print(a)
    '''
    [[0 1 2]
     [3 4 5]]
    '''
    
    print(a[0, 0])   # 0 출력 (1번째 행의 1번째 열)
    print(a[0, 1])   # 1 출력 (1번째 행의 2번째 열)
    print(a[-1, -1]) # 5 출력 (마지막 행의 마지막 열)
    ```

  - 중첩된 ndarray 라면?

    - 리스트와의 차이에 주의 (예시: `list_example[0][1]` vs. `ndarray_example[0,1]`)

  - 음수 인덱싱



- ndarray 의 기능 : 슬라이싱

  - 리스트와 같이 `[start:end:step]` 문법을 따름
  - 만약, 여러 축을 슬라이싱 하고자 한다면?
    - `[start1:end1:step1, start2:end2:step2]`
  - "배열 객체로 구현한 다차원 배열의 원소 중 복수 개를 접근하려면 일반적인 파이썬 슬라이싱(slicing)과 comma(,)를 함께 사용하면 된다." [(link)](https://datascienceschool.net/01%20python/03.01%20%EB%84%98%ED%8C%8C%EC%9D%B4%20%EB%B0%B0%EC%97%B4.html)

  ```python
  import numpy as np
  
  a = np.array([[0, 1, 2, 3], [4, 5, 6, 7]])
  
  print(a)
  '''
  [[0 1 2 3]
   [4 5 6 7]]
  '''
  
  print(a[0, :])    # [0 1 2 3] 출력 (1번째 행 전체)
  print(a[:, 1])    # [1 5] 출력 (2번째 열 전체)
  print(a[1, 1:])   # [5 6 7] 출력 (2번째 행의 2번째 열부터 끝열까지)
  print(a[:2, :2])
  '''
  [[0 1]
   [4 5]] 출력
  '''
  ```
  
  
