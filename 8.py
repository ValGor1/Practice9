x = int(input())
def count(x):
    count = 0
    for a in range(1, x):
        b = (x - a * a) // 2
        if a * a + b * b == x:
            count += 1

    return count
print(count(x))