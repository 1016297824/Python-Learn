# re的匹配方法
import re

# re.match()方法:从头匹配字符串，返回匹配对象，匹配失败返回None
s = "python java C# C++ mySQL"
result = re.match("python", s)
if not result:
    print("匹配失败")
print(result)
print(result.span())
print(result.group())
print()

s = "python java C# C++ mySQL"
result = re.match("python1", s)
if not result:
    print("匹配失败")
print(result)
print()

# re.search()方法:从字符串任意位置匹配，找到第一个返回匹配对象，匹配失败返回None
s = "python java java C# C++ mySQL"
result = re.search("java", s)
if not result:
    print("匹配失败")
print(result)
print(result.span())
print(result.group())
print()

# re.findall()方法:返回所有匹配的字符串，返回列表，匹配失败返回空列表
s = "python java java C# C++ mySQL"
result = re.findall("java", s)
if not result:
    print("匹配失败")
print(result)
print(len(result))

s = "python java java C# C++ mySQL"
result = re.findall("CC", s)
if not result:
    print("匹配失败")
print(result)
print()
