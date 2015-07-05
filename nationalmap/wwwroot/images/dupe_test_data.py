"""
Dupe not only the image but hack the csv file so that it has an extra field for the generated data.
"""
import shutil
import os
import csv

def writeToFile(fn, lines):
    if len(lines) > 200:
        lines = lines[0:200]
    with open(fn, 'w') as f:
        f.writelines(lines)

base_path = "/Users/rdengate/Desktop/govhack_2015/govhack-2015/nationalmap/wwwroot"
#csv_base_path = os.path.join(base_path, "abc_photojournalism.csv")
csv_base_path = os.path.join(base_path, "words-sanitised-jittered-billboarded-repunctuated.csv")
csv_with_billboards = os.path.join(base_path, "abc_photojournalism_cp.csv")
done_csv_nsw = os.path.join(base_path, "abc_photojournalism_nsw.csv")
done_csv_act = os.path.join(base_path, "abc_photojournalism_act.csv")
done_csv_nt = os.path.join(base_path, "abc_photojournalism_nt.csv")
done_csv_sa = os.path.join(base_path, "abc_photojournalism_sa.csv")
done_csv_wa = os.path.join(base_path, "abc_photojournalism_wa.csv")
done_csv_tas = os.path.join(base_path, "abc_photojournalism_tas.csv")
done_csv_qld = os.path.join(base_path, "abc_photojournalism_qld.csv")
done_csv_vic = os.path.join(base_path, "abc_photojournalism_vic.csv")

done_csv_fire = os.path.join(base_path, "abc_photojournalism_fire.csv")
done_csv_flood = os.path.join(base_path, "abc_photojournalism_flood.csv")
done_csv_drought = os.path.join(base_path, "abc_photojournalism_drought.csv")
done_csv_war = os.path.join(base_path, "abc_photojournalism_war.csv")
done_csv_solar = os.path.join(base_path, "abc_photojournalism_solar.csv")

shutil.copy(csv_base_path, csv_with_billboards)

max_lines = 1000;

nsw_lines = []
act_lines = []
nt_lines = []
sa_lines = []
wa_lines = []
tas_lines = []
qld_lines = []
vic_lines = []

fire_lines = []
flood_lines = []
war_lines = []
drought_lines = []
solar_lines = []

goodlines = []
with open(csv_with_billboards, 'r') as f:
    goodlines = f.readlines()

with open(csv_with_billboards, 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')

    i = 0
    for row, goodline in zip(spamreader, goodlines):
        state = row[8].strip()
        keywords = row[10]
        if state == "":
            i = i + 1
            continue
        if i==0:
            fire_lines.append(goodline)
            flood_lines.append(goodline)
            war_lines.append(goodline)
            drought_lines.append(goodline)
            solar_lines.append(goodline)
            nsw_lines.append(goodline)
            act_lines.append(goodline)
            nt_lines.append(goodline)
            sa_lines.append(goodline)
            wa_lines.append(goodline)
            qld_lines.append(goodline)
            vic_lines.append(goodline)
            tas_lines.append(goodline)
            i = i + 1
            continue
        if keywords.lower().find("war") != -1:
            war_lines.append(goodline)
        if keywords.lower().find("fire") != -1:
            fire_lines.append(goodline)
        if keywords.lower().find("flood") != -1:
            flood_lines.append(goodline)
        if keywords.lower().find("drought") != -1:
            drought_lines.append(goodline)
        if keywords.lower().find("solar") != -1:
            solar_lines.append(goodline)

        if state == "NSW":
            nsw_lines.append(goodline)
            continue
        if state == "ACT":
            act_lines.append(goodline)
            continue
        if state == "NT":
            nt_lines.append(goodline)
            continue
        if state == "SA":
            sa_lines.append(goodline)
            continue
        if state == "WA":
            wa_lines.append(goodline)
            continue
        if state == "TAS":
            tas_lines.append(goodline)
            continue
        if state == "VIC":
            vic_lines.append(goodline)
            continue
        if state == "QLD":
            qld_lines.append(goodline)
        i = i + 1

print("NSW: " + str(len(nsw_lines)))
print("ACT: " + str(len(act_lines)))
print("NT: " + str(len(nt_lines)))
print("SA: " + str(len(sa_lines)))
print("WA: " + str(len(wa_lines)))
print("TAS: " + str(len(tas_lines)))
print("QLD: " + str(len(qld_lines)))
print("VIC: " + str(len(vic_lines)))

print("fire: " + str(len(fire_lines)))
print("war: " + str(len(war_lines)))
print("flood: " + str(len(flood_lines)))
print("drought: " + str(len(drought_lines)))
print("solar: " + str(len(solar_lines)))

writeToFile(done_csv_nsw, nsw_lines)
writeToFile(done_csv_act, act_lines)
writeToFile(done_csv_nt, nt_lines)
writeToFile(done_csv_sa, sa_lines)
writeToFile(done_csv_wa, wa_lines)
writeToFile(done_csv_tas, tas_lines)
writeToFile(done_csv_qld, qld_lines)
writeToFile(done_csv_vic, vic_lines)

writeToFile(done_csv_fire, fire_lines)
writeToFile(done_csv_flood, flood_lines)
writeToFile(done_csv_drought, drought_lines)
writeToFile(done_csv_war, war_lines)
writeToFile(done_csv_solar, solar_lines)


#for i in range(len(new_lines)):
#    n = str(i)
#    shutil.copy(os.path.join(base_path, "images/red_square.png"), 
#                os.path.join(base_path, "images/test_word_cloud_%s.png" % n.zfill(4))) 
#    i = i + 1

