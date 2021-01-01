# 整数の入力
a, b = map(int, input().split())
# a * b 
result = a * b

if(result % 2 == 0):
    print("Even")
else:
    print("Odd")

