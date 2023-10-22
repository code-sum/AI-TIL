# ✅ [4/24] 파이썬 기초

> 1. 휴보
> 2. 개념복습



휴보



---



개념복습



- input 함수가 받는 것은 무조건 문자열(string)



- Python 은 동적 타입 언어(Dynamic Typed Language)

  - Python, JavaScript, Ruby 는 변수 선언 시 자료형(type)을 지정하지 않음. 값을 할당하면 그때 동적으로 자료형이 정해짐
    ``` python
    def add(a, b):
        return x + y
    ```

  - 반면, C, C++, C#, Java 는 정적 타입 언어(Static Typed Language). 변수를 처음 선언할 때부터 자료형을 같이 입력해야 함

    ```C
    int add(int a, int b)
    {
        return a + b;
    }
    ```



- Python 은 interpreted language
  - 컴파일하지 않고도, 작성된 코드 그대로 컴퓨터에 명령
  - 반면, C, C++ 과 같은 compiled language 는 컴파일된 파일로 컴퓨터에 명령



- 디버깅

  - 디버깅은 실험하는 과정과 비슷

  - 버그라고 불리는 오류에는 다음과 같은 종류

    1. Syntax error : Python 이 작성한 프로그램을 이해하지 못합니다. 프로그램을 실행할 수 없습니다.

       ```python
       # Syntax error 예시
       >>> a
       NameError: name 'a' is not defined
       ```

    2. Runtime error : 1. 보단 나은 상황. 프로그램 실행으로 한 걸음 더 나아간 상태. 프로그램 실행 중에(runtime) 에러 메시지와 함께 프로그램이 갑자기 종료되는 것을 말합니다.

       ```python
       # Runtime error 예시
       >>> b = [0, 1, 2]
       >>> b[0]
       0
       >>> b[3]
       IndexError: list index out of range
       ```

    3. Semantic error : 증상이 없기 때문에 가장 까다로운 에러에 해당. 프로그램이 에러 메시지 없이 실행되지만, 사용자가 기대하지 않은 실행 결과가 나오는 것을 말합니다. 

       ```python
       # Semantic error 예시
       # 사용자는 3*2 연산을 기대했지만, 3의 2승 출력
       >>> 3**2
       9
       ```

       

- 줄바꿈, 탭

  ```python
  print('\\n')  # \n 출력
  print('\n')   # 줄바꿈이 있는 공백만 출력
  
  '''
  즉, \\n 처럼 \ (백 슬래쉬) 하나 더 붙여주면
  \n은 특수문자(줄바꿈) 역할이 아닌, 문자열 그대로 출력
  '''
  ```


