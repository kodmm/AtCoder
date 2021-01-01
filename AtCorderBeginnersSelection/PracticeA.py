a = int(input())
b, c = map(int, input().split())
s = str(input())
# strip(): 前後の文字を削除, lstrip(): 前の文字を削除, rstrip(): 後の文字を削除

print(a + b + c, s)


#* answer
# 整数の入力
a = int(input())
# スペース区切りの整数の入力
b, c = map(int, input().split())
# 文字列の入力
s = input()
#出力
print("{} {}".format(a+b+c, s))