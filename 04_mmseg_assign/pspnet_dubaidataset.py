from mmengine import Config

cfg = Config.fromfile("configs/pspnet/pspnet_r50-d8_4xb2-40k_DubaiDataset.py")


# 模型 decode/auxiliary 输出头，指定为类别个数

# 结果保存目录
cfg.work_dir = './work_dirs/watermelon87/v01'

# 训练迭代次数
cfg.train_cfg.max_iters = 4000
# 评估模型间隔
cfg.train_cfg.val_interval = 1000
# 日志记录间隔
cfg.default_hooks.logger.interval = 100
# 模型权重保存间隔
cfg.default_hooks.checkpoint.interval = 1000

# 随机数种子
cfg['randomness'] = dict(seed=0)

