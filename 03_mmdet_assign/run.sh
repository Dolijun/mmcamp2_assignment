cd /home/ilab/dolijun/Dolijun/Yan1/openmmlab/mmdetection

#python tools/train.py my_configs/zj_config.py

#python tools/test.py my_configs/zj_config.py work_dirs/zj_config/best_coco_bbox_mAP_epoch_170.pth
#python demo/image_demo.py --help

#python demo/image_demo.py my_configs/balloon.jpg my_configs/zj_config.py --weights work_dirs/zj_config/best_coco_bbox_mAP_epoch_170.pth --out-dir my_configs/

cd ..
#git clone -b tutorials https://github.com/open-mmlab/mmyolo.git
cd mmyolo
#pip install -e .
python demo/featmap_vis_demo.py \
      ../mmdetection/my_configs/balloon.jpg \
      ../mmdetection/my_configs/zj_config.py \
      ../mmdetection/work_dirs/zj_config/best_coco_bbox_mAP_epoch_170.pth  \
      --target-layers backbone  \
      --channel-reduction squeeze_mean