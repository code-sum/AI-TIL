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