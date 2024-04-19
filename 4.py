Checker = True
counter = 0
while Checker == True:
    N = int(input())
    if N == 0:
        Checker = False
        break
    elif N%4 ==0:
        counter +=1

print(counter)
