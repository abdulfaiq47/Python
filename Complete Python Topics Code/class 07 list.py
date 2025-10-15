# Assigment 03
scores=[23,56,65,93]
s=[]

for score in scores:
    if scores not in s:
        s.append(score)

print(s)
#sort accending orders

s.sort()

print(f"1st highest number in list is : {s[-1]}")
print(f"2nd highest number in list is : {s[-2]}")
