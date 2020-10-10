list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

list3 = [i+j for i, j in zip(list1, list2) ]
print(list3)
list4 = []
for i, j in zip(list1,list2):
    result=i+j
    list4.append(result)
print(list4)


aList = [1, 2, 3, 4, 5, 6, 7]
for i in aList:
    square=i**2
    print(square)
bList = [i**2 for i in aList]
print(bList)

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
for i in list1:
    if "" in list1:
        list1.remove("")
print(list1)


#tuple
def swap(x, y):
  return y, x

tuple1 = (11, 22)
tuple2 = (99, 88)
print("Before swapping: ", tuple1,tuple2)
a, b = swap(tuple1, tuple2)
print("After swapping:", a,b)

tuple1 = (11, 22, 33, 44, 55, 66)
tuple2=tuple1[3:-1]
print(tuple2)

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
e=set1.union(set2)
print(e)




student={
    "name": "name1",
    "marks":{
        "LA":"D0",
        "Dlc":"A0"
    }
}
student["marks"]["LA"] = "F"

print(student)

a=[1,2,2,3]
a=set(a)
print(a)



#issubset
a={1,2,3}
b={1,2,3,4}

c=a&b
print(c)
d=a.intersection(a,b)
print(d)
e=a.union(b)
print(e)
f=b.difference(a)
print(f)
l=b-a
print(l)






