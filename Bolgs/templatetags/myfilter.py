from django import template

register=template.Library()   #Library注册模板标签和过滤器
#这个实例化对象用来注册标签，
@register.filter(name="month_to_upper")
def month_to_upper(value):
    return ["一","二","三","四","五","六","七","八","九","十","十一","十二"][value.month-1]
#前面的是列表，后面的是列表的索引