Y, X, D = input().split()
d = input()

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
direction = { "N": 0, "E": 1, "S": 2, "W": 3}

a = (direction[D] + 1) % 4 if (d == "R") else (direction[D] - 1) % 4

def test(a, Y, X):
  Y += dy[a]
  X += dx[a]
  print("Y: {}, X: {}".format(Y, X))

test(a, int(Y), int(X))
