cd /home/ilab/dolijunc/project/mmpretrain
mim train mmpretrain my_configs/resnet50_ft.py --work-dir=./my_configs/out_0
mim test mmpretrain my_configs/resnet50_ft.py --work-dir=./my_configs/out_0_val -C my_configs/out_0/epoch_10.pth
