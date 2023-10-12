# ✅ OpenSearch Quickstart

> 참고자료 : https://opensearch.org/docs/latest/quickstart/



- OpenSearch 에서 제공해주는 Compose file 샘플 다운로드

  ```bash
  # Using cURL:
  
  curl -O https://raw.githubusercontent.com/opensearch-project/documentation-website/2.10/assets/examples/docker-compose.yml
  ```

- `docker-compose.yml` 파일을 다운로드 받은 디렉토리로 이동해서 아래 명령어 실행하면, 백그라운드 프로세스로 클러스터가 생성되고 실행됨

  ```bash
  # -d 옵션은 Docker 컨테이너를 백그라운드 프로세스로 실행하는 옵션
  
  docker-compose up -d
  ```

- 아래 명령어 실행해서 실행중인 컨테이너들을 확인할 수 있음

  ```bash
  docker-compose ps
  ```

  