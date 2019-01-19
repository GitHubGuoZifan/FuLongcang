import  requests
from bs4 import BeautifulSoup
'''
爬取网易云音乐热门排行榜
'''
#headers写多点是为了反爬
headers = {
    'Host': 'music.163.com',
    'Origin': 'https://music.163.com',
    'Referer': 'https://music.163.com/discover/toplist?id=2884035',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
}
base_url=[
    "https://music.163.com/#/discover/toplist?id=2884035", #网易原创歌曲榜
    "https://music.163.com/#/discover/toplist?id=3779629",#云音乐新歌榜，
    "https://music.163.com/#/discover/toplist?id=3778678",#云音乐热歌榜
]
#创建一个会话保持
session = requests.session()
#获取各个排行榜的bs4对象
def get_class(urls):
    ul_list = []
    for url in urls:
        response = session.get(url,headers=headers)
        bs = BeautifulSoup(response.text,'lxml')
        ul = bs.find(name='ul',class_='f-hide')
        ul_list.extend(ul)
    return ul_list
#bs4解析，获取音乐名称和id
def get_urls(ul_obj):
    song_urls=[]
    for ul in ul_obj:
        href = "https://music.163.com/#/discover/toplist?" + ul["href"].split("?")[-1] + ".mp3"
        title = ul.string + ".mp3"
        result = {"href":href,"title":title}
        song_urls.append(result)
        print(href,title)
    print(song_urls)
    return song_urls
#音乐下载
def sav_song(song_urls):
    for song in song_urls:
        path = "music/"+song["title"]
        print("正在下载{}".format(song["title"]))
        with open(path,'wb') as fp :
            content = requests.get(song["href"])
            fp.write(content)
        print("保存{}成功".format(song["title"]))

if __name__ == '__main__':
    ul_objs = get_class(base_url)
    for x in ul_objs:
        song_url = get_urls(x)
        sav_song(song_url)
