import json
import os
import random
import re
import time
from urllib.parse import quote
from selenium import webdriver
from 网络爬虫.MongoConnect import MongoClass
import requests
#guid破解算法
# guid = int(random.random() * 2147483647) * int(time.time() * 1000) % 10000000000
# print(guid)
class QQMusic:

    if not os.path.exists("music/"):
        os.mkdir("music/")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
    }

    def __init__(self):
        #歌手列表链接
        self.singer_list = "https://y.qq.com/portal/singer_list.html#page={0}&"
        #歌曲连接
        self.singer_url = "https://c.y.qq.com/v8/fcg-bin/fcg_v8_singer_track_cp.fcg?g_tk=5381&jsonpCallback=MusicJsonCallbacksinger_track\
&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0&singermid={2}&order=listen&begin=\
{0}&num={1}&songstatus=1"
        #下载链接

        #解码连接
        self.vkey_url = "https://u.y.qq.com/cgi-bin/musicu.fcg?callback=getplaysongvkey7018660354323933&g_tk=5381&jsonpCallback=getplaysongvkey70186603543239\
33&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0&data={}"#songmid
        self.song_collection = MongoClass("spider", "qqmusic").cllection
        self.singer_collection = MongoClass("spider","qqsinger").cllection

    def __del__(self):
        print("success!!!!!!!!!!")
    #根据歌手名字生成vkey请求链，返回列表
    def get_songvkey_by_singername(self,name):
        if isinstance(name, str):
            vkey_urls = []
            ss = self.song_collection.find({"singer_name":{"$regex":"{}".format(name)}})

            for x in ss:
                songmid = x.get("songmid")
                songname = x.get("songname")
                data_dict = {"req": {"module": "CDN.SrfCdnDispatchServer", "method": "GetCdnDispatch",
                                "param": {"guid": "7716147620", "calltype": 0, "userip": ""}},
                        "req_0": {"module": "vkey.GetVkeyServer", "method": "CgiGetVkey",
                                  "param": {"guid": "7716147620", "songmid": [songmid], "songtype": [0], "uin": "0",
                                            "loginflag": 0, "platform": "20"}},
                        "comm": {"uin": 0, "format": "json", "ct": 20, "cv": 0}}
                temp = json.dumps(data_dict)
                data = quote(str(temp),encoding="utf-8")
                url = self.vkey_url.format(data)
                print(url)
                data_dict.clear()
                vkey_urls.append({"songname":songname,"url":url})
            return vkey_urls
        else:
            raise Exception("TypeError")
    # 根据歌曲名字生成vkey请求链,返回列表
    def get_songvkey_by_songname(self,name):
        if isinstance(name, str):
            vkey_urls = []
            x = self.song_collection.find({"songname":{"$regex":"{}".format(name)}})
            for i in x:
                songmid = i.get("songmid")
                songname = i.get("songname")
                data_dict = {"req": {"module": "CDN.SrfCdnDispatchServer", "method": "GetCdnDispatch",
                                     "param": {"guid": "7716147620", "calltype": 0, "userip": ""}},
                             "req_0": {"module": "vkey.GetVkeyServer", "method": "CgiGetVkey",
                                       "param": {"guid": "7716147620", "songmid": [songmid], "songtype": [0],
                                                 "uin": "0",
                                                 "loginflag": 0, "platform": "20"}},
                             "comm": {"uin": 0, "format": "json", "ct": 20, "cv": 0}}
                temp = json.dumps(data_dict)
                data = quote(str(temp), encoding="utf-8")
                url = self.vkey_url.format(data)
                # print(url)
                data_dict.clear()
                vkey_urls.append({"songname":songname,"url":url})
            return vkey_urls
        else:
            raise Exception("TypeError")
    #根据获取到vkey下载歌曲
    def download_music(self,vkey_urls):
        for x in vkey_urls:
            response = requests.get(x["url"],headers=self.headers).text.strip("getplaysongvkey7018660354323933( )")
            dicts = json.loads(response)
            songname = x["songname"]

            pur = dicts["req_0"]["data"]["midurlinfo"][0]["purl"]
            http = dicts["req"]["data"]["freeflowsip"][0]
            songmid = dicts["req_0"]["data"]["midurlinfo"][0]["songmid"]
            if pur :
                download_url = http + pur
                self.song_collection.update_one({"songmid": songmid}, {"$set": {"download_url": download_url}})
            else:
                continue
            print(download_url)
            print("-----------------------开始下载:   %s----------------------"%songname)
            self.request_music(download_url,songname)
            print("-----------------------结束下载:   %s----------------------"%songname)
    #获取所有歌手信息
    def get_singers(self,page_start,page_end):
        option = webdriver.ChromeOptions()
        option.add_argument('--headless')
        for page in range(page_start,page_end+1):
            driver = webdriver.Chrome(chrome_options=option)
            driver.get(self.singer_list.format(page))
            mid = driver.find_elements_by_class_name("js_singer")
            for x in mid:
                data_singermid = x.get_attribute("data-singermid")
                data_singerid = x.get_attribute("data-singerid")
                title = x.get_attribute("title")
                href = x.get_attribute("href")
                result = {
                    "data_singermid":data_singermid,
                    "data_singerid":data_singerid,
                    "title":title,
                    "href":href
                }
                if data_singerid:
                    print("##############开始存储:   %s############" % title)
                    self.singer_collection.update_one({"data_singerid":data_singerid},{"$set":result},upsert=True)
                    print("############存储: %s  成功############" % title)
            driver.quit()
    #获取该歌手的所有歌曲信息
    def get_songs(self,name):
        if isinstance(name, str):
            singermid = self.get_singer_mid(name)
            jsons = requests.get(self.singer_url.format(0,1,singermid)).text.strip("MusicJsonCallbacksinger_track( )")
            jsons = json.loads(jsons)
            total = jsons["data"]["total"]
            jsons = requests.get(self.singer_url.format(0, total,singermid)).text.strip("MusicJsonCallbacksinger_track( )")
            jsons = json.loads(jsons)
            song_list = jsons["data"]["list"]
            singer_name = jsons["data"]["singer_name"]
            singer_id = jsons["data"]["singer_id"]
            for one_song in song_list:
                songmid = one_song["musicData"]["songmid"]
                songname = one_song["musicData"]["songname"]
                result = {"singer_name":singer_name,"singer_id":singer_id,"total":total,"songmid":songmid,"songname":songname}
                print("+++++++++++++++开始存储:   %s++++++++++++++"%songname)
                self.song_collection.update_one({"songmid":songmid},{"$set":result},upsert=True)
                print("+++++++++++++++存储: %s  成功++++++++++++++"%songname)

    #下载音乐
    def request_music(self,download_url,filename):
        path = os.path.join("music",filename+".m4a")
        if not os.path.exists(path):
            content = requests.get(download_url).content
            with open(os.path.join("music",filename+".m4a"),"wb") as f:
                f.write(content)
        else:
            return None
    #获取歌手的mid
    def get_singer_mid(self,name):
        if isinstance(name, str):
            return self.singer_collection.find_one({"title":{"$regex":"{}".format(name)}})["data_singermid"]
        else:
            raise Exception("TypeError")
    #通过歌曲名称下载音乐
    def download_by_songname(self,name):
        if isinstance(name,str):
            hrefs = self.song_collection.find({"songname": name, "download_url": {"$exists": True}})
            if hrefs.count():
                for href in hrefs:
                    print(href["download_url"])
                    self.request_music(href["download_url"],href["songname"])
            else:
                veks = self.get_songvkey_by_songname(name)
                self.download_music(veks)
        else:
            raise Exception("TypeError")
    #通过歌手名字下载音乐.
    def download_by_singername(self,name):
        if isinstance(name,str):
            hrefs = self.song_collection.find({"singer_name": name, "download_url": {"$exists": True}})

            if hrefs:
                for href in hrefs:
                    self.request_music(href["download_url"], href["songname"])
            else:
                veks = self.get_songvkey_by_singername(name)
                self.download_music(veks)
        else:
            raise Exception("TypeError")
if __name__ == '__main__':
    qqmusic = QQMusic()
    #获取xxx曲库
    # qqmusic.get_songs("邓紫棋")

    # qqmusic.get_singers(201,295)
    # qqmusic.get_songs("林俊杰")
    # qqmusic.download_by_songname("穿越")