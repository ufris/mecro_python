from datetime import datetime as dt
from datetime import timedelta as td
import os, csv
import pandas as pd

def roundTime(cal_dt=None, roundTo=60):
   """Round a datetime object to any time lapse in seconds
   dt : datetime.datetime object, default now.
   roundTo : Closest number of seconds to round to, default 1 minute.
   Author: Thierry Husson 2012 - Use it as you want but don't blame me.
   """
   if cal_dt == None : cal_dt = dt.now()
   seconds = (cal_dt.replace(tzinfo=None) - cal_dt.min).seconds
   rounding = (seconds+roundTo/2) // roundTo * roundTo
   return cal_dt + td(0,rounding-seconds,-cal_dt.microsecond)

path = '/home/Downloads/GNAH nonT ICH 통계_20210728.csv'
sorting_save_path = '/home/Downloads/GNAH nonT ICH 통계_20210728_sort.csv'
save_output_path = '/home/Downloads/GNAH nonT ICH 통계_20210728_inspection_time.csv'

# sorting with pandas using groupby
content = pd.read_csv(path)
content['date'] = content["시행일"].astype(str) + content["시행시간"].astype(str).str.zfill(4)
group_content = content.sort_values(['등록번호'], ascending=True).groupby(['등록번호'], sort=False).apply(lambda x: x.sort_values(['date'], ascending=True)).reset_index(drop=True)
group_content.to_csv(sorting_save_path, encoding='utf-8', index=False)

study_dic = {}
save_list = []
with open(sorting_save_path, 'r', encoding='utf-8') as r:
    rdr = csv.reader(r)

    for line in rdr:
        if line[0] == '등록번호':
            continue
        study_name = line[0]
        # study_hour = 0 if int(line[4][2:]) <= 30 else 60
        fix_minute = line[4].zfill(4)
        # fix_minute = 00 if line[4][2:] == '' else int(line[4][2:])
        study_time = [line[3][:4], line[3][4:6], line[3][6:], fix_minute[:2], fix_minute[2:]]
        study_time = [int(i) for i in study_time]

        if line[0] in study_dic.keys():
            study_dic[study_name].append(study_time)
        else:
            study_dic[study_name] = [study_time]
        one_row = [line[i] for i in range(7)]
        save_list.append(one_row)

print(study_dic)
compare_list = []
start_study_name = '10002849'
for one_study in study_dic:
    study_content = study_dic[one_study]
    for i in range(len(study_content)):
        if i == 0:
            compare_list.append('-')
            continue
        past_time = study_content[i-1]
        current_time = study_content[i]

        # ex : dt(2021, 8,     21,  16,   50,     1)
        #      dt(year, month, day, hour, minute, second)
        past_time = dt(past_time[0],past_time[1],past_time[2],past_time[3],past_time[4],0)
        # print(one_study, current_time[0],current_time[1],current_time[2],current_time[3],current_time[4])
        current_time = dt(current_time[0],current_time[1],current_time[2],current_time[3],current_time[4], 0)

        past_time = roundTime(past_time, 60*60)
        current_time = roundTime(current_time, 60 * 60)
        print(past_time)
        print(current_time)

        time_distance = current_time - past_time
        print(time_distance)
        days = time_distance.days
        seconds = time_distance.seconds

        hours = seconds//3600
        minutes = (seconds//60)%60
        only_seconds = (seconds - (minutes * 60))

        hour_distance = days * 24 + hours

        # print("days:", days, "hours:", hours, "minutes:", minutes, "seconds:", only_seconds)

        compare_list.append(hour_distance)

print(compare_list)

[save_list[i].append(str(compare_list[i])) for i in range(len(save_list))]
print(save_list)

f = open(save_output_path, 'w', encoding='utf-8', newline='')
wr = csv.writer(f)
for i in save_list:
    wr.writerow(i)
f.close()
