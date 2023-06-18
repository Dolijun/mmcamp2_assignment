import mmcv
import cv2
from PIL import Image
from mmengine import Config
from mmagic.registry import MODELS
from mmagic.utils import register_all_modules
register_all_modules()



if __name__ == '__main__':
    img_path = "data/demo.jpg"

    img = mmcv.imread(img_path)
    img_canny = cv2.Canny(img,150, 200)
    img_canny_path = img_path.split(".")[0] + "_canny.jpg"
    print(img_canny_path)
    mmcv.imwrite(img_canny, img_canny_path)
    print(img_canny.shape)
    img_canny = img_canny[:,:,None]
    img_canny = cv2.cvtColor(img_canny, cv2.COLOR_GRAY2RGB)
    print("RGB", img_canny.shape)
    img_canny = Image.fromarray(img_canny)

    prompt = "Room with European style and the morden style of wood furniture"
    config_path = "configs/controlnet/controlnet-canny.py"
    cfg = Config.fromfile(config_path)
    controlnet_canny = MODELS.build(cfg.model).cuda()

    output_dict = controlnet_canny.infer(prompt, control=img_canny)
    print(output_dict.keys())
    for idx, sample in enumerate(output_dict["samples"]):
        sample.save(f"data/sample_{idx:>06}.png")
    for idx, ctrol in enumerate(output_dict["controls"]):
        ctrol.save(f"data/ctrol_{idx:>06d}.png")
