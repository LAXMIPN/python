list1=[1,5,9,44,77,65]
list2=[90,5,60,21,3]
print("list1:",list1)
print("list2:",list2)
print("length of list1:",len(list1))
print("length of list2:",len(list2))
if len(list1)==len(list2):
    print("length of the two list are equal")
else:
    print("length is not equal")
    print("sum of list1:",sum(list1))
    print("sum of list2",sum(list2))
    if sum(list1)==sum(list2):
        print("sum of the lists are equal")
    else:
        print("the sum of the list are not equal")
check=any(item in list1 for item in list2)
print("any value occur both:",check)