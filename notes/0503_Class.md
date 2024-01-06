# ✅ [5/3] 텍스트, 이미지, 그래픽, 클래스





#### 미션2. 계좌 정보 관리하기

> 당신은 은행의 전산업무를 위해서 각 고객에 대한 정보를 클래스와 객체를 이용해 관리하려고 합니다.
>
> 주어진 코드를 수정해서 좀 더 효율적으로 거래를 할 수 있는 은행을 만들어봅시다.
>
> ```
> John, 10000, Jenny, 2000, 5000
> ```
>
>  위와 같은 입력을 받아서 문자열을 파싱해 이에 해당하는 `Account` 객체를 생성합시다. 위 예시에서 생성되는 첫 번째 `Account` 객체는`name`은 John이고, `amount`는 10000입니다. 두번째 객체도 같은 방식으로 `name`은 Jenny이고, `amount`는 2000입니다.
>
> 입력의 마지막 문자열에 해당하는 숫자, 이 예시에는 5000원을 그 객체의 `remit`함수를 이용해 첫 번째 객체에서 두 번째 객체로 송금해주세요.
>
> 송금이 완료되면, 두 번째 객체의 잔고를 출력하세요. 자기가 가진 돈보다 많은 돈을 보내려고 할 때에는 송금하지 말고 `불가능, (부족한 금액)원`이라고 출력하세요.

```python
class Account():
    def __init__(self, name, amount): # 고객의 정보를 받는 생성자를 구현하세요.
        self.name = name # 계좌 주인의 이름입니다.
        self.amount = amount # 계좌의 잔고입니다.
    
    def remit(self, receiver_account, amount_money):
        # receiver_account는 Account 객체입니다.
        # amount_money은 int형의 숫자입니다.
        if self.amount >= amount_money:
            self.amount -= amount_money
            receiver_account.amount += amount_money
            return True
        else:
            print(f"불가능, {amount_money - self.amount}원")
            return False
    
    def printmoney(self):
        # 가진 돈을 print()하고, 현재 self.amount를 return합니다.
        print(self.amount)
        return self.amount


def parse_accounts(input_str):
    accounts = []
    input_list = input_str.split(', ')

    for i in range(0, len(input_list) - 1, 2):
        name = input_list[i]
        amount = int(input_list[i + 1])
        account = Account(name, amount)
        accounts.append(account)

    remittance = int(input_list[-1])  # 마지막 숫자를 송금액으로 저장
    return accounts, remittance

    
val = input()
accounts, remittance = parse_accounts(val)

sender = accounts[0]
recipient = accounts[1]

if sender.remit(recipient, remittance):
    recipient.printmoney()
```



#### 미션3. 이자 계산

> ```python
> John, 10000, 8
> ```
>
> 위와 같은 입력을 받아서 문자열을 파싱해 이에 해당하는 `Account` 객체를 생성합시다. 위 예시에서 생성되는 `Account` 객체는`name`은 John이 되겠죠.
>
> 두 번째 입력에 해당하는 숫자, 이 예시에는 10000원은 이자 지급 전 계좌에 남아 있는 금액을 의미합니다.
>
> 마지막 입력에 해당하는 숫자, 이 예시에는 8%는 이율의 의미합니다. 즉, 8%의 이율로 이자를 지급하는 것을 의미합니다.
>
> 종합해보면 John의 계좌에 남아 있는 10000원은 8%의 이율로 이자를 지급받게 됩니다.
>
> 출력 예시: 
>
> ```python
> John 10800
> ```

```python
class Account():
    def __init__(self, name, balance): # 고객의 정보를 받는 생성자를 구현하세요.
        self.name = name # 계좌 주인의 이름입니다.
        self.balance = balance # 계좌의 잔액입니다.
    
    def accrue(self, ratio):
        # ratio는 이율입니다.
        self.balance += self.balance * ratio
    
    def printmoney(self):
        # 계좌의 주인과 가진 돈을 print() 합니다.
        print(self.name, int(self.balance))

val = input()
#########

# 입력을 parsing하여 실제로 이자를 지급해 봅시다.
val_input = val.split(', ')
name = val_input[0]
balance = int(val_input[1])
interest_rate = float(val_input[2]) / 100

# printmoney를 사용해서 출력해주세요.
account = Account(name, balance)
account.accrue(interest_rate)
account.printmoney()
```

