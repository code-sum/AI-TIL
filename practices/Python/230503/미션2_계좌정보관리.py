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