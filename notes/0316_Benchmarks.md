# ✅ LangChain Benchmarks
> _"벤치마크(Benchmark). 생성형 인공지능(AI)이나 거대언어모델(LLM)과 관련한 정보를 접하다 보면 심심치 않게 등장하는 단어다. 주로 토목공학에서 쓰이던 기준점, 표준점이라는 의미가 정보기술(IT) 영역으로 넘어와서는 디바이스의 연산 능력을 평가하는 기준으로 사용돼 왔다. 생성형 인공지능(AI) 분야에서는 LLM의 성능을 평가하는 기준 데이터셋을 의미한다. 벤치마크 점수라고 하면 특정 LLM이 벤치마크 데이터셋을 얼마나 정답에 가깝게 산출해내는 지를 평가한 수치다."_ [(link)](https://www.sedaily.com/NewsView/29VSXCSWOD)


- Running Locally [(link)](https://langchain-ai.github.io/langchain-benchmarks/notebooks/run_without_langsmith.html)
  - LangChain Benchmarks 는 기본적으로 LangSmith 를 활용하게 되어 있지만, 아래 코드를 통해 LangSmith 계정 없이도 로컬 환경에서 결과를 확인할 수 있음
    ```python
    # Prove that we can run without LangSmith
    import os
    
    _ = [
        os.environ.pop(key)
        for key in list(os.environ.keys())
        if key.startswith("LANGCHAIN_")
    ]
    ```
    ```python
    from langchain_benchmarks import registry

    task = registry["Multiverse Math"]
    task
    ```
    ```python
    # Evaluate
    import uuid

    from langchain_benchmarks.tool_usage import agents, get_eval_config
    from langchain_benchmarks.utils import run_without_langsmith
    
    experiment_uuid = uuid.uuid4().hex[:4]
    
    
    models = ["gpt-3.5-turbo-1106"]
    
    for model in models:
        print()
        eval_config = get_eval_config(output_evaluation="qa_math")
        agent_factory = agents.OpenAIAgentFactory(task, model=model)
        test_run = run_without_langsmith(
            # This will clone the dataset locally if not already there
            path_or_token_id=task.dataset_id,
            llm_or_chain_factory=agent_factory,
            evaluation=eval_config,
            verbose=True,
        )
    ```
    ```python
    # You can interact with the object directly or as a flattened dataframe
    df = test_run.to_dataframe()
    df.head()
    ```
    ```python
    df.to_csv("output.csv", index=False)
    ```

- 참고자료
  - LangChain Benchmarks - Github [(link)](https://github.com/langchain-ai/langchain-benchmarks?tab=readme-ov-file)
  - LangChain Benchmarks - 공식문서 [(link)](https://langchain-ai.github.io/langchain-benchmarks/index.html)
