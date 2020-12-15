import os
import io
import json
import torch
import torchvision.transforms as transforms
from PIL import Image
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from model import AlexNet
from alexnet import get_prediction
from eye_detect import get_eye_pix
from neural_style import style_transfer
from utils import get_byte_img

app = Flask(__name__)
CORS(app)  # 解决跨域问题

@app.route("/flow_predict", methods=["POST"])
@torch.no_grad()
def predict():
    image = request.files["file"]
    img_bytes = image.read()
    print(type(img_bytes))
    info = get_prediction(image_bytes=img_bytes)
    return jsonify(info)

@app.route('/pushFace',methods=[ 'POST'])
def pushFace():
    image = request.files["file"]
    image.save('./static/face.png')
    info = get_eye_pix()
    return jsonify(info)

@app.route('/pushNeu',methods=[ 'POST'])
def pushNeu():
    image = request.files["file"]
    image.save('./static/neu.jpg')
    info = style_transfer( width=500)
    return jsonify(info)

@app.route('/getNeu',methods=['GET', 'POST'])
def getNeu():
    img_url = './static/neu_result.jpg'
    imgByteArr = get_byte_img(img_url)
    return imgByteArr

@app.route('/getFace',methods=['GET', 'POST'])
def getFace():
    img_url = './static/face_result.png'
    imgByteArr = get_byte_img(img_url)
    return imgByteArr



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)




