# ３文字の整数の入力
s = str(input())
print(s)
# listにする
list_s = list(s)

# integer型のlistにする
list_s = [int(i) for i in list_s]
# list_sの値が`1`が格納されている個数を求める
result = list_s.count(1)

print("{}".format(result))



"""解答

print(input().count('1'))
"""