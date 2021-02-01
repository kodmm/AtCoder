a, b, c = map(int, input().split())

def attack(first, second):

    while first[0] != 0 and second[0] != 0:
            first[0] -=1
            if first[0] == 0:
                print(second[1]) 
                break
            second[0] -=1
            if second[0] == 0:
                print(first[1]) 
                break

while True:
    if 0 <= a and b <= 100 and 0 <= c <= 1: 
        attack([a, 'Takahashi'],[b, 'Aoki']) if c == 0 else attack([b, 'Aoki'], [a, 'Takahashi'])
        break
    else:
        a, b, c = map(int, input('one more').split())

    

# Answer

A, B, C = map(int, input().split())
if A + B + C > B:
    print("Takahashi")
else:
    print("Aoki")
