import os
import shutil

env_dic = os.environ

IMG_PATH = env_dic["LOCALAPPDATA"] + "/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets/"

for i in os.listdir(IMG_PATH):
    shutil.copyfile(IMG_PATH + i, i + ".jpg")
