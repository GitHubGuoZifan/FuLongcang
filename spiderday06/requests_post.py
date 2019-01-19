import requests

url = 'https://cn.bing.com/ttranslationlookup?&IG=E1E271EFEA254FD9ACE8D7FA793FC41F&IID=translator.5036.15'

headers={
    'user-agent':' Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
}
word = input('请输入要查询的单词：')
formdata = {
    'from':' it',
    'to':'en',
    'text':word,
}
#formdata就是一个原生字典
r = requests.post(url=url,data=formdata,headers=headers)
print(r.text)