stu, marks = int(input()), input().split().index("MARKS")
print (sum([int(input().split()[marks]) for _ in range(stu)]) / stu)
