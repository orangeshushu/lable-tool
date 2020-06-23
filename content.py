import os
import csv
import numpy as np
import numpy as np
filepath=".\clean_data"
namelist = os.listdir(filepath)
# print(namelist)
for username in namelist:
    username_path = filepath + "\\" + username
    with open(username_path, "r", encoding="UTF-8") as csvfile:
        reader = csv.reader(csvfile)
        # print(reader)
        rows = [row for row in reader]
    # print(rows)
for content in rows[4:]:
    print(content)
