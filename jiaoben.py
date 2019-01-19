from urllib.request import urlretrieve
import json, os
with open("‪点评.txt", "r", encoding="utf8") as f:
    for index, x in enumerate(f):
        x = json.loads(x)
        print(x, type(x))
        # pat = os.path.join(x["商品名称"][0]+".jpg")
        pat = os.path.join(str(index)+ ".jpg")
        print(pat)
        urlretrieve("http:"+x["商品图片地址"][0], pat)