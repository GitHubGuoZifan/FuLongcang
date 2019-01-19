import urllib.request
import urllib.error

url='http://www.maodan.com/'

try:
    response = urllib.request.urlopen(url)
# except urllib.error.URLError as e :
    #精确捕获
except urllib.request.HTTPError as e :
    print(e)

print('代码正常运行')