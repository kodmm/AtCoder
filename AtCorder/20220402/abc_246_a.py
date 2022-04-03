xy = [input().split() for _ in range(3)]

a = []
b = []
x = ""
y = ""
for value in xy:
    a.append(value[0])
    b.append(value[1])

for value in a:
    if a.count(value) == 1:
        x = value
        break

for value in b:
    if b.count(value) == 1:
        y = value
        break

print("{} {}".format(x, y))