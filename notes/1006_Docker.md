# ✅ Docker Desktop 설치 및 실행

> 목표 : Windows OS 에 Docker Desktop 설치 및 실행



### 1. WSL2 세팅하기

- 현재 Windows 에 설치된 리눅스 버전이 WSL 인지, WSL2 인지 확인

  ```powershell
  wsl --list --verbose
  ```

- WSL 버전 기본값이 2가 아닌 다른 상태라면, 아래 명령어 실행해서 2 로 변경

  ```powershell
  wsl --set-default-version 2
  ```




### 2. Docker Desktop 설치

- [다운로드 사이트](https://www.docker.com/products/docker-desktop/)에서 [Download for Windows] 클릭

- 다운로드 받은 `Docker Desktop Installer.exe` 파일 실행

- 설치 중간에 Configuration 창 뜨면, 둘 다 체크하고 설치 진행

  ![1006_Docker_1](1006_Docker.assets/1006_Docker_1.png)

  

  - 1번째 옵션은 WSL 관련
  - 2번째 옵션은 바탕화면에 아이콘 추가할지 여부

- 설치 완료되면 Installation succeeded 메세지 뜸

  ![1006_Docker_2](1006_Docker.assets/1006_Docker_2.png)

  - 시스템 상태에 따라 재시작이나 로그아웃 해야 하는 경우도 있음