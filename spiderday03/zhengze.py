import re

#如何使用
#match,search,findall,compile,sub
'''
match:从字符串开始匹配，匹配失败返回none，匹配成功立马结束
search:从字符串任意位置开始匹配，匹配成功立马结束，匹配失败返回none 
只能匹配一个，返回一个对象ret
ret.group()  查看匹配结果
'''
#生成正则表达式 有的是 \1 \2 有的是$1  $2
string='<div><span>一骑红尘妃子笑，无人知是荔枝来</span></div>'
pattern=re.compile(r'<(\w+)><(\w+)>(.*)</\2></\1>')
ret=pattern.match(string)
# ret=re.match(r'',string)
print(ret.group(1))
print(ret.group(2))
print(ret.group(3))