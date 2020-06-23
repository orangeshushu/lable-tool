# gather all the branch result into one result file
import os
import csv
filepath = "./label_data/"
all_file = os.listdir(filepath)
# print(all_file)
res_username = []

mid_content = []
save_file_path = ""

with open('label_reslut.csv', 'w',encoding='utf-8') as csv_write:
    csv_write = csv.writer(csv_write)
    for file in all_file:
        username = file.split(".")[0][1:]
        with open("label_data/{filepath}".format(filepath=file), "r", encoding="utf-8") as f:
            file_content = csv.reader(f)
            column = [row for row in file_content]
            print(column[1])
            print(type(column[1]))
            content = column[1].append(username)
            print(content)
            csv_write.writerow(column[1])
            # for each_content in file_content:
            #     print(each_content)
                # break
                # write_content =
                # csv_write.writerow(each_content[1].append(username))

        # csv_write.writerow((str(username),))


