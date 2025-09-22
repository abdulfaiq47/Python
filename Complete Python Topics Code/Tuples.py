# Tuple

T = 1,2,3,4,5,6,7,8,9,0
print(T)

type(T)

T[1:4:2]
print(T)

T2 =["Apple","Banana","cherry","cherry"]
print(T2)

a, b, c, d = T2
#a, b, c, *d = T #here '*' is starik

print(a)
print(b)
print(c)

print(T2.count("Apple"))
print(T2.count("Banana"))
print(T2.count("cherry"))


print(T2.index("Banana"))
