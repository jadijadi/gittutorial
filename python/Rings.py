#Rings
i=int(input("Enter Start:"))
j=int(input("Enter End:"))
#print('------')
for x in range(i):
    for y in range(j):
        print(f"({x},{y})")
while i < j:
    print(i)
    i+=1
