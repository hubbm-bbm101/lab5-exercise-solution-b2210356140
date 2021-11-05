x = int(input("Please enter a number:"))
y=0
z=0
m=0
for i in range(1, x+1):
    if i%2==1:
        y = y+i
    else:
        z=z+i
        m=m+1

print("Sum of odd numbers: " + str(y))
print("Average of even nubers: " + str(z/m))