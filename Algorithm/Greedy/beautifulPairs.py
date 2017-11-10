n = int(raw_input())
arrA = map(int,raw_input().split())
arrB = map(int,raw_input().split())
ans = 0
for i in range(n):
    for j in range(len(arrB)):
        if arrA[i] == arrB[j]:
            arrB.pop(j)
            ans += 1
            break
if ans == n:
    ans -= 1
else:
    ans += 1

print ans
