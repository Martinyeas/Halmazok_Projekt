file = open("./11.14/file2.txt","w")

#add
fruits = {"apple", "banana", "cherry"}

fruits.add("orange")

fruits = str(fruits)+" \n"
file.write(fruits)

#clear
fruits = {"apple", "banana", "cherry"}

fruits.clear()

fruits = str(fruits)+" \n"
file.write(fruits)

#copy
fruits = {"apple", "banana", "cherry"}

x = fruits.copy()

x = str(x)+" \n"
file.write(x)

#differnce
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.difference(y)

z = str(z)+" \n"
file.write(z)

#difference_update
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.difference_update(y)

x = str(x)+" \n"
file.write(x)

#discard
fruits = {"apple", "banana", "cherry"}

fruits.discard("banana")

fruits = str(fruits)+" \n"
file.write(fruits)

#intersection
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

z = str(z)+" \n"
file.write(z)

#intersection_update
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

x = str(x)+" \n"
file.write(x)

#isdisjoint
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}

z = x.isdisjoint(y)

z = str(z)+" \n"
file.write(z)

#issubset
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

z = x.issubset(y)

z = str(z)+" \n"
file.write(z)

#issuperset
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}

z = x.issuperset(y)

z = str(z)+" \n"
file.write(z)

#pop
fruits = {"apple", "banana", "cherry"}

fruits.pop()

fruits = str(fruits)+" \n"
file.write(fruits)

#remove
fruits = {"apple", "banana", "cherry"}

fruits.remove("banana")

fruits = str(fruits)+" \n"
file.write(fruits)

#symmetric_difference
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

z = str(z)+" \n"
file.write(z)

#symmetric_difference_update
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

x = str(x)+" \n"
file.write(x)

#union
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.union(y)

z = str(z)+" \n"
file.write(z)

#update
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.update(y)

x = str(x)+" \n"
file.write(x)

print('kör')
print('futa')