# Exercise 1: Basic Set Operations
a= {1,2,3,"hello",8.8}
print(a)
a.add(456)
print(a)
a.remove(1)
print(a)
a.discard(456)
print(a)

# Exercise 2: Clear All Elements

a= {1,2,3,"hello",8.8}
a.clear()
print(a)


# Exercise 3: Find the Length of a Set
a= {1,2,3,"hello",8.8}
print(len(a))
# Exercise 4: Check if a Set is Empty

a= {1,2,3,"hello",8.8}
if (len(a)==0):
    print("empty")
else:
    print("not")

# Exercise 5: Union of Sets
a= {1,2,3,"hello",8.8}
b= {7,5,6}
c = a | b
print(c)

# Exercise 6: Intersection of Sets
a= {1,2,3,"hello",8.8}
b= {7,5,6}
c = a&b
print(c)

# Exercise 7: Difference of Sets
a= {1,2,3,"hello",8.8}
b= {7,5,6}
c = a-b
print(c)

# Exercise 8: Symmetric Difference

set1= {1,2,3}
set2= {1,2,3,7,9}
set3= set1.symmetric_difference(set2)
print(set3)

# Exercise 9: Find Max and Min
a= {1,2,3}
bc = min(a)
print(bc)

cd = max(a)
print(cd)

# Exercise 10: Sum of Set Elements
sum_set ={1,2.3,4,5}
print(sum(sum_set))
