##firstly we have to define a function
def pradeep():
    print("hello pradeep!")

pradeep()

def sony(a, b):
    c=a+b
    print(c)

sony(1,6)

### the function name should be small
def hari(name,age):
    print("Hi! your name  is  "+ name + " , You are "+ str(age) )

hari("manoj",54)

##return
def cube(num):
   print("hello")
   return num*num*num
   

print(cube(99999))
##print is primted before the return after the return it gives null

##split method 
def convert(str):
    li = list(str.split(" "))
    return li

str="Hello world and Hi"
print(convert(str))
##string slicing 
def ismail(bomb):
     list1 = []
     list1[0:]= bomb
     return list1

bomb="he is a very good boy"
print(ismail(bomb))    


