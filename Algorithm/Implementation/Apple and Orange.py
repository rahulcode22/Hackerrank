s,t = map(int, input().strip().split(' '))
a,b = map(int, input().strip().split(' '))
m,n = map(int, input().strip().split(' '))

house = range(s, t+1)

print(len([(temp + a) for temp in map(int, input().strip().split(' ')) if (temp + a) in house]))

print(len([(temp + b) for temp in map(int, input().strip().split(' ')) if (temp + b) in house]))
