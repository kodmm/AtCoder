b = int(input())

a = list(map(int, input().split()))

count = 0

n = len(a)

for i in range(0, n -1):
    for j in range(i+1, n):
        if a[i] == a[j]:
            continue
        else:
            count += 1

print(count)

# numChar = int(input())

# a = list(map(int, input().split()))

# count = len(set(a))
# print(count)