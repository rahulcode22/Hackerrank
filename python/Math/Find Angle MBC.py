import math 
AB = int(raw_input())
BC = int(raw_input())
a= math.degrees(math.atan2(AB,BC))
print str(int(round(a)))+'°'
