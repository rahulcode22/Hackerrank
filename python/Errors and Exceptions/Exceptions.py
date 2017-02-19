t=int(raw_input())
for i in range(t):
    a,b=raw_input().split()
    
    try:
        print int(a)/int(b)
    except (ZeroDivisionError,ValueError) as e:
            print "Error Code:",e
