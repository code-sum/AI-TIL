# ✅ Ragas

> **[참고자료]**
>
> - Ragas 공식문서 [(link)](https://docs.ragas.io/en/latest/)
> - Ragas Github [(link)](https://github.com/explodinggradients/ragas)
> - LangChain "RAG Evaluation" Webinar [(link)](https://www.youtube.com/watch?v=fWC4VxolWAk) (23.08.25)
> - [LangChain Blog] [Evaluating RAG pipelines with Ragas + LangSmith](https://blog.langchain.dev/evaluating-rag-pipelines-with-ragas-langsmith/) (23.08.23)
> - [Medium] [RAG Evaluation](https://cobusgreyling.medium.com/rag-evaluation-9813a931b3d4) (23.09.01)
> - [Medium] [Combining Ragas (RAG Assessment Tool) with LangSmith](https://cobusgreyling.medium.com/combining-ragas-rag-assessment-tool-with-langsmith-e46078001f95) (23.09.06)



- Ragas
  - *"Evaluation framework for your Retrieval Augmented Generation (RAG) pipelines."*
  - 평가, 모니터링 기능을 제공하여 프로덕션 단계의 LLM & RAG application 성능을 높임



- Ragas 의 평가 대상

  > 아래 2가지 컴포넌트는 평가 프로세스를 나누는 카테고리기도 하며, QA pipeline 을 평가하기 위해선 2가지 컴포넌트 모두를 평가 대상으로 삼아야 함

  1. 검색기(Retriever) : 입력된 질문에 답변하는데 있어 가장 연관성 있는 정보를 검색
  2. 생성기(Generator) : 검색된 정보를 바탕으로 답변을 생성



- Ragas Score

  > 아래 4가지 항목의 조화 평균(harmonic mean) 계산

  ![1223_Ragas](1223_Ragas.assets/1223_Ragas.png)

  - 생성(generation) 성능을 평가하는 지표
    - `faithfulness` : 답변의 정확도. 생성된 답변에 환각현상(hallucinations)이 얼마나 있는지(=혹은 생성된 답변이 얼마나 정확한지) 측정
    - `answer_relevancy` : 질문과의 연관도. 생성된 답변이 질문 내용과 얼마나 연관성이 높은지 측정
  - 검색(retrieval) 성능을 평가하는 지표
    - `context_precision`
    - `context_recall`