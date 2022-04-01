x, y, n = map(int, input().split())
nlist = list([input() for _ in range(n)])
# print("x: {}, y: {}, n: {}. nlist:{}".format(x, y, n, nlist))

direction = {"N": 0, "E": 1, "S": 2, "W": 3}

dx = (0, 1, 0, -1)
dy = (-1, 0, 1, 0)

currentDir = direction["N"]

for value in nlist:
    currentDir = (currentDir + 1) % 4 if value == "R" else (currentDir -1) % 4
    x += dx[currentDir]
    y += dy[currentDir]
    print("{} {}".format(x, y))


