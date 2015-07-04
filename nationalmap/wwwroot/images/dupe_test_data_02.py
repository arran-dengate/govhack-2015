"""
Dupe not only the image but hack the csv file so that it has an extra field for the generated data.
"""
import shutil
import os

base_path = "/Users/rdengate/Desktop/govhack_2015/govhack-2015/nationalmap/wwwroot"
#csv_base_path = os.path.join(base_path, "abc_photojournalism.csv")
csv_base_path = os.path.join(base_path, "abc_datesRemoved.csv")
csv_with_billboards = os.path.join(base_path, "abc_photojournalism_cp.csv")
done_csv = os.path.join(base_path, "abc_photojournalism_bb.csv")

shutil.copy(csv_base_path, csv_with_billboards)

new_lines = []
with open(csv_with_billboards) as f:
    first_line = f.readline();
    new_lines.append(first_line.strip() + ",Billboards\n")

    i = 0
    for line in f.readlines():
        n = str(i)
        line = line.strip() + ',"images/test_word_cloud_%s.png"\n' % n.zfill(4)
        i = i + 1

        new_lines.append(line)

with open(done_csv, 'w') as f:
    f.writelines(new_lines)

for i in range(len(new_lines)):
    n = str(i)
    shutil.copy(os.path.join(base_path, "images/test_word_cloud.png"), 
                os.path.join(base_path, "images/test_word_cloud_%s.png" % n.zfill(4))) 
    i = i + 1

