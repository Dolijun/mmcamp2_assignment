from mmpretrain import ImageClassificationInferencer
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont


def cv2ImgAddText(img, text, left, top, *, textStyle, textColor=(0, 0, 0), textSize=20):
    if isinstance(img, np.ndarray):
        img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    # Draw Object
    draw = ImageDraw.Draw(img)

    # font style
    fontStyle = ImageFont.truetype(textStyle, textSize, encoding='uft-8')

    draw.text((left, top), text, textColor, font=fontStyle)

    return cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)



inf = ImageClassificationInferencer('resnet50_ft.py', pretrained='out_0/epoch_10.pth')
img_path = 'apple.png'
res = inf(img_path, show=False)
#
print(res)
pred_label = res[0]['pred_label']
pred_score = res[0]['pred_score']
pred_class = res[0]['pred_class']
txt = f"{str(pred_label)}-{pred_class}-{pred_score}"


img = cv2.imread(img_path)
img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
img = cv2ImgAddText(img, txt, 0, 0, textStyle='font/FZSJ-BHTJW.TTF', textSize=24)
img = cv2ImgAddText(img, txt, 0, 30, textStyle='font/FZY3JW.TTF')

## save img
cv2.imwrite('apple_res.png', img)

## show img
# cv2.imshow('show', img)
# cv2.waitKey()
# cv2.destoryAllWindows()