x, y, n = map(int, input().split())

dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)
# direction = {'E': 0, 'S': 1, 'W': 2, 'N': 3}

now_direction = 0
count = 0
max_count = 1
first = True

# 11223344

def move(direction, x, y):
    x += dx[direction]
    y += dy[direction]
    return x, y

for _ in range(n):
    direction = now_direction % 4

    (x, y) = move(direction, x, y)
    count += 1
    if first and count == max_count:
        first = False
        count = 0
        now_direction += 1
    elif count == max_count:
        first = True
        max_count += 1
        count = 0
        now_direction += 1
print(x, y)