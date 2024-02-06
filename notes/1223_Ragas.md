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



- LLM in Ragas
  - **특징** : LLM 은 스스로 생성한 출력물을 중시하며, 서로 다른 출력물(outputs)을 비교해 달라고 요청받았을 때, 출력물의 상대적인 포지션을 중시함
  - **장점** : 얼마나 인간적인 판단을 내리느냐의 관점에서 볼 때, 평가에 LLM 을 활용하는 방식이 전통적인 평가지표(metrics) 보다 나음
    - *metrics : Metrics are measures of [quantitative assessment](https://www.investopedia.com/articles/investing/041114/simple-overview-quantitative-analysis.asp) commonly used for assessing, comparing, and tracking performance or production.*
  - **단점** : LLM 은 점수를 매겨 달라는 요청을 받았을 때 편견(bias)의 영향을 받을 수 있고, 길이가 긴 답변들을 중시하는 경향도 있음
    - 예를 들어, 1 부터 10까지 숫자 중에 난수를 생성해 달라고 100번 요청 받았을 때, 7을 출력하는 비중이 압도적으로 높았던 사례도 발견됨 [(link)](https://www.youtube.com/watch?v=fWC4VxolWAk)
  - Ragas 또한 평가 기능을 위해 내부적으로(under the hood) LLM 을 활용하긴 함
  - 그러나 Ragas 는 LLM 을 QA pipeline 평가에 활용할 때 발생하는 위 단점들을 해결하고자 하며, 가능한 한 데이터 어노테이션이 적은 평가지표를 제공함
    - *데이터 어노테이션* *: 데이터셋에 메타데이터를 추가하는 작업. ‘태그’ 형식으로 이미지, 텍스트, 비디오를 비롯한 모든 유형의 데이터에 추가가 가능. 쉽게 말해 인공지능이 데이터의 내용을 이해할 수 있도록 주석을 달아주는 작업을 의미*



- Ragas 의 평가 대상

  > 아래 2가지 컴포넌트는 평가 프로세스를 나누는 카테고리기도 하며, QA pipeline 을 평가하기 위해선 2가지 컴포넌트 모두를 평가 대상으로 삼아야 함

  1. 검색기(Retriever) : 입력된 질문에 답변하는데 있어 가장 연관성 있는 정보를 검색
  2. 생성기(Generator) : 검색된 정보를 바탕으로 답변을 생성



- Ragas Score

  > 아래 4가지 항목의 조화 평균(harmonic mean) 계산

  ![1223_Ragas](1223_Ragas.assets/1223_Ragas.png)

  - 생성(generation) 성능을 평가하는 지표
    - `faithfulness` : 신뢰도(=답변의 정확도). 생성된 답변에 환각현상(hallucinations)이 얼마나 있는지(=혹은 생성된 답변이 얼마나 정확한지) 측정
    - `answer_relevancy` : 질문과 답변의 연관도. 생성된 답변이 질문 내용과 얼마나 연관성이 높은지 측정
  - 검색(retrieval) 성능을 평가하는 지표
    - `context_precision` : 컨텍스트 정밀도. context 내부 chunks 들이 ground_truth(=사실이라고 정의된 것들)에 얼마나 부합하는지를 계산
      - (ML 에서 precision 은 모델이 True라고 분류한 것 중에서 실제 True인 것의 비율)
    - `context_recall` : 컨텍스트 재현도. 질문에 답변하는 과정에서 ‘필요한 모든 필수 정보’를 ‘검색기’가 검색할 수 있는지를 계산
      - (ML 에서 recall 은 실제 True인 것 중에서 모델이 True라고 예측한 것의 비율)
    - [참고자료 / Machine Learning] precision vs. recall 개념 구분 [(link)](https://sumniya.tistory.com/26)



- Ragas 활용 예시

  1. `pip install ragas`

  2. 평가를 위한 Chain 만들기

  3. `from ragas.metrics` 에서 평가에 필요한 모든 항목 import 

  4. `from ragas.langchain` 에서 `RagasEvaluatorChain` import

     - ragas 평가 항목을 LangChain [EvaluationChain](https://python.langchain.com/docs/guides/evaluation/?ref=blog.langchain.dev) 으로 변환시켜 주는 체인

     ```python
     from ragas.metrics import faithfulness, answer_relevancy, context_precision, context_recall
     from ragas.langchain import RagasEvaluatorChain
     
     # make eval chains
     eval_chains = {
         m.name: RagasEvaluatorChain(metric=m) 
         for m in [faithfulness, answer_relevancy, context_precision, context_recall]
     }
     ```

  5. 위 코드로 평가용 체인이 만들어지면, 아래 코드를 작성하여 평가용 체인을 호출

     ```python
     # evaluate
     for name, eval_chain in eval_chains.items():
         score_name = f"{name}_score"
         print(f"{score_name}: {eval_chain(result)[score_name]}")
     
     # 평가용 체인 호출은 __call__() 메서드 활용
     
     # output
     # faithfulness_score: 1.0
     # answer_relevancy_score: 0.9193459596511587
     # context_precision_score: 0.07480974380786602
     # context_recall_score: 0.9193459596511587
     ```

     
- 평가용 LLM 커스텀
  > 참고자료 : [공식문서] Bring your own LLMs [(link)](https://docs.ragas.io/en/latest/howtos/customisations/llms.html)

  1. 평가를 위한 `dataset` 세팅
  
     ```python
     from datasets import Dataset
 
     # To dict
     data = {
         "question": questions,
         "answer": answers,
         "contexts": contexts,
         "ground_truths": ground_truths
     }
    
     # Convert dict to dataset
     dataset = Dataset.from_dict(data)
     ```
     
  2. RAGAS 에 내장된 LLM 버전 `gpt-3.5-turbo-16k` >> `gpt-4-1106-preview` 로 업그레이드
 
     ```python
     from ragas import evaluate
     from ragas.metrics import (
         faithfulness,
         answer_relevancy,
         context_precision,
         context_recall,
     )
     from langchain_openai import ChatOpenAI
     from ragas.llms import LangchainLLM
    
     ragas_llm = ChatOpenAI(
         model="gpt-4-1106-preview", 
         temperature=0.5
     )
    
     gpt4_wrapper = LangchainLLM(llm=ragas_llm)
    
     faithfulness.llm = gpt4_wrapper 
     answer_relevancy.llm = gpt4_wrapper 
     context_precision.llm = gpt4_wrapper
     context_recall.llm = gpt4_wrapper
     ```
  
  3. 평가 실행
 
     ```python
     result = evaluate(
     dataset = dataset, 
     metrics=[
          faithfulness,
          answer_relevancy,
          context_precision,
          context_recall,
        ],
     )
     ```
  
  4. 결과 확인

     ```python
     df = result.to_pandas()
     df
     ```
