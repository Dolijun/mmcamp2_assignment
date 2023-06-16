import os
import cv2
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

def visual_multi(img_pathes, ann_pathes,opacity=0.4, ncol=5):
    assert len(img_pathes) == len(ann_pathes)
    fig, axes = plt.subplots(nrows=min(5, (len(img_pathes) + 1) // ncol), ncols=ncol, sharex=True, figsize=(12, 12))
    for i in range(min(5 * ncol, len(img_pathes))):
        img_path = img_pathes[i]
        ann_path = ann_pathes[i]
        img = cv2.imread(img_path)
        ann = cv2.imread(ann_path)

        axes[i // ncol, i%ncol].imshow(img[:, :, ::-1])
        axes[i // ncol, i%ncol].imshow(ann[:, :, 0], alpha=opacity)
        axes[i//ncol, i%ncol].axis('off')

    fig.suptitle("Image and Semantic Label", fontsize=30)
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    img_path = "data/dubai_dataset/img_dir/train/1.jpg"
    ann_path = "data/dubai_dataset/ann_dir/train/1.png"

    img = cv2.imread(img_path)
    ann = cv2.imread(ann_path)

    print(img.shape)
    print(ann.shape)

    # cv2.imshow("mask", ann[:, :, 0])
    # cv2.waitKey()
    # cv2.destoryAllWindows()

    # 展示真值
    # plt.imshow(ann[:, :, 0])
    # plt.show()

    # 真值叠加
    # plt.imshow(img[:, :, ::-1])
    # plt.imshow(ann[:, :, 0], alpha=0.3)
    # plt.axis('off')
    # plt.show()

    # 批量可视化
    filelist = os.listdir("data/dubai_dataset/img_dir/train")
    file_nums = [filename.split('.')[0] for filename in filelist]
    img_pathes = [f"data/dubai_dataset/img_dir/train/{i}.jpg" for i in file_nums]
    ann_pathes = [f"data/dubai_dataset/ann_dir/train/{i}.png" for i in file_nums]

    visual_multi(img_pathes, ann_pathes)

