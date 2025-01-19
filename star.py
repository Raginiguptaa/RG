

num=int(input("Enter the number\n"))

for i in range(1,num+1):
    for j in range(1,num+1):
        print(j,end=" ")

    print("\n")    


print("_____________________________________________________________________________________")
for i in range(1,num+1):
    for j in range(1,i+1):
        print(j,end=" ")

    print("\n") 


print("______________________________________________________________________________________")

lst=[1,2,3,4,5]
#find sum of the list
sum=0
for i in range (len(lst)):
    sum=sum+lst[i]


print(sum)
    