import string
alphabet = list(string.ascii_lowercase)

change_alpha = list(map(int, input().split()))

answer = []
for v in change_alpha:
    answer.append(alphabet[v - 1])
print("".join(answer))