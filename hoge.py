a, b = map(str, input().split())
a = list(a)
b = list(b)
s1, s2 = 0, 0
s1 = [int(i) for i in a]
s2 = [int(i) for i in b]
s1 = sum(s1)
s2 = sum(s2)
if(s1 > s2):
    print("{}".format(s1))
else:
    print("{}".format(s2))