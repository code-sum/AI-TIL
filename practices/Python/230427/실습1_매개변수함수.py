name = input("What is your name? ")
print("Welcome to CS101, " + name)

raw_n = input("Enter a positive integer> ")
n = int(raw_n)
for i in range(n):
  print( "*" * i)