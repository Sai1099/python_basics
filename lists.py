
color = ["blue","orange","metal","nf","wswed"]
print(color[0:3])
color[1] = "Apple"
print(color[1])
fuckers = ["lokesh","pradeep","hari","sony"]
disorder = [1,3,4,6]
fuckers.extend(disorder)
print(fuckers)
##Remove() is used to delete the element in the list doesn't support the index value
fuckers.remove("lokesh")
print(fuckers)
fuckers.append("varun")
print(fuckers)
fuckers.reverse()
print(fuckers)
##pop is used to delete the string or int using the index value 
fuckers.pop(2)
print(fuckers)

BCD = "aeiou"
run = list(BCD)
print(run)
print(list(run))
##for getting combine numbers in lists
y =list(set(list1).intersection(list4))

##to insert element we have to do insert(position,element)
lizt=[1,3,5,689,86]
lizt.insert(2,67)
print(lizt)
