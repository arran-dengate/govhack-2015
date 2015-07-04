"""
Dupe not only the image but hack the csv file so that it has an extra field for the generated data.
"""
import shutil
import os
import csv

def writeToFile(fn, lines):
    #if len(lines) > 1000:
    #    lines = lines[0:1000]
    with open(fn, 'w') as f:
        f.writelines(lines)

base_path = "/Users/rdengate/Desktop/govhack_2015/govhack-2015/nationalmap/wwwroot"
#csv_base_path = os.path.join(base_path, "abc_photojournalism.csv")
csv_base_path = os.path.join(base_path, "abc_photojournalism.csv")
csv_with_billboards = os.path.join(base_path, "abc_photojournalism_cp.csv")
done_csv_nsw = os.path.join(base_path, "abc_photojournalism_nsw.csv")
done_csv_act = os.path.join(base_path, "abc_photojournalism_act.csv")
done_csv_nt = os.path.join(base_path, "abc_photojournalism_nt.csv")
done_csv_sa = os.path.join(base_path, "abc_photojournalism_sa.csv")
done_csv_wa = os.path.join(base_path, "abc_photojournalism_wa.csv")
done_csv_tas = os.path.join(base_path, "abc_photojournalism_tas.csv")

shutil.copy(csv_base_path, csv_with_billboards)

max_lines = 1000;

nsw_lines = []
act_lines = []
nt_lines = []
sa_lines = []
wa_lines = []
tas_lines = []

with open(csv_with_billboards, 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')

    i = 0
    for row in spamreader:
        state = row[8].strip()
        if state == "":
            i = i + 1
            continue
        if i==0:
            nsw_lines.append(",".join(row) + ",Billboards\n")
            act_lines.append(",".join(row) + ",Billboards\n")
            nt_lines.append(",".join(row) + ",Billboards\n")
            sa_lines.append(",".join(row) + ",Billboards\n")
            wa_lines.append(",".join(row) + ",Billboards\n")
            tas_lines.append(",".join(row) + ",Billboards\n")
            i = i + 1
            continue
        row_end = ',"images/%s.png"\n' % str(i-1).zfill(4)
        if state == "NSW":
            nsw_lines.append(",".join(row) + row_end)
            continue
        if state == "ACT":
            act_lines.append(",".join(row) + row_end)
            continue
        if state == "NT":
            nt_lines.append(",".join(row) + row_end)
            continue
        if state == "SA":
            sa_lines.append(",".join(row) + row_end)
            continue
        if state == "WA":
            wa_lines.append(",".join(row) + row_end)
            continue
        if state == "TAS":
            tas_lines.append(",".join(row) + row_end)
            continue
        i = i + 1

print("NSW: " + str(len(nsw_lines)))
print("ACT: " + str(len(act_lines)))
print("NT: " + str(len(nt_lines)))
print("SA: " + str(len(sa_lines)))
print("WA: " + str(len(wa_lines)))
print("TAS: " + str(len(tas_lines)))

writeToFile(done_csv_nsw, nsw_lines)
writeToFile(done_csv_act, act_lines)
writeToFile(done_csv_nt, nt_lines)
writeToFile(done_csv_sa, sa_lines)
writeToFile(done_csv_wa, wa_lines)
writeToFile(done_csv_tas, tas_lines)




#for i in range(len(new_lines)):
#    n = str(i)
#    shutil.copy(os.path.join(base_path, "images/red_square.png"), 
#                os.path.join(base_path, "images/test_word_cloud_%s.png" % n.zfill(4))) 
#    i = i + 1

