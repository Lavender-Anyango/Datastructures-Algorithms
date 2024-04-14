

shapes = ()
shapes = ("circle", "rectangle", "circle")

print(shapes)
print(shapes[1])
print("length:", len(shapes))
if "circle" in shapes:
    print("circle is in shapes")

if "apple" not in shapes:
    print("apple is not in shapes")

mixed = ("string", False, 2, 5.6)

# upack
names = ("Jim", "Dwight", "Pam")
person1, person2, person3 = names 
print("person1:", person1)
print("person2:", person2)
print("person3:", person3)


#upack in a list
numbers = (1,2,3,4,5)
n1, n2, *rest = numbers
print("n1:", n1)
print("n2:", n2)
print("rest:", rest)


# creating functions which return
def function():
    return 1,2,3

#results
(v1,v2,v3) = function()
print("v1:", v1)
print("v2:", v2)
print("v3:", v3)


# concatenate 
first = (1,2)
second = (3,4)
joined = first + second 
print("joined:", joined)

multi = first * 3
print("multi:", multi)


# count the occurrences of a value
print("one count:", multi.count(1))

# working with tuples and lists
values = [20, 30, 40, 50]
temp_list = list(values)
values = tuple(temp_list)
print(values)
letters = ("a", "b", "c", "d", "e", "f")
print(letters[1:4])

del letters 

simple_tuple = ([1], 2, 3)
simple_tuple[0].append(55)
print(simple_tuple)