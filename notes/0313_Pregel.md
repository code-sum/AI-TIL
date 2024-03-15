# ✅ Pregel 알고리즘과 LangGraph

![0313_Pregel](https://github.com/code-sum/AI-TIL/assets/106902415/9f75d5b7-4559-40fe-a613-ea5273b99b45)

> [이미지 출처](https://15799.courses.cs.cmu.edu/fall2013/static/papers/p135-malewicz.pdf)



- Pregel 알고리즘이란?
  - 2010년 구글에서 발표한 대규모 그래프 처리 알고리즘 [(link)](https://research.google/pubs/pregel-a-system-for-large-scale-graph-processing/)
  - `superstep` 이라고 불리는 반복 가능한 객체(iterations)가 연속되는 구조임
  - Facebook 이 소셜 네트워크 분석하는데 내부적으로 활용하고 있는 [Apache Giraph](https://github.com/apache/giraph)에 영향을 줌



- Pregel 알고리즘과 LangGraph
  - LangGraph 는 LLM 어플리케이션에 주기(cycle)를 추가하는 용도로 개발되었으며, 이는 DAG 알고리즘과 다름
    - 주기는 순환고리 내에서 LLM 을 호출하여 다음 단계에 어떤 동작을 할 것인지 물어보는 식으로 Agent 와 유사한 동작(agent-like behaviors)을 구현하는데 필요함
    - 단순히 DAG 알고리즘으로 서비스를 구현하고 싶다면, LangChain LCEL 문법을 쓰면 됨
  - LangGraph 는 Pregel 과 [Apache Beam](https://beam.apache.org/) 의 영향을 받음
    - `StateGraph.compile()` 처럼, 설계된 Graph 를 컴파일할 때 쓰는 `.compile()` 매서드가 LangGraph 패키지 내 `Pregel` 클래스를 상속받아 구현되어 있음
   
      
      ```python

      from langgraph.pregel import Channel, Pregel
      
      class CompiledGraph(Pregel):
          graph: Graph
      
          def get_graph ...
      ```

    - `Pregel` 클래스는 `get_state`, `update_state`, `invoke`, `stream`, `transform` 등의 메서드가 구현되어 Graph 의 State 를 관리하고, 리턴값의 형태를 결정함


- 용어
  - DAG : 방향 비순환 그래프(Directed Acyclic Graph)



- 참고자료
  - [Research Paper] [Pregel: A System for Large-Scale Graph Processing (2010)](https://15799.courses.cs.cmu.edu/fall2013/static/papers/p135-malewicz.pdf)
  - [Medium Post] [A quick introduction to Google’s Pregel graph processing system](https://medium.com/@AdityaChatterjee/googles-pregel-graph-processing-system-90341156848a)

