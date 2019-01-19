import urllib.request
import urllib.parse
#ajax_post局部刷新
post_url='https://fanyi.baidu.com/v2transapi'
#post参数
formdata={
    'from': 'en',
	'to': 'zh',
	'query': 'woman',
	'transtype': 'realtime',
	'simple_means_flag': '3',
	'sign': '814534.560887',
	'token': '05cf25c0cc32904d8c773f124c81d2d0',
}
formdata=urllib.parse.urlencode(formdata).encode('utf8')
#构建请求对象
headers={
    'Accept': '*/*',
	# 'Accept-Encoding': 'gzip, deflate, br',
	'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
	'Connection': 'keep-alive',
	# 'Content-Length': '121',
	'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
	'Cookie': 'BIDUPSID=6F6C332F8A0E3C9949BD5D9F884F1FFB; BAIDUID=EBF0141899EAFDB3849E880FE66EBFE0:FG=1; PSTM=1536564348; PSINO=1; BDRCVFR[auK81cz0o7_]=mk3SLVN4HKm; pgv_pvi=3136647168; pgv_si=s1616527360; BDRCVFR[iqrboYocJ-C]=jCHWiyEa0lYpAN8n1msQhPEUf; BDRCVFR[Ke8kQFs3CYT]=jCHWiyEa0lYpAN8n1msQhPEUf; H_PS_PSSID=; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; locale=zh; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1536634908; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1536634908; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D',
	'Host': 'fanyi.baidu.com',
	'Origin': 'https://fanyi.baidu.com',
	'Referer': 'https://fanyi.baidu.com/?aldtype=16047',
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
	'X-Requested-With': 'XMLHttpRequest',

}
request=urllib.request.Request(url=post_url,headers=headers)
response=urllib.request.urlopen(request,data=formdata)
print(response.read().decode())
