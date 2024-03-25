import  time as t
class Mytime():
    def __init__(self):
        self.begin=0
        self.end=0
        self.prompt=""

    def __str__(self):
        return self.prompt

    __repr__=__str__

    def start(self):
        self.begin=t.localtime()
        print("计时开始！")

    def stop(self):
        if not self.begin:
            print("计时未开始！")
        else:
            self.end=t.localtime()
            print("计时结束！")
            self.__calc()

    def __calc(self):
        self.lasted=[]
        self.prompt="统计时间为:"
        for index in range(6):
            self.lasted.append(self.end[index]-self.begin[index])
        print(self.prompt+str(self.lasted)+"秒")
m=Mytime()
while True:
    
    cmd=input("k开始，j结束，请输入指令：")
    if cmd=='k':
        m.start()
    elif cmd=='j':
        m.stop()
    else:
        print("指令有误")
        break
    
