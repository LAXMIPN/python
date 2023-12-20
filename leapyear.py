fyear=int(input("enter the current year"))
lastyear=int(input("enter the last year"))
print("leap years are")
for i in range(fyear,lastyear):
    if(i%4==0)and(i%100!=0)or(i%400==0):
        print(i)

