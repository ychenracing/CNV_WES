#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

wes_samples_folder_path = '/home/chen/CNV/wes_samples/Whole_exome_but1120'
output_folder = '/home/chen/CNV/CNVnator/wes'
cnvnator_path = '/home/chen/Desktop/CNVnator_v0.3/src'
hg19_chr_path = '/home/chen/CNV/CNVnator/hg19/Sequence/Chromosomes'


def generate_cnvnator_shell(case_path, output_path):
    if not os.path.exists(output_path):
        os.mkdir(output_path)
    sample_name = output_path[-7:]
    with open(os.path.join(output_path[:-7], 'wes_cnvnator.sh'), 'a+') as fw:
        fw.write(cnvnator_path + ' -root ' + os.path.join(output_path, sample_name) +
                 '.root -chrom 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 X Y -tree ' + case_path + '\n')
        fw.write(cnvnator_path + ' -root ' + os.path.join(output_path, sample_name) +
                 '.root -chrom 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 X Y -d ' + hg19_chr_path + ' -his 100\n')
        fw.write(cnvnator_path + ' -root ' + os.path.join(output_path, sample_name) +
                 '.root -stat 100\n')
        fw.write(cnvnator_path + ' -root ' + os.path.join(output_path, sample_name) +
                 '.root -partition 100\n')
        fw.write(cnvnator_path + ' -root ' + os.path.join(output_path, sample_name) +
                 '.root -chrom 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 X Y -call 100\n')


if __name__ == '__main__':
    files = os.listdir(wes_samples_folder_path)
    for file_item in files:
        if file_item.endswith('bam'):
            if 'NA19152' not in file_item and 'mapped' in file_item:
                sample_name = file_item[:file_item.index('.')]
                generate_cnvnator_shell(os.path.join(wes_samples_folder_path, file_item),
                                        os.path.join(output_folder, sample_name))
