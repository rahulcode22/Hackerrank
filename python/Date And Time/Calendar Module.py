import calendar
m, d, y = map(int, raw_input().split()) 
print(list(calendar.day_name)[calendar.weekday(y, m, d)].upper())
