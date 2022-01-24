# Question 2:
# Create a pyramid of X's for n number of levels:

num = int(input("Enter Number Of Rows : "))
for y in range(0,num):
    for z in range(0,num-y-1):
        print(end=" ") 
    for z in range(0,y+1):
        print("x",end=" ")
    print()


    
