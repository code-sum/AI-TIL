# ✅ [Prompt Engineering] Models | GPT-4

> 참고자료 : [🗂️](https://www.promptingguide.ai/models/gpt-4)



- 배경지식
  - 어떤 모델을, 어떤 용도로 사용하는지에 따라 프롬프트도 달라져야 함



- GPT-4 모델의 문제점
  - (1) hallucination
  - (2) reasoning error



- GPT-4 모델의 문제점 해결하기
  - (1) 정확도를 개선하기 위해 GPT-4 모델과 외부 지식을 결합 (=RAG)
  - (2) 프롬프트 엔지니어링 테크닉을 활용하여 결과를 개선
    - GPT-4 모델에게 한꺼번에 너무 많은 부담 주지 않기 (=to avoid high-stakes use)
      - ① 질문 마지막에 “Think step-by-step.” 문장 덧붙이기
      - ② 모델 조종하는(=steer) System Message 세팅해서 아래와 같이 명령하기
        - “You can think step-by-step and respond with ‘I don’t know the answer’ If you are not sure about the answer.”



- GPT-4 모델의 문제점 해결하기 :: 적용사례

  1. 문제상황 : “Elvis Presley” 가 정답이지만, 잘못된 답변 표출 ⬇️

     ![gpt4-6](https://github.com/code-sum/AI-TIL/assets/106902415/48a0747a-4b1c-46dd-856c-740ee5fa4d27)

  2. 해결방법 ① : 질문 마지막에 “Think step-by-step.” 문장 덧붙이기 ⬇️

     ![gpt4-7](https://github.com/code-sum/AI-TIL/assets/106902415/0726aeb8-aa06-4a8a-ad0d-eaa8020ce286)

  3. 해결방법 ② : System Message 세팅해서 think step-by-step 명령하기 ⬇️

     ![gpt4-8](https://github.com/code-sum/AI-TIL/assets/106902415/fbad83ce-312e-4c56-87f9-678d1e88a217)