count = input()

numbers = list(map(int, input().split()))
print(numbers)

#  無限大を代入する
ans = float('inf')
for i in numbers:
    ans = min(ans, len(bin(i)) - bin(i).rfind('1') -1)
print(ans)