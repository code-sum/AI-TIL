n1 = int(input())
list1 = []

for i in range(n1):
    list1.append(int(input()))

n2 = int(input())
list2 = []

for i in range(n2):
    list2.append(int(input()))
    
# 두 list를 중복없는 리스트 result_list로 합친 후, 오름차순 정렬하여 출력하세요.
result_list = list(set(list1 + list2))
result_list.sort()

print(result_list)