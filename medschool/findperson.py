import json

with open("result.json","r+",encoding="utf-8") as f:
    personlist=json.loads(f.read())

persons=[]
for i in personlist:
    n=list(i.values())[0]
    # print(n)
    persons.append(n)



with open("temp.txt","r+",encoding="utf-8") as f:
    content=f.readlines()
    # print(content[4])
    # if content[4].endswith('PhD\r\n'):
    #     print(1)
    for i in content:
        # print(i)
        name=''
        i=i.strip()
        if i.endswith('PhD') or  i.endswith('MD'):
            name=i.split(' ')
            # print(name)
            for j in name:
                # print(j)
                j=j.strip(",")
                j=j.strip('')
                # print(j)
                if len(j)>3 and j is not "PhD" and j is not "MD":
                    for k in persons:
                        if j in k:
                            print(i)
                            print(k)
                            print("-"*100)


