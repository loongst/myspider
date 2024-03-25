'''
#斐波那契数列
a,b=0,1
while b<100:
    print(b,end=",")
    a,b=b,a+b
'''

'''
#迭代器和生成器
list=[1,2,3,4,5]
it=iter(list)
for x in it:
    print(x,end=" ")
'''

'''
import sys
def fibonacci(n): #斐波那契生成器函数
    a,b,counter=0,1,0
    while True:
        if(counter>n):
            return
        yield a
        a,b=b,a+b
        counter+=1
f=fibonacci(10) #f是一个迭代器
while True:
    try:
        print(next(f),end=" ")
    except StopIteration:
        sys.exit()

'''

'''
import pickle
data1={'a':[1,2.0,3,4+6j],
        'b':('string',u'Unicode string'),
        'c':None}
selfref_list=[1,2,3]
selfref_list.append(selfref_list)
output=open('data.pkl','wb')

pickle.dump(data1,output)

pickle.dump(selfref_list,output,-1)

output.close()

'''
'''
import os,sys
ret=os.access("data.pkl",os.X_OK)
print(ret)

class Myclass:
    name=''
    age=0
    sex=''
    def __init__(self,n,a,s):
        self.data=[1,2,3,4]
        self.name=n
        self.age=a
        self.sex=s
        self.mimi='3d'
        self.girl='somuch'
    def f(self):
        return 'hello world'
class Myclass2(Myclass):
    def f(self):
        print("fuck sexy girl mimi")
    pass 
y=Myclass2('sexgirl','25','famale')
print(y.name,y.age,y.sex,y.mimi,y.girl)


x=Myclass('xml',25,'male')
print(x.data,x.name,x.age,x.sex,x.mimi,x.girl)

'''
'''
print(x.name,x.age)
 
print(x.i)
print(x.f())

                                                                                                                                                                                                                                                                                                                                                                                                 ;
x.data=[4,5,6,7]
print(x.data)

'''



#三角形面积
'''
def area3():
    a=[]
    d=0
    for i in range(0,3):
        a.append(float(input("input oneside length:")))
        d+=a[i]
    s=d/2
    area=(s*(s-a[0])*(s-a[1])*(s-a[2]))**0.5
    print("三角形面积：%2.4f"%area)
'''

'''
#文件IO
with open('test.txt','wt') as f:
    f.write("这是一句话啊！")

with open('test.txt','rt') as outf:
    text=outf.read()
    print(text)
'''

'''
#二分查找法
mylist=[1,3,4,6,7,8,10,13,14]
list1=[2,3,4,10,40]
startn=0
endn=len(mylist)
print(endn)
def twochoice(mylist,startn,endn,m):
    p=int((endn+startn)/2)
    print(p,mylist[p])
    if m==mylist[p]:
        print(p)
    elif m<mylist[p]:
        endn=p-1
        twochoice(mylist,startn,endn,m)
    else:
        startn=p+1
        twochoice(mylist,startn,endn,m)
twochoice(mylist,0,endn,4)
endn=len(list1)
twochoice(list1,0,endn,10)
'''

'''
#list方法  
# append（需要插入的元素） 
# extend（[需要插入的元素1，。。。2]） 
# insert（位置索引，元素）
# remove（元素）  del listname【索引】 
# pop（）删除最后一个元素

dir(list) 输出list的所有内置方法

list1=list2 只是将list2的地址标签赋给list1，如果需要拷贝list2，需要使用分片：list1=list2[:]

params
'''

'''
#汉诺塔  x上n个盘子， yz为空， 
#  先将前n-1个移动到y上，    func(n-1)
# 然后将最下面一个移动到z上， 1
# 最后将前n-1个移动到z上     func(n-1)
#
#
#
def hl(n):
    if n==1:
        return 1
    else:
        return 2*hl(n-1)+1
while True:
    n=int(input("塔的层数："))
    print(hl(n))

'''


#精简计时器
import  time

class Mytime():
    def __init__(self):
        self.start=[]
        self.stop=[]
        self.counts=[]

    def __str__(self):
        return 

#即计时开始
    def Countstart(self):
        self.start=time.localtime()
        print("计时开始！"+str(self.start))
        
#计时结束
    def Countstop(self):
        print(self.start)
        self.stop=time.localtime()
        print("计时结束！"+str(self.stop))
        self.__calc()


    def __calc(self):
        for index in range(6):

            self.counts.append(self.stop[index]-self.start[index])
            print(self.counts)
t=Mytime()
while True:
    
    cmd=input("k开始，j结束，请输入指令：")
    if cmd=='k':
        t.Countstart()
    elif cmd=='j':
        t.Countstop()
    else:
        print("指令有误")
        break

        
