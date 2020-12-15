import os
import io
import json
import torch
import torch.nn as nn
import torchvision.transforms as transforms
from PIL import Image
from model import AlexNet

def transform_image(image_bytes):
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    my_transforms = transforms.Compose([transforms.Resize(255),
                                        transforms.CenterCrop(224),
                                        transforms.ToTensor(),
                                        transforms.Normalize(
                                            [0.485, 0.456, 0.406],
                                            [0.229, 0.224, 0.225])])
    image = Image.open(io.BytesIO(image_bytes))
    if image.mode != "RGB":
        raise ValueError("input file does not RGB image...")
    return my_transforms(image).unsqueeze(0).to(device)


def get_prediction(image_bytes):
# 异常处理：防止传入非图片的东西
    try:
        weights_path = "./Alexnet.pth"
        class_json_path = "./class_indices.json"
        assert os.path.exists(weights_path), "weights path does not exist..."
        assert os.path.exists(class_json_path), "class json path does not exist..."

        # select device
        device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        print(device)
        # create model
        model = AlexNet(num_classes=5)
        # load model weights
        model.load_state_dict(torch.load(weights_path, map_location=device))
        model.to(device)
        model.eval()

        # load class info
        json_file = open(class_json_path, 'rb')
        class_indict = json.load(json_file)


        tensor = transform_image(image_bytes=image_bytes)
        outputs = torch.softmax(model.forward(tensor).squeeze(), dim=0)
        # detach去除梯度信息
        prediction = outputs.detach().cpu().numpy()
        # < 左对齐
        template = "class:{:<15} probability:{:.3f}"
        index_pre = [(class_indict[str(index)], float(p)) for index, p in enumerate(prediction)]
        # sort probability
        index_pre.sort(key=lambda x: x[1], reverse=True)
        text = [template.format(k, v) for k, v in index_pre]
        return_info = {"result": text}
    except Exception as e:
        return_info = {"result": [str(e)]}
    return return_info