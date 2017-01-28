n =raw_input()
s = set(map(int, raw_input().split())) 
for i in range(int(raw_input())):
    choice=raw_input().split()
    if choice[0]=="pop" :
        s.pop()
    elif choice[0]=="remove" :
        s.remove(int(choice[1]))
    elif choice[0]=="discard" :
        s.discard(int(choice[1]))
print sum(s)
    
