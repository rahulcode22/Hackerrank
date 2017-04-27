n,k,q = list(map(int,input().split()))
nums = list(map(int,input().split()))
for _ in range(q):
    print(nums[(int(input())+n-k)%n])
