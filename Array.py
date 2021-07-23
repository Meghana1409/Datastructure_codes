a=[1,2,3,4,9]
#access value
print("access value",a[1])
print()

# insert values
a.append(3)
print(a)
print()
a.insert(2,9)
print(a)
print()
# finds value
f=9
for i in range(len(a)):
    if a[i]==f:
        print('found at position',i)
        
# traverse array
print(a)
for i in a:
    print(i)

b=['a','b']
print(":".join(b))

# concat lists
print(a+b)

# copy
a1=a.copy()
print(a1)

print("sort Array...")
g=[5,2,9,7]
g.sort()
print("sort method..",g)
print("sorted function..",sorted([8,5,2,0]))

print("count()")
n=[0,0,6,7,5,4,4,4]
print(n.count(4))
print(n.count(5))
# delete
a.remove(9)
print("remove method..",a)
print(a.pop())
print("pop method..",a)
g.clear()
print("Clear method..",g)


##output:
"""

access value 2

[1, 2, 3, 4, 9, 3]

[1, 2, 9, 3, 4, 9, 3]

found at position 2
found at position 5
[1, 2, 9, 3, 4, 9, 3]
1
2
9
3
4
9
3
a:b
[1, 2, 9, 3, 4, 9, 3, 'a', 'b']
[1, 2, 9, 3, 4, 9, 3]
sort Array...
sort method.. [2, 5, 7, 9]
sorted function.. [0, 2, 5, 8]
count()
3
1
remove method.. [1, 2, 3, 4, 9, 3]
3
pop method.. [1, 2, 3, 4, 9]
Clear method.. []
"""