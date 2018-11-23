# n个圆盘由a柱移动到c柱，借助b柱
def hanoi(a,b,c,p):
    if len(p) == 1:
        print("圆盘{}:{}-->{}".format( str(p[0]), a, c))
    else:
        hanoi(a,c,b,p[0:-1])
        hanoi(a,b,c,[p[-1]])
        hanoi(b,a,c,p[0:-1])
        
[老师] 09:02:08
# n个圆盘由a柱移动到c柱，借助b柱
def hanoi(a,b,c,n):
    if n == 1:
        print(a + "-->" + c)
    else:
        hanoi(a,c,b,n-1)
        hanoi(a,b,c,1)
        hanoi(b,a,c,n-1)
[老师] 09:06:12
p = range(1,5)  
hanoi('a','b','c',p)
