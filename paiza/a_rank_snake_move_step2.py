y, x, count = map(int, input().split())
destinations = list(map(str, [input() for _ in range(count)]))
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
direction = {"N": 0, "E": 1, "S": 2, "W": 3}

for idx, dir in enumerate(destinations):
    x += dx[direction[dir]]
    y += dy[direction[dir]]
    print("{} {}".format(y, x))