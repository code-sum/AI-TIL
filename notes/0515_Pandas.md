# ✅ [5/15] Pandas 객체소개



- Pandas 란?
  - Python 기반 데이터 분석 및 데이터 처리 라이브러리
  - https://pandas.pydata.org/



- Pandas 설치 가이드 

  - Anaconda 를 이용한 설치 [(link)](https://pandas.pydata.org/getting_started.html)

  - pip 를 이용한 설치

    - 미리 구축한 가상환경 실행

      ```bash
      $ pyenv activate [가상환경이름]
      ```

    - 실행중인 가상환경에 Pandas 설치

      ```bash
      $ pip install pandas
      ```

    - 패키지 import (아래와 같이 alias 로 `pd` 를 주로 사용)

      ```python
      import pandas as pd
      ```



- CSV 파일에서 데이터 불러오기

  - 불러온 데이터를 `df` 라는 이름의 `DataFrame` 객체에 로드
  - `DataFrame` 은 Pandas 에서 데이터를 다루는 기본적인 구조

    ```python
    import pandas as pd

    df = pd.read_csv("sample.csv")
    ```
      
