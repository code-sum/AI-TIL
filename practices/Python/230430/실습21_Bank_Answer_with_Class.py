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