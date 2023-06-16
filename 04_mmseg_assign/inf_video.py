import torch
from mmseg.apis import init_model, inference_model
from mmseg.datasets import cityscapes
from mmengine.model.utils import revert_sync_batchnorm
from mmengine import ProgressBar
import mmcv
from PIL import Image
import numpy as np
import shutil
import time
import os


def predict_single_frame(model, img, palette, opacity=0.2):
    result = inference_model(model, img)

    seg_map = np.array(result.pred_sem_seg.data[0].detach().cpu().numpy()).astype('uint8')
    seg_map = Image.fromarray(seg_map).convert("P")
    seg_map.putpalette(np.array(palette, dtype="uint8"))

    show_img = np.array(seg_map.convert("RGB")) * (1 - opacity) + img * opacity

    return show_img


def predict_video(model, video_path, palette, temp_dir=None, out_file=None):
    imgs = mmcv.VideoReader(video_path)
    pgb = ProgressBar(len(imgs))
    out_dir = os.path.dirname(out_file)
    if temp_dir is None:
        temp_dir = os.path.join(out_dir, "temp_dir")
        assert not os.path.exists(temp_dir), "please clarity the temp_dir"
        os.makedirs(temp_dir)

    for frame_id, img in enumerate(imgs):
        show_img = predict_single_frame(model, img, palette)
        out_frame = f"{temp_dir}/{frame_id:06d}.jpg"
        mmcv.imwrite(show_img, out_frame)

        pgb.update()

    mmcv.frames2video(temp_dir, out_file, fps=imgs.fps, fourcc="mp4v")

    shutil.rmtree(temp_dir)
    print(f"删除临时文件夹{temp_dir}")


if __name__ == '__main__':
    config_path = os.environ["CONFIG"]
    checkpoint = os.environ["CKPT"]
    video_path = os.environ["VIDEO"]

    model = init_model(config_path, checkpoint, device="cuda:0")
    if not torch.cuda.is_available():
        model = revert_sync_batchnorm(model)

    # 从cityscapes 获取类别和类别可视化颜色
    classes = cityscapes.CityscapesDataset.METAINFO["classes"]
    palette = cityscapes.CityscapesDataset.METAINFO["palette"]

    time_ = time.strftime("%Y%m%d%H%M%S")
    predict_video(model, video_path, palette=palette, out_file=os.path.join("outputs", time_, "out_video.mp4"))
