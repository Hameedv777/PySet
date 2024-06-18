print("===Printing the whole set===")
a={3,1,4,5,6,9}
print(a)

print("===Add an element to set===")

a.add(7)
print(a)
print("===Update on set===")

b={15,20,30,45,75}
a.update(b)
print(a)
print("===Remove  on set===")
a.remove(5)
print(a)
a.discard(3)
print("===Discard on set===")
print(a)
print("===Unoin on  set===")
c={9,8,10}
d=a.union(c)
print(d)
print("===Intersection on  set===")
e={4,7,9,10,11,25}
f=a.intersection(e)
print(f)