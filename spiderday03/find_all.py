import re
#
# string='<div>大乔</div><div>王昭君</div><div>貂蝉</div>'
# pattern=re.compile(r'<div>(.*?)</div>')
# ret=pattern.findall(string)
# print(ret)
#
string='i love you very much '
pattern=re.compile(r'LOVE',re.I)
ret=pattern.search(string)
print(ret.group())


# pattern=re.compile(r'^abc$')
# string='abc'
# ret=pattern.search(string)
# print(ret.group())
#多行模式
string='''以爱开头的歌词
爱我中华，
爱情三十六计，
爱我别走，
爱上一个不回家的人
'''
pattern=re.compile(r'^爱',re.M)
ret=pattern.findall(string)
print(ret)

#单行模式
# string='''
# <div>细思极恐
# 你的对手在看书
# 你的敌人在磨刀
# 你的闺蜜在减肥
# 隔壁老王在练腰
# </div>
# '''
# pattern = re.compile(r'<div>(.*?)</div>',re.S)
# ret=pattern.search(string)
# print(ret.group(1))