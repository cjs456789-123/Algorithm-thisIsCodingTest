N, M = 2, 15
array = [2,3]

d = [10001] * (M+1)

d[0] = 0
for i in range(N):
    for j in range(array[i], M+1):
        if d[j - array[i]] != 10001:
            d[j] = min(d[j], d[j - array[i]] + 1)

if d[M] == 10001:
    print(-1)
else:
    print(d[M])