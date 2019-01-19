import csv
import random
from time import sleep
import pymongo
import requests
from pyquery import PyQuery as pq

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
}
base_url = "https://www.shi-ci.com"
count = 0

def mongo_db():
    conect = pymongo.MongoClient(host="localhost",port=27017)
    db = conect.spider
    table = db.poems
    return table


def get_index_page(url):
    urls = []
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            doc = pq(response.text)
            results = doc("li")
            # print(results)
            for result in results.items():
                result = str(result.children().attr("href"))
                if len(result)>5:
                    urls.append(base_url+"/"+result)
            return urls
    except:
        return None

def get_author_page(url):
    urls = []
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            doc = pq(response.text)
            results = doc(".poem-preview")
            for result in results.items():
                result = str(result.children().attr("href"))
                if len(result) > 5:
                    urls.append(base_url + "/" + result)
            return urls
    except:
        return None

def get_poem_list(url):
    global count
    if count % 100 == 0:
        sleep(random.randint(3, 10))
    urls = []
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            doc = pq(response.text)
            results = doc(".poem-preview")
            for result in results.items():
                result = str(result.children().attr("href"))
                if len(result) > 5:
                    urls.append(base_url + "/" + result)
            return urls
    except:
        return None

def save_to_csv(url):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        doc = pq(response.text)
        title = doc("#poem>h1").text()
        year = doc("#poem>h3").text()
        content = doc("#poem>div").text()
        try:
            with open("poems.csv","a",encoding="utf-8") as csvf:
                filenames = ["title","year","content"]
                writer = csv.DictWriter(csvf,filenames,delimiter=' ')
                writer.writerow({"title": title,"year": year,"content": content})
                print("%ssuccess"%title)
        except ValueError as e:
            print(e)
    return None
def save_to_txt(url):
    global count

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            doc = pq(response.text)
            title = doc("#poem>h1").text()
            year = doc("#poem>h3").text()
            content = doc("#poem>div").text()
            with open("poemsbook.txt","a",encoding="utf-8") as f:
                result = title+"\n"+year+"\n"+content+"\n-------------------\n"
                f.write(result)
                count +=1
                print("%ssuccess,第%d首" % (title,count))
    except:
        return None
def save_to_mongo(url):
    global count
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            doc = pq(response.text)
            title = doc("#poem>h1").text()
            year = doc("#poem>h3").text()
            content = doc("#poem>div").text()
            result = {
                "title":title,
                "year":year,
                "content":content
            }
            collection = mongo_db()
            collection.inser(result)
            count +=1
            print("%ssuccess,第%d首" % (title,count))
    except:
        return None
def start():
    urls = get_index_page(base_url)
    for url in urls:
        author_urls = get_author_page(url)
        for author_url in author_urls:
            poem_urls = get_poem_list(author_url)
            for poem_url in poem_urls:
                save_to_mongo(poem_url)
if __name__ == "__main__":
    start()