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

  > 아래 2가지 컴포넌트는 평가 프로세스를 나누는 카테고리기도 함

  1. 검색기(Retriever) : 입력된 질문에 답변하는데 있어 가장 연관성 있는 정보를 검색
  2. 생성(Generator) : 검색된 정보를 바탕으로 답변을 생성