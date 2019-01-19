from lxml import etree
#生成tree对象
tree=etree.parse('ppp.html')
#获取文本内容
# ret=tree.xpath('//li[@id="dumu"]/text()')
#获取类的值
# ret=tree.xpath('//div[@class="tang"]/ul/li[3]/@class')
#找出文本中包含花的文本内容
# ret=tree.xpath('//li[contains(text(),"花")]/text()')
# ret=tree.xpath('//li[start-with(@class,"w")]/text()')
#查找包含换行符在内的id为girl的所有的文本内容
# ret=tree.xpath('//div[@id="girl"]/text()')
#去掉里面的换行符
ret=tree.xpath('//div[@id="girl"]//text()')
string=''.join(ret).replace('\n','').replace('\t','')
print(string)