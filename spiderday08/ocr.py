import pytesseract
from PIL import Image

def shibie(imagepath):
    #先处理图片，然后再识别
    #打开文件
    img = Image.open(imagepath)

    #转化为灰度图片
    img = img.convert('L')

    #img.show()
