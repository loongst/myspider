import json
import csv
import datetime
with open("result.json","r+") as f:
    content=f.read()
    print(json.loads(content)[0])


ext=["t"+str(i) for i in range(50)]
header=['nickName','phonenumber']
header.extend(ext)


# print(header)


def comparetime(t1,t2):
    if datetime.datetime.strptime(t1,"%Y-%m-%d %H:%M:%S") <datetime.datetime.strptime(t2,"%Y-%m-%d %H:%M:%S"):
        return True
    else:
        return False







with open("数据.csv","a+",encoding='gbk',newline='') as f:
    # 1.创建写入对象
    # fieldnames = [] 指定表头
    # 表头名字和字典里的键一定要一致
    # 我们是根据字典里的键去寻找对应的表头名字 如果没有 则报错
    write = csv.DictWriter(f,fieldnames=header)
    # 2.将表头写入
    write.writeheader()
    for i in json.loads(content):
        print("^"*100)
        print(i)
        ret={}
        ret['nickName']=i['nickName']
        ret['phonenumber']=str(i['phonenumber'])+'\t'

        tmp=[]

        mmset=[]
        for mm in i['bloodinfo']:
            mmset.append(mm['time'].split(' ')[0])
        mmset=list(set(mmset))
        mmset.sort(reverse=True)

        endlist=[]
        for jj in mmset:
            tt=[]
            print(i['bloodinfo'])
            print("/"*200)
            for kk in i['bloodinfo']:
                if kk['time'].split(' ')[0]==jj:
                    tt.extend([kk])
            if len(tt)<2:
                endlist.extend(tt)
            else:
                tmpM=tt[0]
                for d in range(1,len(tt)):
                    if comparetime(tt[d]['time'],tmpM['time']):
                        tmpM=tt[d]
                print(tmpM)
                endlist.extend([tmpM])
        print(endlist)

        i['bloodinfo']=endlist
        print("+"*100)
        for j in range(len(i['bloodinfo'])-1,-1,-1):
            tmp.extend(list(i['bloodinfo'][j].values()))
        for k in range(len(tmp)):
            ret[header[k+3]]=str(tmp[k])+'\t'
        print(ret)
        
        # 3.将数据写入
        # for i in content:
        write.writerow(ret)
        # print(content)