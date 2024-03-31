
N = int(input())
op = input()
e = input() 
i=  input()
list=[]
##print(input("insert") + input(e) + input(i))
if(op=="insert"):
    print(list.insert(e,i))
elif(op == "delete"):
    print(list.remove(e,i))
elif(op == "append"):
    print(list.append(e,i))
elif(op == "sort"):
    print(list.sort())
elif(op == "reverse"):
    print(list.reverse())
elif(op == "pop"):
    print(list.pop())
elif(op == "print"):
    print(list)
else:
    print("error")

