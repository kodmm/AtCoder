import sys
h, w, y, x, m = map(str, input().split())
s_i = [list(input()) for _ in range(int(h))]

direction = {"N": 0, "E": 1, "S": 2, "W": 3}

dx = (0, 1, 0, -1)
dy = (-1, 0, 1, 0)

x, y = map(int, [x, y])

x += dx[direction[m]]
y += dy[direction[m]]

print(x, y)

try:
    if (x < 0 or y < 0 or s_i[y][x] == "#"):
        print("No")
        sys.exit()
    next_i = s_i[y][x]
except IndexError:
    print("No")
    sys.exit()
else:
    print("Yes")