import os
import sys
import shutil

if len(sys.argv) == 1:
    path = "."
else:
    path = sys.argv[1]
trans_map = {"train": "training", "val": "validation", "test": "testing"}
dirs = os.listdir(path)
ori = dirs[0]
tar = dirs[1]

new_name = "./processed_data"
if os.path.exists(new_name):
    shutil.rmtree(new_name)
os.mkdir(new_name);

for d in os.listdir(os.path.join(path, ori)):
    if not os.path.isdir(os.path.join(path, ori, d)):
        continue
    tar_dic = os.path.join(new_name, trans_map[d])
    if os.path.exists(tar_dic):
        shutil.rmtree(tar_dic)
    print ("mkdir target dictionary: %s" % (d))
    os.mkdir(tar_dic)
    os.mkdir(os.path.join(tar_dic, "images"))
    os.mkdir(os.path.join(tar_dic, "instances"))
    for page in os.listdir(os.path.join(path, ori, d)):
        if not os.path.isdir(os.path.join(path, ori, d, page)):
            continue
        tar_pics = os.listdir(os.path.join(path, tar, d, page));
        for label in os.listdir(os.path.join(path, ori, d, page)):
            splited = label.split("_")
            if splited[-1] != "labelIds.png":
                continue
            tar_name = "_".join(["_".join(splited[0:-2]), "leftImg8bit.png"])
            if tar_name not in tar_pics:
                continue
            print ("find pair of picture %s, moving it ..." % (label))
            shutil.copyfile(os.path.join(path, tar, d, page, tar_name), os.path.join(tar_dic, "images", tar_name))
            shutil.copyfile(os.path.join(path, ori, d, page, label), os.path.join(tar_dic, "instances", label))
