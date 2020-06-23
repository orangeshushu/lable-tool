import os
import csv
import numpy as np
filepath=".\html"
namelist = os.listdir(filepath).sort(key=lambda x:int(x[:1]))
print(namelist)
# for username in namelist:
#     # oder_path = username.split("-")[0]
#     # print(oder_path)
#     # username_path = filepath + "\\" + username
#     print(username)