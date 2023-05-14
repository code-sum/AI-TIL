# ✅ [4/30] ClassA_Practice

> 실습21. Bank
>
> - Functional Programming, OOP 두 가지 버전으로 코드 작성



#### 실습21. Bank

> `deposit()`, `withdrawal()`, `bank()` 세 함수로 코드가 ATM 역할을 하도록 구현하세요.
>
> 코드는 우선 유저한테 `What do you want to do? deposit(d) or withdrawal(w) or balance check(c)?`를 물어본 후 유저의 입력값을 확인해야 합니다:
>
> - 입력값이 ‘’”이면 return으로 함수를 종료시켜야 합니다.
> - 입력값이 “w”면, 유저한테 얼마를 출금하고 싶은지 물어본 후 출금을 진행해야 합니다.
> - 입력값이 “d”면, 유저한테 얼마를 입금하고 싶은지 물어본 후 입금을 진행해야 합니다.
> - 입력값이 “c”면, 유저한테 잔액을 보여줘야 합니다.

```python
# 출제코드

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

