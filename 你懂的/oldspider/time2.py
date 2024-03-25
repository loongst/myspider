import time as t

class Mytimer():

    def __str__(self):
        return self.prompt

    def __repr__(self):
        return self.prompt

    def __init__(self):
        self.begin=0
        self.end=0
        self.prompt="未开始计时！"
        self.lasted=[]
        self.unit=['年','月','日','时','分','秒']

    def start(self):
        print("开始计时！")
        self.prompt="请先开始计时！"
        self.begin=t.localtime()

    def stop(self):
        if not self.begin:
            self.prompt="请先开始计时！"
        else:
                
            print("计时结束！")
            self.end=t.localtime()
            self.__calc()

    #内部方法，计算运行时间
    def __calc(self):

        self.lasted=[]
        self.prompt="总共运行时间为"
        for index in range(6):
            self.lasted.append(self.end[index]-self.begin[index])
            self.prompt+=str(self.lasted[index])+str(self.unit[index])
        print(self.prompt)

    def __add(self,other):
        pass
        

m=Mytimer()
while True:
    
    cmd=input("k开始，j结束，请输入指令：")
    if cmd=='k':
        m.start()
    elif cmd=='j':
        m.stop()
    else:
        print("指令有误")
        break
