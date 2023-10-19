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


- OpenSearch 에서 제공해주는 Docker Container 가 정상적으로 실행되었다면 위 명령어 실행 결과는 아래와 같음

  ```bash
   NAME                    COMMAND                  SERVICE                 STATUS              PORTS
   opensearch-dashboards   "./opensearch-dashbo…"   opensearch-dashboards   running             0.0.0.0:5601->5601/tcp
   opensearch-node1        "./opensearch-docker…"   opensearch-node1        running             0.0.0.0:9200->9200/tcp, 9300/tcp, 0.0.0.0:9600->9600/tcp, 9650/tcp
   opensearch-node2        "./opensearch-docker…"   opensearch-node2        running             9200/tcp, 9300/tcp, 9600/tcp, 9650/tcp
  ```

  