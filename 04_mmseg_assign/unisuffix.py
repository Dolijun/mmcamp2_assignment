import os
import cv2
import re

def unify_suffix(path, suffix=".jpg"):
    img_files = os.listdir(path)
    for img_file in img_files:
        searchObj = re.search("^[^\.]+(\..+)$", img_file)
        if searchObj.group(1) != suffix:
            new_file = img_file.replace(searchObj.group(1), suffix)
            # new_file = re.sub("\..+?$", suffix, img_file)
            # new_file = img_file.split(".")[0] + suffix
            img = cv2.imread(os.path.join(path, img_file))
            cv2.imwrite(os.path.join(path, new_file), img)
            os.remove(os.path.join(path, img_file))


if __name__ == '__main__':
    img_paths = [f"data/Watermelon87_Semantic_Seg_Mask/img_dir/{dir}" for dir in ["train", "val"]]
    for path in img_paths:
        unify_suffix(path, suffix=".jpg")
    ann_paths = [f"data/Watermelon87_Semantic_Seg_Mask/ann_dir/{dir}" for dir in ["train", "val"]]
    for path in ann_paths:
        unify_suffix(path, suffix=".png")
