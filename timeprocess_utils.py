# -*- coding: utf-8 -*-
"""
 @File: timelist_processing - timeprocess_utils
 
 @Time: 2020/5/15 5:54 PM
 
 @Author: lotuswang
 
 
"""

import os
import datetime
import numpy as np
import pandas as pd
from pathlib import Path
import csv

def check_path(my_path):
    my_file = Path(str(my_path))
    my_path=str(my_path)
    if not os.path.exists(my_file):
        try:
            os.makedirs(my_path)
        except Exception as e:
            raise FileNotFoundError('！！！[Error] make dir ' + my_path + e)


def time_trans(in_date, in_time):
    in_time = in_time.replace('：',':')
    year = int(in_date[:4])
    month = int(in_date[4:6])
    day = int(in_date[-2:])
    hour = int(in_time.split(':')[0])
    minute = int(in_time.split(':')[1])
    return datetime.datetime(year,month,day,hour,minute,0,0)


def caulculate_duration(in_date, start, end):
    if type(start)!=datetime.datetime:
        start = time_trans(in_date, start)
    if type(end)!=datetime.datetime:
        end = time_trans(in_date, end)
    return int((end-start).seconds/60)


def generate_duration(input_fn, input_df):
    dur_list = []
    in_date = input_fn.split('/')[-1][:8]
    for start, end in zip(input_df['start'], input_df['end']):
        start = str(start)
        end = str(end)
        dur_list.append(caulculate_duration(in_date, start, end))
    input_df['duration'] = dur_list
    return input_df


def get_efficient_ratio(timelist_df):
    efficient_index=['high','middle','low']
    high = np.sum(timelist_df.query('效能=="高"')['duration'])
    middle = np.sum(timelist_df.query('效能=="中"')['duration'])
    low = np.sum(timelist_df.query('效能=="低"')['duration'])
    # print(high,middle,low)
    result = pd.Series([high, middle, low], index=efficient_index,
                  )
    return result


def get_timematrix_ratio(timelist_df):
    timematrix_index = ['A', 'S', 'B', 'C', 'R']
    try:
        a = np.sum(timelist_df.query('时间矩阵=="使用"')['duration'])
    except Exception as e:
        a = 0
    try:
        s = np.sum(timelist_df.query('时间矩阵=="投资"')['duration'])
    except Exception as e:
        s = 0
    try:
        b = np.sum(timelist_df.query('时间矩阵=="浪费"')['duration'])
    except Exception as e:
        b = 0
    try:
        c = np.sum(timelist_df.query('时间矩阵=="闲耗"')['duration'])
    except Exception as e:
        c = 0
    try:
        r = np.sum(timelist_df.query('时间矩阵=="休息"')['duration'])
    except Exception as e:
        r = 0
    result = pd.Series([a, s, b, c, r], index=timematrix_index, )
    return result


def handel_line(start, end, duration, in_date='20200411'):
    start = start.replace('：', ':')
    end = end.replace('：', ':')

    a = int(start.split(':')[0])
    b = int(end.split(':')[0])
    cycle_time = b - a
    if cycle_time == 1:
        return [start, ], [end, ], [duration, ], [a, ]
    else:
        start_list = []
        end_list = []
        dur_list = []
        tag_list = []
        tmp_start = start
        for i in range(cycle_time):
            tag_list.append(a + i)
            start_list.append(tmp_start)
            tmp_end = str(a + i + 1) + ':00'
            end_list.append(tmp_end)
            dur_list.append(caulculate_duration(in_date,
                                                tmp_start,
                                                tmp_end))
            tmp_start = tmp_end
        tag_list.append(b)
        start_list.append(tmp_start)
        end_list.append(end)
        dur_list.append(caulculate_duration(in_date, tmp_start, end))
        return start_list, end_list, dur_list, tag_list


def handle_input_df(input_df):
    start_list=[]
    end_list=[]
    duration_list=[]
    energy_list = []
    tag_list = []
    for start, end, duration, en1, en2 in zip(input_df['start'],
                                              input_df['end'],
                                              input_df['duration'],
                                              input_df['效能'],
                                              input_df['时间矩阵']):
        tmp_start, tmp_end, tmp_dur, tmp_tag = handel_line(start,
                                                          end,
                                                          duration,)
        if en2=='休息':
            en=50
        elif en1=='高':
            en=100
        elif en1=='中':
            en=70
        else:
            en=30
        tmp_en = [en]*len(tmp_start)
        start_list.extend(tmp_start)
        end_list.extend(tmp_end)
        duration_list.extend(tmp_dur)
        energy_list.extend(tmp_en)
        tag_list.extend(tmp_tag)
    result_df=pd.DataFrame([tag_list,
                            duration_list,
                            energy_list,
                            start_list,
                            end_list],
                           index=['tag','duration','energy','start','end']).T
    return result_df


def handle_tag_df(tag_df):
    t_list = [0] * 19
    d_list = [0.0001] * 19
    for tag, duration, energy in zip(tag_df['tag'],
                                     tag_df['duration'],
                                     tag_df['energy']):
        tag = int(tag) - 6
        t_list[tag] = t_list[tag] + int(duration) * int(energy)
        d_list[tag] = d_list[tag] + int(duration)

    result_list = np.around(np.array(t_list) / np.array(d_list))
    result_list = np.array(result_list, 'int')
    return result_list


#############################
#          for week         #
#############################


def generate_table_1_line(in_date, input_df):
    result_list = [str(in_date)]
    tag_df = handle_input_df(input_df)
    time_div_list = handle_tag_df(tag_df)
    a = [str(i) for i in list(time_div_list)]
    result_list =  result_list+a
    return result_list


def generate_sabcr(timelist_df):
    try:
        a = np.sum(timelist_df.query('时间矩阵=="使用"')['duration'])
    except Exception as e:
        a = 0
    try:
        s = np.sum(timelist_df.query('时间矩阵=="投资"')['duration'])
    except Exception as e:
        s = 0
    try:
        b = np.sum(timelist_df.query('时间矩阵=="浪费"')['duration'])
    except Exception as e:
        b = 0
    try:
        c = np.sum(timelist_df.query('时间矩阵=="闲耗"')['duration'])
    except Exception as e:
        c = 0
    try:
        r = np.sum(timelist_df.query('时间矩阵=="休息"')['duration'])
    except Exception as e:
        r = 0
    total= np.sum(timelist_df['duration'])
    return [int(s), int(a), int(b), int(c), int(r), int(total)]


def generate_table_3_line(in_date, input_df):
    result_list = [str(in_date)]
    sabcr_list = generate_sabcr(input_df)
    a = [str(i) for i in list(sabcr_list)]
    result_list =  result_list+a
    return result_list


def write_table_1(input_dir, tmp_dir ):
    a = list(range(6, 25, 1))
    a = [str(i) for i in a]
    table_1_index = ['date', ] + a
    table_1_list = []
    for input_fn in os.listdir(input_dir):
        if input_fn.endswith('.csv'):
            # print(input_fn)
            input_fn = input_dir + input_fn
            in_date = input_fn.split('/')[-1][:8]
            input_df = pd.read_csv(input_fn)
            index = ['任务编号', '任务', 'start', 'end', '效能', '时间矩阵', ]
            input_df = input_df[index]
            input_df.dropna(inplace=True)
            input_df = generate_duration(input_fn=input_fn,
                                         input_df=input_df)
            table_1_list.append(generate_table_1_line(in_date, input_df))
    input_sg = input_dir.split('/')[-2]
    table_1_sg = tmp_dir + input_sg + '_week_time_energy_series.csv'
    if table_1_list:
        with open(table_1_sg, 'w')as f:
            f_csv = csv.writer(f)
            f_csv.writerow(table_1_index)
            f_csv.writerows(table_1_list)
    return table_1_sg


def write_table3(input_dir, tmp_dir):
    table_3_index = ['date', 'S', 'A', 'B', 'C', 'R', 'total']
    table_3_list = []
    for input_fn in os.listdir(input_dir):
        if input_fn.endswith('.csv'):
            # print(input_fn)
            input_fn = input_dir + input_fn
            in_date = input_fn.split('/')[-1][:8]
            input_df = pd.read_csv(input_fn)
            index = ['任务编号', '任务', 'start', 'end', '效能', '时间矩阵', ]
            input_df = input_df[index]
            input_df.dropna(inplace=True)
            input_df = generate_duration(input_fn=input_fn,
                                         input_df=input_df)
            table_3_list.append(generate_table_3_line(in_date, input_df))
    input_sg = input_dir.split('/')[-2]
    table_3_sg = tmp_dir + input_sg + '_week_time_matrix.csv'
    if table_3_list:
        with open(table_3_sg, 'w')as f:
            f_csv = csv.writer(f)
            f_csv.writerow(table_3_index)
            f_csv.writerows(table_3_list)
    return table_3_sg


def generate_table4(table_3):
    table_4 = pd.DataFrame([np.array(table_3['S'] / table_3['total']) * 100,
                            np.array(table_3['A'] / table_3['total']) * 100,
                            np.array(table_3['B'] / table_3['total']) * 100,
                            np.array(table_3['C'] / table_3['total']) * 100,
                            np.array(table_3['R'] / table_3['total']) * 100, ],
                           index=['S', 'A', 'B', 'C', 'R']).T
    return table_4


