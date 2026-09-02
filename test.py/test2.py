total=0
for i in range(1,101):
    if i%2!=0:
        continue
total+=i                
print(total)
for i in range(1,10):
    for j in range(1,i+1):
     print(f'{i}*{j}={i*j}',end='\t')



a,b=0,1
for _ in range(20):
    a,b=b,a+b
    print(a)

for num in range(100,1000):
    high=num//100
    mid=num//10%10
    low=num%10
    if high**3+mid**3+low**3==num:
        print(num)
    
    
