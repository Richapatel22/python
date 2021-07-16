n=int(input("enter the number till you want to print fibonacci series"))
t=0
p=1
count=0
print("Fibonacci sequence:")
while count < n:
       print(t)
       sum = t + p
       t = p
       p = sum
       count += 1
