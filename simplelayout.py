#!/usr/bin/python
# -*- coding: UTF-8 -*-


import os
import sys
import argparse


def create_args():
    parser = argparse.ArgumentParser() #创建实例对象
    parser.add_argument('--board_grid', default=100, type=int,
                        help='布局板分辨率，代表矩形区域的边长像素数')
    parser.add_argument('--unit_grid', default=10, type=int,
                        help='矩形组件分辨率,能被布局板分辨率整除')
    parser.add_argument('--unit_n', default=3, type=int,
                        help='组件数量')
    parser.add_argument('--positions', nargs='*', type=int,
                        help='组件位置')
    parser.add_argument('-o', '--outdir', default='example_dir', type=str,
                        help='输出结果的目录， 若目录不存在程序会自行创建')
    parser.add_argument('--file_name', default='example', type=str,
                        help='输出文件名（不包括文件类型后缀）')
    args = parser.parse_args() # 解析

    return args


def check_args(args):
    """参数检查 """
    if (args.board_grid % args.unit_grid) != 0:
        print('布局板分辨率不能整除组件分辨率！')
        sys.exit(1)

    if len(args.positions) != args.unit_n:
        print('组件位置与数量不一致！')
        sys.exit(1)

    n_limit = (args.board_grid // args.unit_grid) ** 2
    if min(args.positions) < 1 or max(args.positions) > n_limit:
        print('组件位置编号不在规定范围内！')
        sys.exit(1)
    

def main():
    args = create_args()
    check_args(args)

    # 检查路径是否存在，不存在则创建
    outdir = args.outdir.rstrip('/').rstrip('\\')
    if not os.path.exists(outdir):
        os.makedirs(outdir)
    
    # 判断文件是否存在，不存在则创建
    file_types = ['mat', 'jpg']
    for file_type in file_types:
        file_path = '{outdir}/{fname}.{ftype}'.format(
                    outdir=outdir, fname=args.file_name, ftype=file_type)
        if not os.path.exists(file_path):
            os.mknod(file_path)


if __name__ == "__main__":
    main()
