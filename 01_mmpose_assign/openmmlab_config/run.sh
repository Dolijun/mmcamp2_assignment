PYTHON="/home/ilab/software/anaconda3/envs/openmmlab/bin/python"
cd /home/ilab/dolijunc/project/mmpose
${PYTHON} tools/train.py data/Ear210_Keypoint_Dataset_coco/openmmlab_config/rtmpose-s-ear.py
${PYTHON} tools/test.py data/Ear210_Keypoint_Dataset_coco/openmmlab_config/rtmpose-s-ear.py  work_dirs/rtmpose-s-ear/best_PCK_epoch_260.pth
${PYTHON} demo/topdown_demo_with_mmdet.py  \
          data/Ear210_Keypoint_Dataset_coco/openmmlab_config/rtmdet_tiny_ear.py \
          ../mmdetection/work_dirs/rtmdet_tiny_ear/best_coco_bbox_mAP_epoch_165.pth \
          data/Ear210_Keypoint_Dataset_coco/openmmlab_config/rtmpose-s-ear.py \
          work_dirs/rtmpose-s-ear/20230603_200120/epoch_300.pth \
          --input data/Ear210_Keypoint_Dataset_coco/openmmlab_config/myEar0.jpg \
          --output-root data/out \
          --device cuda:0 \
          --bbox-thr 0.5 \
          --kpt-thr 0.5 \
          --nms-thr 0.5 \
          --radius 6 \
          --thickness 3 \
          --draw-bbox \
          --draw-heatmap \
          --show-kpt-idx


cd /home/ilab/dolijunc/project/mmdetection
${PYTHON} tools/train.py data/Ear210_Keypoint_Dataset_coco/openmmlab_config/rtmdet_tiny_ear.py
${PYTHON} tools/test.py data/Ear210_Keypoint_Dataset_coco/openmmlab_config/rtmdet_tiny_ear.py  work_dirs/rtmdet_tiny_ear/best_coco_bbox_mAP_epoch_165.pth
${PYTHON} demo/image_demo.py data/Ear210_Keypoint_Dataset_coco/openmmlab_config/myEar0.jpg \
          data/Ear210_Keypoint_Dataset_coco/openmmlab_config/rtmdet_tiny_ear.py \
          --weights work_dirs/rtmdet_tiny_ear/best_coco_bbox_mAP_epoch_165.pth \
          --device cuda:0 \
          --pred-score-thr 0.5 \
          --out-dir data/out
