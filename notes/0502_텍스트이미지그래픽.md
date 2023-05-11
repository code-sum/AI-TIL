# ✅ [5/2] 사전형, 집합, 텍스트, 이미지, 그래픽



#### 미션1. 은닉 흑백 사진의 검은 pixel 수

> mona_lisa.png 파일에 이미지 프로세싱 수업 자료에 나와 있는 알고리즘대로 흑백 사진이 은닉되어 있습니다.
>
> 은닉되어 있는 흑백사진의 검은색 픽셀의 수는 총 몇 개 일까요?
>
> mona_lisa.png 파일에서 어떤 조건에 있는 pixel이 은닉된 검은 픽셀인지 생각해봅시다.

```python
from cs1media import *

# black_pixel의 수를 return하는 decode_black_pixel 함수를 구현해 봅시다.
def decode_black_pixel(img):
    num = 0
    w, h = img.size()
    for y in range(h):
        for x in range(w):
            r, g, b = img.get(x, y)
            if r % 2 == 1: 
                num += 1
    return num
  
# mona_lisa 파일을 불러옵니다.
img = load_picture("mona_lisa.png")
# decode_black_pixel 함수를 호출합니다.
result = decode_black_pixel(img)
# 결과를 출력합니다.
print (result)
```

