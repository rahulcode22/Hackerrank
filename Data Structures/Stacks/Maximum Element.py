st = []
maxi = 0

for i in range(int(input())):
    k = input().split()
    if k[0] == '1':
        st.append(int(k[1]))
        maxi = max(maxi, int(k[1]))
    elif k[0] == '2':
        k = st.pop()
        if k == maxi:
            maxi = max(st + [0])
    else:
        print(maxi)
