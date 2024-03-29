# ✅ 프로젝트 환경세팅



- VSCODE 설치 https://crazykim2.tistory.com/748

- Python 설치 및 환경변수 설정 

  https://danmilife.tistory.com/26

  - 이건 Global 의 경우이므로 참고만 하고, 실제로는 각 프로젝트마다 별도의 가상환경을 구축하고 각각 필요한 버전의 Python 패키지를 설치할 것

- Ubuntu 설치
> WSL(Windows Subsystem for Linux)은 Windows에 리눅스 운영체제를 설치할 수 있게 해주는 하위 시스템(subsystem)이다. WSL에 우분투(Ubuntu), 오픈수세(OpenSUSE), 칼리(Kali), 데비안(Debian), 아치 리눅스(Arch Linux) 등을 설치할 수 있다. [(link)](https://wikidocs.net/205061)
> Ubuntu 는 영국 기업 캐노니컬이 개발, 배포하는 컴퓨터 운영 체제이다. 데비안 리눅스를 기반으로 개발되며, 데비안에 비해 '사용자 편의성'에 초점을 맞춘 리눅스 배포판이다. [(link)](https://ko.wikipedia.org/wiki/%EC%9A%B0%EB%B6%84%ED%88%AC)

- 설치 가이드
  - https://learn.microsoft.com/ko-kr/windows/wsl/install
  - https://wotres.tistory.com/entry/WSL-windows-에-ubuntu-설치-하는-법
  - https://makepluscode.tistory.com/216

- 명령 프롬프트 관리자 권한으로 실행 후 `wsl --install`

- 설치 결과 : WSL 설치하면 Ubuntu 도 함께 설치됨

  ```powershell
  Microsoft Windows [Version 10.0.22621.2283]
  (c) Microsoft Corporation. All rights reserved.
  
  C:\Windows\System32>wsl --install
  설치 중: 가상 머신 플랫폼
  가상 머신 플랫폼이(가) 설치되었습니다.
  설치 중: Linux용 Windows 하위 시스템
  Linux용 Windows 하위 시스템이(가) 설치되었습니다.
  설치 중: Ubuntu
  Ubuntu이(가) 설치되었습니다.
  요청한 작업이 잘 실행되었습니다. 시스템을 다시 시작하면 변경 사항이 적용됩니다.
  
  C:\Windows\System32>
  ```

- 위 상태에서 PC 다시시작 하면 아래와 같이 username, password 설정하는 명령어 뜸

  ```powershell
  Ubuntu이(가) 이미 설치되어 있습니다.
  Ubuntu을(를) 시작하는 중...
  Installing, this may take a few minutes...
  Please create a default UNIX user account. The username does not need to match your Windows username.
  For more information visit: https://aka.ms/wslusers
  Enter new UNIX username: [username]
  New password: [password]
  ```

- ID / PW 설정 결과

  ```powershell
  Ubuntu이(가) 이미 설치되어 있습니다.
  Ubuntu을(를) 시작하는 중...
  Installing, this may take a few minutes...
  Please create a default UNIX user account. The username does not need to match your Windows username.
  For more information visit: https://aka.ms/wslusers
  Enter new UNIX username: [username]
  
  New password: [password]
  Retype new password: [password]
  passwd: password updated successfully
  Installation successful!
  To run a command as administrator (user "root"), use "sudo <command>".
  See "man sudo_root" for details.
  
  Welcome to Ubuntu 22.04.2 LTS (GNU/Linux 5.15.90.1-microsoft-standard-WSL2 x86_64)
  
   * Documentation:  https://help.ubuntu.com
   * Management:     https://landscape.canonical.com
   * Support:        https://ubuntu.com/advantage
  
  
  This message is shown once a day. To disable it please create the
  /home/[username]/.hushlogin file.
  [username]@DESKTOP-CHN2AFA:~$
  ```

- pyenv 설치 및 가상환경 활성화

  - 가이드

    - https://nightskyshop1023.tistory.com/9
    - https://nightskyshop1023.tistory.com/10
    - https://bustermachinelab.net/wsl2%EC%97%90-pyenv-virtualenv-%EA%B5%AC%EC%B6%95%ED%95%98%EA%B8%B0/

  - WSL 내의 ubuntu 인 경우 아래 명령어를 실행하여 pyenv 설치 필요한 것들을 먼저 설치

    ```powershell
    $ sudo apt-get update;
    $ sudo apt-get install make build-essential libssl-dev zlib1g-dev \
    libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
    libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
    ```

  - pyenv 에서 제공하는 자동 설치 도구 이용

    - 아래 코드로 virtualenv 도 같이 설치됨

      ```powershell
      $ curl https://pyenv.run | zsh   # zsh 경우
      $ curl https://pyenv.run | bash   # bash shell 경우
      $ exec $SHELL
      ```

    - pyenv 관련 환경설정

      ```powershell
      $ sed -Ei -e '/^([^#]|$)/ {a \
      export PYENV_ROOT="$HOME/.pyenv"
      a \
      export PATH="$PYENV_ROOT/bin:$PATH"
      a \
      ' -e ':a' -e '$!{n;ba};}' ~/.profile
      ```

      ```powershell
      $ echo 'eval "$(pyenv init --path)"' >>~/.profile
      ```

      ```powershell
      $ echo 'eval "$(pyenv init -)"' >> ~/.bashrc
      ```

      ```powershell
      $ echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
      ```

    - pyenv 설치 확인

      ```powershell
      $ exec $SHELL
      $ pyenv --version
      ```

  - 설치 가능한 Python 버전 목록 확인

    ```powershell
    $ pyenv install --list
    ```

  - 원하는 Python 버전 설치

    ```powershell
    $ pyenv install 3.11.5
    $ pyenv install 3.10.6
    ```

  - virtualenv으로 가상 환경 생성

    ```powershell
    $ pyenv virtualenv <파이썬버전> <내환경이름>
    ```

  - 생성한 가상환경 활성화

    ```powershell
    $ pyenv local <내환경이름>
    또는 
    $ pyenv shell <내환경이름>
    
    $ python -V  # Python 버전 확인
    ```

  - 생성한 가상환경을 현재 작업을 위한 환경으로 설정

    - local 로 작성하면, 특정 폴더만 현재 환경을 적용

    - global, local 둘 다 적용시켜 놓는 것이 좋음

      ```powershell
      $ pyenv global 3.10.6
      ```

- 협업하려는 원격저장소를 본인의 로컬에 clone

  - 원격저장소에 접근 권한이 없는경우 404 페이지가 보임
  - SSH 방식
  - HTTP 방식

- VSCODE 에 Python 확장 프로그램 설치

- 만들어놓은 가상환경이 있는 경우, 가상환경 활성화

  - 가이드 https://nightskyshop1023.tistory.com/10

  - clone 받은 디렉토리로 이동

    ```powershell
    $ cd <디렉토리명>
    ```

  - clone 받은 디렉토리에 미리 만들어놓은 가상환경 적용

    ```powershell
    $ pyenv local <내환경이름>
    ```

- Ubuntu 로 접근한 VSCODE Extensions 에서 Jupyter, Python Extension Pack 설치

  - Jupyter, ipykernel 설치 (경로 꼬이지 않도록 가상환경당 jupyter를 설치해 실행하는 것 추천)

  - 가이드 

    - https://shangom-developer.tistory.com/2

    ```bash
    $ pip install jupyter
    ```

    ```bash
    $ pip install ipykernel
    ```

- 가상환경 디렉토리 폴더가 있는 디렉토리에서 Jupyter 실행

  ```bash
  $ jupyter notebook
  ```

  

