print("hello world")
a=10
b=20
print(a+b)
print(type(a))
c='123'
print(int(c, base=16))
f=float(input("请输入华氏温度"))
c=(f-32)/1.8
print("%.2f华氏度=%.2f摄氏度"%(f,c))
import math
radius=float(input("请输入圆的半径"))
perimeter=2*math.pi*radius
area=math.pi*radius*radius
print(f"周长={perimeter:.1f}")
print(f"面积={area:.1f}")
year=int(input("请输入年份"))
is_leap=year%4==0 and year%100!=0 or year%400==0
print(f'{is_leap=}')
status_code=int(input("请输入状态码"))
match status_code:
    case 200:
        description="请求成功"
    case 404:
        description="资源未找到"
    case 500:
        description="服务器内部错误"
    case _:
        description="未知状态码"
print("状态码status_code:",description)
x=float(input("请输入一个整数"))
if x>1:
   y=3*x-5
elif x>=-1:
    y=x+2       
else:
    y=5*x+3
print(f'{y=}')
import time
for _ in range(5):
    print("hello world")
    time.sleep(1)
total=0
for i in range(1,101):
    total+=i
print(total)
lxy=0
for i in range(1,101):
    if i%2==0:
        lxy+=i
print(lxy)
print(sum(range(1,101,2)))
chw=0
i=1
while i<=100:
    chw+=i
    i+=1
print(chw)