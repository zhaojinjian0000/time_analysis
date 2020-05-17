# -*- coding: utf-8 -*-
"""
 @File: timelist_processing - time_process
 
 @Time: 2020/5/15 5:59 PM
 
 @Author: lotuswang
 
 
"""
import os
import time
import sys
from optparse import OptionParser
from multiprocessing import Pool
import shutil
import numpy as np
import pandas as pd
from timeprocess_utils import *
import matplotlib.pyplot as plt


def get_args():
    optParser = OptionParser(usage="%prog [-i] [-o]", version="%prog 1.0",
                             description="A time processing tools for IDP learning")
    optParser.add_option('-i', '--input_file', action='store', type="string",
                         dest='input_fn',
                         help='path to the time_list.csv')
    optParser.add_option('-o', '--output_dir', action='store', type="string", dest='output_dir',
                         default='./day_result/',
                         help='path to store the output files')
    optParser.add_option('-t', '--tmp_dir', action='store', type="string", dest='temp_dir',
                          default='./tmp_file/',
                         help='path to the tmp dir, which is used to store the preprocessing files')

    (tmp_args, _) = optParser.parse_args()
    if tmp_args.input_fn and tmp_args.output_dir:
        return tmp_args
    else:
        optParser.parse_args(['-h'])
        exit()


if __name__ == '__main__':
    try:
        args=get_args()
        input_sg = args.input_fn.split('/')[-1][:-4]
        in_date = args.input_fn.split('/')[-1][:8]

        check_path(args.temp_dir)
        check_path(args.output_dir)

        input_df = pd.read_csv(args.input_fn)
        index = ['任务编号', '任务', 'start', 'end', '效能', '时间矩阵', ]
        input_df = input_df[index]
        input_df.dropna(inplace=True)

        input_df = generate_duration(input_fn=args.input_fn,
                                     input_df=input_df)
        # input_df.to_csv(args.input_fn, index=False)


        s = get_efficient_ratio(input_df)
        plt.figure()
        plt.title(in_date + ' efficience pie chart')
        plt.axis('equal')  # 保证长宽相等
        plt.pie(s, explode=[0.1, 0, 0],
                labels=s.index,
                shadow=True,
                autopct='%1.2f%%', )
        plt.savefig(args.output_dir+input_sg + '-efficience_pie_chart.png')
        print(args.output_dir+input_sg + '-efficience_pie_chart.png has been saved......')

        m = get_timematrix_ratio(input_df)
        plt.figure()
        plt.title(in_date + ' time matrix pie chart')
        plt.axis('equal')  # 保证长宽相等
        plt.pie(m,
                labels=m.index,
                shadow=True,
                autopct='%1.2f%%', )
        plt.savefig(args.output_dir+input_sg + '-time_matrix_pie_chart.png')
        print(args.output_dir+input_sg + '-time_matrix_pie_chart.png has been saved......')

        tag_df = handle_input_df(input_df)
        time_div_list = handle_tag_df(tag_df)

        x = np.arange(6, 25, 1)  # x坐标
        plt.figure(figsize=(10, 6))
        plt.title(in_date + ' energy trend', fontsize=20)
        plt.plot(x, np.array(time_div_list),
                 lw=3, c='lightblue',
                 marker='o',
                 ms=4,
                 label='Y1')  # 绘制y1
        plt.xticks(x)  # x轴的刻度
        plt.grid()
        plt.xlim(6, 24)  # x轴坐标范围
        plt.ylim(0, 110)  # y轴坐标范围
        plt.xlabel('time')  # x轴标注
        plt.ylabel('energy')  # y轴标注
        # plt.legend()  # 图例
        plt.savefig(args.output_dir+input_sg + '-energy_trend.png')  # 保存图片
        print(args.output_dir+input_sg + '-energy_trend.png has been saved......')
        shutil.rmtree(args.temp_dir)
    except Exception as e:
        print(e)








