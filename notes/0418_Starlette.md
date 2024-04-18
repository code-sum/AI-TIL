# ✅ [Streaming] 추천 패키지 목록



- `StreamingResponse` 와 `EventSourceResponse` 의 차이점

  - response body 를 기록하는 소스코드는 `StreamingResponse(generate())` 를 리턴하도록 구현되어 있지만

  - Streaming 기능이 구현된 소스코드는 `EventSourceResponse(_stream_log())`를 리턴하도록 구현되어 있어서 차이점 확인
  - 공통점 : 둘 다 `starlette` 패키지에서 `Response` 클래스를 상속 받아서 구현

1. `StreamingResponse`

   - 모듈 import 방식 : `from starlette.responses import StreamingResponse`

   - 비동기적으로 큰 파일이나 데이터를 스트리밍할 때 사용되며, Starlette에서 기본적인 스트리밍을 구현할 때 활용

   - Starlette에서는 일반적인 비동기 스트리밍을 위해 `StreamingResponse` 사용


2. `EventSourceResponse`
   - 모듈 import 방식 : `from sse_starlette import EventSourceResponse`
   
   - sse_starlette 패키지는 SSE 구현에 최적화
   



- **Starlette** vs. **sse_starlette** 패키지 비교

  1. Starlette

     - Starlette는 경량 웹 프레임워크로, 빠르고 간편하게 웹 서비스를 만들 수 있도록 설계되었습니다.

     - ASGI(Asynchronous Server Gateway Interface)를 지원하며, 비동기 웹 어플리케이션을 작성하기에 적합합니다.

     - 요청과 응답을 다루는데 필요한 핵심 기능을 제공하며, 라우팅, 미들웨어, 응답 생성 등의 기능을 포함하고 있습니다.

     - 기본적인 HTTP 요청과 응답 처리를 위한 라이브러리이며, REST API, 웹소켓 서버, 마이크로서비스 등을 구축하기에 좋습니다.

  2. sse_starlette

     - sse_starlette는 Starlette를 확장하여 Server-Sent Events (SSE)를 지원하도록 만든 패키지입니다.

     - SSE는 서버에서 클라이언트로 실시간으로 데이터를 보내는 단방향 통신을 위한 프로토콜입니다.

     - sse_starlette는 SSE를 쉽게 구현할 수 있도록 도와주는 도구들을 제공합니다.

     - Starlette의 미들웨어를 사용하여 SSE를 구현하고, SSE 라우트 핸들러를 쉽게 작성할 수 있도록 해줍니다.

     - 이를 통해 웹 애플리케이션에서 실시간으로 데이터를 전송하고 업데이트하는 기능을 구현할 수 있습니다.

  3. 종합

     - 요약하자면, Starlette는 경량 웹 프레임워크이며, sse_starlette는 Starlette를 확장하여 SSE를 쉽게 구현할 수 있도록 도와주는 패키지입니다. 만약 실시간으로 데이터를 업데이트하고 클라이언트에게 전송해야 하는 기능이 필요하다면 sse_starlette를 사용하는 것이 좋습니다.
     - SSE를 구현하기 위한 응답 클래스로, sse_starlette에서 사용. 클라이언트에게 실시간 이벤트를 전송하고, 자동 재연결 등의 기능을 제공
     - SSE 를 구현하려면 sse_starlette의 `EventSourceResponse`를 사용
     - 해당 클래스 각주에 **“implementation based on Starlette StreamingResponse”** 라고 작성되어 있음!

