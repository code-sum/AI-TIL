def color_complementary(r, g, b):
# 보색 변환 함수를 구현해 보세요.
    comp_r = 255 - r
    comp_g = 255 - g
    comp_b = 255 - b

    # 보색 값을 반환합니다.
    return comp_r, comp_g, comp_b

# 사용자에게 input을 사용하여 3개의 값을 받습니다. (각각 r,g,b)를 나타내는 수치들 입니다.
r = int(input(""))
g = int(input(""))
b = int(input(""))

# color_complementary(r,g,b) 함수를 호출하여 보색변환 이후의 r,g,b값을 comma로 구분된 괄호의 형태로 출력합니다.
comp_r, comp_g, comp_b = color_complementary(r, g, b)
print('(',comp_r,',',comp_g,',',comp_b,')')