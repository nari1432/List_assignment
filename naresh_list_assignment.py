 

#remove duplicts in list
len = [2,6,7,9,55,4,3,44,90,999]

result=[]
for i in len:
    if i not in result:
        result.append(i)
print(result)

len2 = [25,66,77,88,99,20,33,67,89,98,22]

result=[]
for i in len:
    if i not in result:
       result.append(i)
print(result)

# to find list of elements

len = [11,20,30,40,50]
sum=0
for i in len:
    sum=sum+1
print("sum of list is:",sum)


# To merge two list

len1 = ["naresh","raju","kumar","kalyan"]
len2 = ["ramu","venu","swan","mithn"]
len1.extend(len2)
print(len1)

Empoly = ["cnu","mani","mintu","swty"]
salry = [20,30,40,90,50]
Empoly.extend(salry)
print(Empoly)

# list of multipul integers and into single integers

len = [100,200,300,400]
print("original len:",len)
x = int("".join(map(str,len)))
print("single integer:",x)


len2 = [102,203,305,406]
print("original len2:",len2)
y = int("".join(map(str,len2)))
print("single integer:",y)

# to delete given element from the list

len = [10,20,30,40,50]
del len [1]
print(len)


len1 = [20,30,577,222,333,444,666,99]
del len1 [2]
print(len1)

# to delete element of given index in the list

wrok = ["monday","tuesday","wednesday","thursday","friday"]
wrok.remove("tuesday")
print(wrok)

name = ["venu","tinu","weeky","pard","den"]
name.remove("tinu")
print(name)

# to insert an element at given index location

fruits = ["banana","kiwy","mango","dragon"]
fruits.append("chilli")
print(fruits)
fruits.insert(1,"lemon")
print(fruits) 

fruits1 = ["mango","kiwy","banana"]
fruits1.append("pinappale")
print(fruits1)
fruits1.insert(1,"rino")
print(fruits1)

# to check the size of the given two list are same

x = [22,33,44,55,66,77]
y = [56,44,58,60,77,88]
result = False
for x in len1:
    for y in len2:
        if(x==y):
            result=True
print("len1 have common elements")



# function that takes to list an retun true if they have atleast one common member


list1 = [1,2,3,4,5]
list2 = [5,6,7,8,9]
for i in list1:
    for i in list2:
        if(x==y):
            print("true")

x = [22,33,44,55,66]
y = [11,44,77,55,22]
for x in list2:
    if(x==y):
        print("true")

#to print even and odd numbers separatly in the list

len = [2,1,3,4,5,57,77,54,67,88,]
for i in len:
    if(i%2==0):
        print(i,"is even")
    else:
        print(i,"is odd")

len2 = [11,9,5,0,33,89,388,34,29,]
for i in len2:
    if(i%2==0):
        print(i,"is even")
    else:
        print(i,"is odd")
