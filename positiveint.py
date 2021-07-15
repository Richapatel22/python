n = int(input("Enter the number of elements you'd like to enter: "))

l = list()

for i in range(n):

 x = int(input("Enter the element: "))

 l.append(x)

 num=list()
for i in l:

 if i > 0:

   num.append(i)

print(num)
