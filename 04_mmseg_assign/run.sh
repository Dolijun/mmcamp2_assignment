#python demo/image_demo.py \
#  data/Watermelon87_Semantic_Seg_Mask/img_dir/val/01bd15599c606aa801201794e1fa30.jpg \
cd /home/ilab/dolijun/Dolijun/Yan1/openmmlab/mmsegmentation

#python tools/train.py data/pspnet_r50-d8_4xb2-40k_watermelon87.py --work-dir data/outputs

#python tools/test.py data/pspnet_r50-d8_4xb2-40k_watermelon87.py \
# data/outputs/iter_4000.pth \
# --work-dir  data/outputs




#python demo/image_demo.py data/input_img.jpg \
# data/pspnet_r50-d8_4xb2-40k_watermelon87.py \
# data/outputs/iter_4000.pth \
# --out-file data/predict.jpg \
# --opacity 0.5


python demo/video_demo.py data/video_watermelon.webm \
 data/pspnet_r50-d8_4xb2-40k_watermelon87.py \
 data/outputs/iter_4000.pth \
 --device cuda:0 \
--output-file data/predict_2.mp4 \
--output-fourcc "MJPG" \
--output-fps 24 \
--opacity 0.7
