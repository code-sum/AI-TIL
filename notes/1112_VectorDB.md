# ✅ VectorDB 비교

> 1. Chroma
> 2. OpenSearch
> 3. Weaviate
> 4. FAISS

![vector](https://github.com/code-sum/AI-TIL/assets/106902415/1d3a805c-8099-4ac6-8861-9c5de8d33e39)
📋 [(Image Source)](https://www.pinecone.io/learn/vector-database/)

### VectorDB (Vector Database) 란?
  > "벡터 데이터베이스는 벡터를 고차원 포인트로 저장하고 검색하는 기능을 제공합니다. N차원 공간에서 가장 가까운 이웃을 효율적이고 빠르게 조회할 수 있는 추가적인 기능을 추가합니다. 일반적으로 k-NN(k-Nearest Neighbor) 인덱스로 구동되며 계층적 탐색 가능한 소규모 세계(HNSW) 및 반전된 파일 인덱스(IVF) 알고리즘과 같은 알고리즘으로 구축됩니다. 벡터 데이터베이스는 데이터 관리, 내결함성, 인증 및 액세스 제어, 쿼리 엔진과 같은 추가 기능을 제공합니다." - AWS


![vector2](https://github.com/code-sum/AI-TIL/assets/106902415/d369f327-e8ee-4fc1-a5f1-d091811b7e7d)
📋 [(Image Source)](https://blog.det.life/why-you-shouldnt-invest-in-vector-databases-c0cd3f59d23c)

### 1. Chroma [(공식)](https://www.trychroma.com/) [(GitHub)](https://github.com/chroma-core/chroma)
   - 장점
     - 오픈소스
     - 설치가 쉬움 (local 에 구성)
   - 단점
### 2. OpenSearch [(공식)](https://opensearch.org/) [(GitHub)](https://github.com/opensearch-project)
   - 장점
     - 오픈소스 ([Elasticsearch](https://www.elastic.co/kr/elasticsearch) 코드 베이스를 Fork 한 오픈소스 검색 엔진)
   - 단점
     - [Quickstart](https://opensearch.org/docs/latest/quickstart/) 참고하여 `docker-compose.yml` 다운로드 받고 up 시켜보면, 컨테이너가 3개나 구동됨
### 3. Weaviate [(공식)](https://weaviate.io/) [(GitHub)](https://github.com/weaviate/weaviate)
   - 장점
     - 오픈소스
     - Docker 컨테이너 1개만 구동해도 활용 가능
   - 단점
### 4. FAISS [(공식)](https://faiss.ai/) [(GitHub)](https://github.com/facebookresearch/faiss)
   - 장점
     - 오픈소스
     - 속도가 매우 빠름 (인터페이스는 Python 이나 C++ 로 제작, GPU 차원에서도 효율적으로 동작하도록 개발됨)
   - 단점
     - 활용도가 제한적 (엄밀히 따지면 VDB 내의 Vector Index 관련 기능만 지원)
