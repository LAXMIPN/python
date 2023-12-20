newlist="web programming using php"
list=[i for i in newlist.casefold()]
dict={}.fromkeys(list,0)
for i in newlist.casefold():
    if i in dict:
        dict[i]=dict[i]+1
print(newlist)
print(dict)
