from pspnet_dubaidataset import cfg
from mmengine.runner import Runner
from mmseg.utils import register_all_modules

register_all_modules(init_default_scope=False)

runner = Runner.from_cfg(cfg)
# runner.train()

cfg["load_from"] = "work_dirs/watermelon87/v01/iter_4000.pth"
runner.test()


