import re

#re.search
#在一个字符串中搜索匹配正则表达式的第一个位置，返回match对象  
match=re.search(r'\d',"my name is xml ,age 23")
if match:
    print(match.group(0))

#re.match
#从一个字符串的开始位置起匹配正则表达式，返回match对象
match=re.search(pattern,objectstring)
if match:
    print(match.group(0))

#re.findall()
#搜索字符串，以列表类型返回全部能匹配的字符串

#