friends_file= open("eop.txt","r")
tyou = open("eop.txt", "a")
print(friends_file.readable())
print(tyou.readable())

for friend in friends_file.readlines():
    print(friend)

##print(friends_file.readline())
##print(friends_file.readlines())
friends_file.close()





intel_core = open("intel.txt","a")
print(intel_core.writable())
intel_core.write("\nHello ")
##for words in intel_core.readlines():
  ##  print(words)

##don't use two at same time you get the error