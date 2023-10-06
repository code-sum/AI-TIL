# ✅ Docker Desktop 설치 및 실행

> 목표 : Windows OS 에 Docker Desktop 설치 및 실행



### 1. WSL2 세팅

- 현재 Windows 에 설치된 리눅스 버전이 WSL 인지, WSL2 인지 확인

  ```powershell
  wsl --list --verbose
  ```

- WSL 버전 기본값이 2가 아닌 다른 상태라면, 아래 명령어 실행해서 2 로 변경

  ```powershell
  wsl --set-default-version 2
  ```

  