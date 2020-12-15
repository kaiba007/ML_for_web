import io
from PIL import Image


def get_byte_img(img_url):
    with open(img_url, 'rb') as f:
        a = f.read()
    '''对读取的图片进行处理'''
    img_stream = io.BytesIO(a)
    img = Image.open(img_stream)

    imgByteArr = io.BytesIO()
    img.save(imgByteArr, format='PNG')
    imgByteArr = imgByteArr.getvalue()
    print(imgByteArr)
    return imgByteArr