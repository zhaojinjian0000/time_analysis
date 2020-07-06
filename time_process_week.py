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
    optParser = OptionParser(usage="%prog [-d] [-o]", version="%prog 1.0",
                             description="A time processing tools for IDP learning")
    optParser.add_option('-d', '--input_dir', action='store', type="string",
                         dest='input_dir',
                         help='path to the time_list dir')
    optParser.add_option('-o', '--output_dir', action='store', type="string", dest='output_dir',
                         default='./week_result/',
                         help='path to store the output files')
    optParser.add_option('-t', '--tmp_dir', action='store', type="string", dest='temp_dir',
                          default='./tmp_file/',
                         help='path to the tmp dir, which is used to store the preprocessing files')

    (tmp_args, _) = optParser.parse_args()
    if tmp_args.input_dir and tmp_args.output_dir:
        return tmp_args
    else:
        optParser.parse_args(['-h'])
        exit()


if __name__ == '__main__':
    try:
        args=get_args()
        check_path(args.temp_dir)
        check_path(args.output_dir)
        input_sg = args.input_dir.split('/')[-2]
        table_1_sg = write_table_1(input_dir=args.input_dir, tmp_dir=args.temp_dir)

        table_1 = pd.read_csv(table_1_sg)
        a = list(range(6, 25, 1))
        a = [str(i) for i in a]
        fig = plt.figure(figsize=(12, 6))
        plt.boxplot(table_1[a].T,
                    notch=False,  # box instead of notch shape
                    sym='bo',
                    vert=True)  # vertical box aligmnent

        x = np.arange(1, 20, 1)  # x坐标
        plt.plot(x, np.mean(table_1[a]),
                 lw=3, c='lightblue',
                 marker='o',
                 ms=4,
                 label='mean')
        plt.xticks(list(range(1, 20, 1)), a)
        plt.ylim(-10, 110)
        plt.xlabel('time')
        plt.ylabel('energy')
        plt.legend()
        plt.title(input_sg + '_box_plot', fontsize=20)
        plt.grid()
        plt.savefig(args.output_dir + input_sg + '_box_plot.png')
        print(args.output_dir + input_sg + '_box_plot.png has been saved......')

        table_3_sg = write_table3(input_dir=args.input_dir,
                                  tmp_dir=args.temp_dir)
        table_3 = pd.read_csv(table_3_sg)
        ind = range(len(table_3))
        plt.figure(figsize=(8, 6))
        plt.xticks(ind, table_3['date'])
        plt.ylabel('min')
        sa = []
        sab = []
        sabc = []
        for i in range(0, len(table_3)):
            sum1 = table_3['S'][i] + table_3['A'][i]
            sa.append(sum1)
            sum2 = sum1 + table_3['B'][i]
            sab.append(sum2)
            sum3 = sum2 + table_3['C'][i]
            sabc.append(sum3)

        width = 0.4  # 设置条形图一个长条的宽度
        p1 = plt.bar(ind, table_3['S'], width, color='lightblue')
        p2 = plt.bar(ind, table_3['A'], width, bottom=table_3['S'], color='lightgreen')  # 在p1的基础上绘制，底部数据就是p1的数据
        p3 = plt.bar(ind, table_3['B'], width, bottom=sa, color='gray')
        p4 = plt.bar(ind, table_3['C'], width, bottom=sab, color='lightyellow')
        p5 = plt.bar(ind, table_3['R'], width, bottom=sabc, color='pink')

        plt.legend((p1[0], p2[0], p3[0], p4[0], p5[0]),
                   ('S', 'A', 'B', 'C', 'R'), )
        plt.title(input_sg + '_time_matrix_bar_plot', fontsize=20)
        plt.legend()
        plt.savefig(args.output_dir + input_sg + '_time_matrix_bar_plot.png')
        print(args.output_dir + input_sg + '_time_matrix_bar_plot.png has been saved......')

        plt.figure()
        plt.title(input_sg + '_week_time_matrix_pie_chart')
        plt.axis('equal')  # 保证长宽相等
        plt.pie([np.sum(table_3['S']),
                 np.sum(table_3['A']),
                 np.sum(table_3['B']),
                 np.sum(table_3['C']),
                 np.sum(table_3['R'])],
                labels=['S', 'A', 'B', 'C', 'R'],
                shadow=True,
                autopct='%1.2f%%', )
        # plt.savefig(input_sg+'-time_matrix_pie_chart.png')
        plt.savefig(args.output_dir + input_sg + '_week_time_matrix_pie_chart.png')
        print(args.output_dir + input_sg + '_week_time_matrix_pie_chart.png has been saved......')


        table_4 = generate_table4(table_3)
        ind = range(len(table_4))
        plt.figure(figsize=(12, 6))
        plt.xticks(ind, table_3['date'])
        plt.ylabel('%')
        sa = []
        sab = []
        sabc = []
        for i in range(0, len(table_4)):
            sum1 = table_4['S'][i] + table_4['A'][i]
            sa.append(sum1)
            sum2 = sum1 + table_4['B'][i]
            sab.append(sum2)
            sum3 = sum2 + table_4['C'][i]
            sabc.append(sum3)

        width = 0.4  # 设置条形图一个长条的宽度
        p1 = plt.bar(ind, table_4['S'], width, color='lightblue')
        p2 = plt.bar(ind, table_4['A'], width, bottom=table_4['S'], color='lightgreen')  # 在p1的基础上绘制，底部数据就是p1的数据
        p3 = plt.bar(ind, table_4['B'], width, bottom=sa, color='gray')
        p4 = plt.bar(ind, table_4['C'], width, bottom=sab, color='lightyellow')
        p5 = plt.bar(ind, table_4['R'], width, bottom=sabc, color='pink')

        plt.legend((p1[0], p2[0], p3[0], p4[0], p5[0]),
                   ('S', 'A', 'B', 'C', 'R'), )
        plt.title(input_sg + '_time_matrix_hist_plot', fontsize=20)
        plt.savefig(args.output_dir + input_sg + '_time_matrix_hist_plot.png')
        print(args.output_dir + input_sg + '_time_matrix_hist_plot.png has been saved......')

        shutil.rmtree(args.temp_dir)
    except Exception as e:
        print(e)








