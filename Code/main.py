import os
import shutil


lis = os.listdir(r'E:\SME\SME-数据\大创-点云\论文\2019')
l = []
for file in lis:
    if file.find('point') != -1:
        l.append(file)
        shutil.move(r"E:\SME\SME-数据\大创-点云\论文\2019" + '\\' + file,
                    r'E:\SME\SME-数据\大创-点云\论文\CVPR2019' + '\\' + file.split('\\')[-1])
for i in l:
    print(i)
