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