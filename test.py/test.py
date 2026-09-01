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