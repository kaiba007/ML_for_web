import cv2
import io
import numpy as np
from PIL import Image

def get_eye_pix():
# 异常处理：防止传入非图片的东西
    try:
        face_xml = cv2.CascadeClassifier('./static/haarcascade_frontalface_default.xml')
        eye_xml = cv2.CascadeClassifier('./static/haarcascade_eye.xml')
        img = cv2.imread('./static/face.png')
        # cv2.imshow('src', img)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # detect faces 1 (gray)data 2 scale 3 5(目标大小，人脸最小不能小于5个像素)
        faces = face_xml.detectMultiScale(gray, 1.3, 5)
        print('faces=', len(faces))
        # draw给人脸画方框
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)  # 最后一个参数：线条宽度
            # detect eyes
            roi_face = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]
            eyes = eye_xml.detectMultiScale(roi_face)
            print('eyes=', len(eyes))
            # draw 给眼睛画方框
            for (e_x, e_y, e_w, e_h) in eyes:
                cv2.rectangle(roi_color, (e_x, e_y), (e_x + e_w, e_y + e_h), (0, 0, 255), 2)
        # cv2.imshow('dst', img)
        cv2.imwrite('./static/face_result.png',img)
        cv2.waitKey(0)
        info = '预测分类成功，点击获取识别图片'
        return info
    except Exception as e:
        return_info = {"result": [str(e)]}
    return return_info