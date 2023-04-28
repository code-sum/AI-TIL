def my_power(a,b):
    result = a
    for i in range(1, b):
        result *= a
    return result

# my_power을 사용하는 code입니다. 수정하지 마십시오.
x = int(input())
y = int(input())
print(my_power(x,y))