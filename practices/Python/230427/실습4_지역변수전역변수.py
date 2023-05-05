a = "Letter a"

def f(a):
  print("A = ", a)
  
def g():
  a = 7
  f(a + 1)
  print("A = ", a)
  
print("A = ", a)
f(3.14)
print("A = ", a)
g()
print("A = ", a)


'''
출력값
A = Letter a
A = 3.14
A = Letter a
A = 8
A = 7
A = Letter a
'''