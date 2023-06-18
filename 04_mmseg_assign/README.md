## 提交文件结构
``` shell
.
├── 20230616_220241                 # 训练日志
│   ├── 20230616_220241.log
│   └── vis_data
│       ├── 20230616_220241.json
│       ├── config.py
│       └── scalars.json
├── 20230616_222113                 # 测试日志
│   ├── 20230616_222113.json
│   ├── 20230616_222113.log
│   └── vis_data
│       └── config.py
├── DubaiDataset_pipeline.py
├── inf_video.py
├── input_img.jpg                     # 预测原图
├── predict_2.avi                     # 测试视频结果
├── predict_2.mp4                     # 测试视频结果
├── predict.jpg
├── pspnet_dubaidataset.py
├── pspnet_r50-d8_4xb2-40k_DubaiDataset_1.py
├── pspnet_r50-d8_4xb2-40k_DubaiDataset.py
├── pspnet_r50-d8_4xb2-40k_watermelon87.py    # 配置文件
├── run.sh                                    # 运行脚本
├── street_20220330_174028.mp4
├── test_watermelon.py
├── train_dubai.py
├── unisuffix.py
├── video_1.mp4
├── video_watermelon.webm                     # 输入视频
└── visual_dataset.py   

```
## 测试结果
```shell
2023/06/16 22:21:24 - mmengine - INFO - 
+------------+-------+-------+
|   Class    |  IoU  |  Acc  |
+------------+-------+-------+
| Unlabeled  | 96.35 | 97.45 |
|    red     | 94.17 | 98.27 |
|   green    | 93.33 | 95.55 |
|   white    | 84.78 | 93.73 |
| seed-black | 75.63 | 81.99 |
| seed-white | 58.54 | 63.75 |
+------------+-------+-------+
2023/06/16 22:21:24 - mmengine - INFO - Iter(test) [17/17]    aAcc: 97.0800  mIoU: 83.8000
```
## 图片
![image](./input_img.jpg)
![image](./predict.jpg)

## 视频
https://github.com/Dolijun/mmcamp2_assignment/blob/main/04_mmseg_assign/predict_2.avi

