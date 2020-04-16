def f1(l1):
    temp=[]
    for i in l1:
        temp.append(i*i)

    return temp
        
    

mylist=[]
size=int(input("Enter the size of the list"))
for i in range(size):
    val=int(input("Enter the element for the list: "))
    mylist.append(val)

newlist=f1(mylist)
print(mylist)   #oldlist
print(newlist)  #newlist
