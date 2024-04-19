N, d, R = map(int,input().split())
if N >= 3:
    print((d + d + R + R )*(N-1) + 16)
else:
    print((d + d + R + R + 16) * (N-1))