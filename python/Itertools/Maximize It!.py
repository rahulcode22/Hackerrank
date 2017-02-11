# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools

k, m = map(int, raw_input().split())
lists_of_ints = [map(int, raw_input().split())[1:] for i in range(k)]

S_max = []

for product in itertools.product(*lists_of_ints):
	S_max.append(sum(map(lambda i: i**2, product))%m)

print max(S_max)


    
