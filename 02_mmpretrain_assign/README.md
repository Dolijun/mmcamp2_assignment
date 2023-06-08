# 第二次作业说明

## 文件列表
```shell
.
├── out_0                           # 训练日志
│   ├── 20230608_004355
│   │   ├── 20230608_004355.log
│   │   └── vis_data
│   │   ├── 20230608_004355.json
│   │   ├── config.py
│   │   └── scalars.json
│   ├── last_checkpoint
│   └── resnet50_ft.py
├── out_0_val                       # 测试日志
│   ├── 20230608_094158
│   │   ├── 20230608_094158.json
│   │   ├── 20230608_094158.log
│   │   └── vis_data
│   │   └── config.py
│   └── resnet50_ft.py
├── resnet50_ft.py                  # 配置文件
├── run.sh                          # 运行脚本
└── split_datasets.py               # 数据集划分

6 directories, 13 files
```

## 验证集评估指标

```shell
2023/06/08 09:42:02 - mmengine - INFO - Load checkpoint from my_configs/out_0/epoch_10.pth
2023/06/08 09:42:05 - mmengine - INFO - Epoch(test) [100/108]    eta: 0:00:00  time: 0.0147  data_time: 0.0002  memory: 182  
2023/06/08 09:42:05 - mmengine - INFO - Epoch(test) [108/108]    accuracy/top1: 93.7355  accuracy/top5: 99.1879  data_time: 0.0014  time: 0.0228
```

## 推理结果

![image](./apple_res.png)
