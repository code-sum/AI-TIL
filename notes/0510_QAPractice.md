# ✅ [5/10] 실습문제 풀이 (4/24 ~ 5/7)

> 1. [4/28] 미션5. 소수 중 3k-1 꼴인 수
> 2. [4/28] 미션10. 행렬
> 3. [4/30] bank 실습문제
> 4. [5/7] 평균기온 실습문제



## 1. [4/28] 미션5. 소수 중 3k-1 꼴인 수

> n을 입력받고, n 이하의 소수 중 3k-1(k는 1이상의 자연수) 꼴인 수를 포함하는 **리스트**를 만들고 출력하세요. ( **리스트는 작은 수 부터 오름차순으로 정렬되어 있어야 합니다.** )
>
> 예를 들어, n = 10 인 경우 2,5가 리스트에 차례로 들어 있어야 합니다.

```python
'''
소수: 1과 자기 자신만을 약수로 갖는 수
1은 소수가 아님에 유의
'''

import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

n = int(input())
prime_and_3k_1 = []

for i in range(2, n+1):
    if is_prime(i) and (i % 3 == 2):
        prime_and_3k_1.append(i)
    
print(prime_and_3k_1)
```



## 2. [4/28] 미션10. 행렬

> 행렬은 수를 숫자를 네모꼴로 배열해놓은 것입니다.
>
> - 주어진 행렬의 원소 중에서 5를 초과하는 원소를 모두 찾습니다.
> - 이 원소의 위치를 튜플로 만들어서 새 리스트에 추가하세요.
> - 이 리스트를 출력하세요.

```python
# 기본 코드입니다. 수정하지 마세요.
matrix = [[4,7,2,1,0,2],[2,3,5,7,9,5],[2,5,2,3,4,1],[7,5,3,2,1,5],[3,9,2,7,8,10],[0,6,2,3,9,2]] 
#행과 열이 둘 다 6개인 행렬입니다.


# 이제 코딩을 시작하세요!

index_list=[]

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] > 5:
            index_list.append((i, j))

index_list.sort()
print(index_list)
```



## 3. [4/30] bank 실습문제

> `deposit()`, `withdrawal()`, `bank()` 세 함수로 코드가 ATM 역할을 하도록 구현하세요.
>
> 코드는 우선 유저한테 `What do you want to do? deposit(d) or withdrawal(w) or balance check(c)?`를 물어본 후 유저의 입력값을 확인해야 합니다:
>
> - 입력값이 ‘’”이면 return으로 함수를 종료시켜야 합니다.
> - 입력값이 “w”면, 유저한테 얼마를 출금하고 싶은지 물어본 후 출금을 진행해야 합니다.
> - 입력값이 “d”면, 유저한테 얼마를 입금하고 싶은지 물어본 후 입금을 진행해야 합니다.
> - 입력값이 “c”면, 유저한테 잔액을 보여줘야 합니다.

```python
balance = 0

def deposit(money) :
    # Input : (Integer) The amount of money that a user wants to deposit
    # Output : (None) No Output
    
    # Add the money to the current balance
    
    #################
    ### implement ###
    #################
    # Do something on here !
    pass    
    #################

def withdrawal(money) :
    # Input : (Integer) The amount of money that a user wants to withdraw
    # Output : (None) No Output
    
    # Withdraw the money from the current balance

    #################
    ### implement ###
    #################
    # Do something on here !
    pass
    #################


def bank() :
    # Input : (None) No Input
    # Output : (None) No Output
    
    while True:
        process = input("Deposit(d) or withdrawal(w) or balance check(c)? ")
        
        # If a user's input is empty string (''), then quit this function.
        # If a user's input is 'd', then ask the amount of money to deposit and deposit it.
        # If a user's input is 'w', then ask the amount of money to withdraw and withdraw it.
        # If a user's input is 'c', then check the current balance.

        #################
        ### implement ###
        #################
        # Do something on here !
        pass
        #################

bank()
```

```python
# 답안코드

balance = 0

def deposit(bal, money):
    return bal + money

def withdrawal(bal, money):
    if bal >= money:
        return bal - money
    # bal이 충분하지 않을 경우, None이 반환됨

def bank(balance):

    while True:
        process = input("What do you want to do? deposit (d), withdraw (w), check balance (c)")
        if process == "d":
            money_to_deposit = int(input("How much to deposit?"))
            # 문자열의 메서드 중에 isdigit() -> 특정 문자가 숫자인지 판별
            balance = deposit(balance, money_to_deposit)
        elif process == "w":
            money_to_withdraw = int(input("How much to withdraw?"))
            okay = withdrawal(balance, money_to_withdraw)
            #if okay: # okay가 0이면 제대로 작동 안함 !!! 왜냐하면 0을 python이 False로 해석해서 else 쪽으로 빠짐
            #    balance = okay
            #else: # None
            #    print("Not enough money")
            if okay == None:
                print("Not enough money")
            else:
                balance = okay
        elif process == "c":
            print("Your balance is: ", balance)
        elif process == "":
            return
        else:
            print("Allowed commands are d, w, c, or ''.")


bank(balance)
```

```python
# 답안코드 (Class version)

class Bank_Account:
    def __init__(self):
        self.balance = 0
        print("Hello!!! Welcome to the Deposit & Withdrawal Machine")

    def deposit(self):
        amount = float(input("Enter amount to be deposited: "))
        self.balance += amount
        print("\nAmount Deposited:", amount)

    def withdraw(self):
        amount = float(input("Enter amount to be withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\nYou Withdrew:", amount)
        else:

            print("\nInsufficient balance")

    def display(self):
        print("\nNet Available Balance=", self.balance)


def main():
    account = Bank_Account() # 인스턴스 만들기 --> 즉, init도 호출됨 --> 즉, self.balance도 0이 됨
    while True:
        action = input("What do you want to do? deposit(d) or withdrawal(w) or balance check(c)? ")
        if action == "":
            return
        elif action == "d":
            # input으로 여기서 입력 받고,
            # 받은 내용을 deposit() 함수에 인자로 줄 수도 있음
            account.deposit()
        elif action == "w":
            account.withdraw()
        elif action == "c":
            account.display()
        else:
            print("Invalid action")

main()
```



## 4. [5/7] 평균기온 실습문제

> 영국의 월별 기온 데이터가 1723년부터 1970년까지 주어져있습니다.
>
> 
>
> 1. 데이터를 읽어와 각 연도의 겨울 평균 기온과 여름 평균 기온을 출력하세요
>
> - 겨울 평균 = ( 1월 + 2월 ) / 2
> - 여름 = ( 7월 + 8월 ) / 2
> - 문자열 서식화를 통해 각 연도의 연평균 기온, 겨울 평균 기온, 겨울 평균 기온을 출력하세요
>
> (%, f-string, 또는 .format 메서드로 테이블화해보세요)
>
>  
>
> 2. 읽어온 정보를 다른 확장자의 파일로 저장해보세요
>
> - 파일명 `tpmon.csv`.
> - 연도와 12개 월별 평균 기온이 한 줄에 포함되도록 하세요
> - CSV 형식으로 작성하세요 (i.e. 각 데이터를 쉼표로 구분하세요).
> - 파일을 다운받아 내용물을 확인하세요 `elice_utils.send_file('tpmon.csv')`
> - 받은 파일을 엑셀로 열어보세요

```python
with open("tpmon.txt", "r") as temp_data:
    x = []
    lines = temp_data.readlines()[1:] # readlines() --> 각 줄을 원소로 가지는 리스트가 반환
    for line in lines: # 한 줄씩 보기
        new_line = line.strip().split() # 각 줄에서 양 끝 공백을 잘라내고, 띄어쓰기 기준으로 자릅니다
        x.append(new_line) # 각 줄을 띄어쓰기로 자르고, 그 결과물을 x에 넣기




    with open("tpmon.csv", "w") as write_csv:
        for i, year_info in enumerate(x): # year_info는 각 연도의 월별 기온이 원소로 들어있는 리스트


            current_year = 1723 + i
            print("{}:\t {:.1f} / {:.1f}".format(current_year, (float(year_info[0])+float(year_info[1]))/2, (float(year_info[6])+float(year_info[7]))/2))

            write_csv.write(f"{', '.join(year_info)}, {current_year}") # 한 줄 쓰기
            write_csv.write("\n")

```

