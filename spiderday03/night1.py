import re
# string='<div>大乔</div><div>王昭君</div><div>貂蝉</div><div>雅典娜</div><div>阿珂</div>'
# pattern=re.compile(r'<div>(.*?)</div>')
# ret=pattern.findall(string)
# print(ret)

#忽略大小写
# string='i love you very much'
# pattern=re.compile(r'LOVE',re.I)
# ret=pattern.search(string)
# print(ret.group())

#多行模式
# string='''
# 以爱开头的歌词
# 爱我中华，爱我中华
# 爱情36计
# 爱我别走，如果你说你不爱我
# 爱上一个不回家的人
# '''
# pattern=re.compile(r'^爱',re.M)
# ret=pattern.findall(string)
# print(ret)

#单行模式
string='''
<div>
细思极恐
你的对手在看书
你的敌人在磨刀
你的闺蜜在减肥
隔壁老王在炼腰
</div>
'''
pattern=re.compile(r'<div>(.*?)</div>',re.S)
ret=pattern.search(string)
print(ret.group(1))