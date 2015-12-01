#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

'''
    Generate cnvnator running script on Baylor for wes data.
'''

wes_samples_folder_path = '/stornext/snfs5/ruichen/dmhg/fgi/wangfei/wes_samples'
rootsys_path = '/stornext/snfs5/ruichen/dmhg/fgi/lily/software/root'
cnvnator_path = '/stornext/snfs5/ruichen/dmhg/fgi/lily/software/CNVnator_v0.2.7/src'
hg19_chr_path = '/stornext/snfs5/ruichen/dmhg/fgi/lily/Proteomics/database/Human/Homo_sapiens/UCSC/hg19/Sequence/Chromosomes'
workdir_path = '/stornext/snfs5/ruichen/dmhg/fgi/lily/CNV/CNVnator/ychen/wes'


def generate_cnvnator_shell(case_path, output_path):
    if not os.path.exists(output_path):
        os.mkdir(output_path)
    sample_name = output_path[-7:]
    with open(os.path.join(output_path[:-7], 'wes_cnvnator.sh'), 'a+') as fw:
        fw.write(cnvnator_path + ' -root ' + os.path.join(output_path, sample_name) + '.root -chrom 1 2 3 4 5 6 7 8 9 10 12 13 14 15 16 17 18 19 21 22 X -tree ' + case_path + '\n')
        fw.write(cnvnator_path + ' -root ' + os.path.join(output_path, sample_name) + '.root -chrom 1 2 3 4 5 6 7 8 9 10 12 13 14 15 16 17 18 19 21 22 X -d ' + hg19_chr_path + ' -his 100\n')
        fw.write(cnvnator_path + ' -root ' + os.path.join(output_path, sample_name) + '.root -stat 100\n')
        fw.write(cnvnator_path + ' -root ' + os.path.join(output_path, sample_name) + '.root -partition 100\n')
        fw.write(cnvnator_path + ' -root ' + os.path.join(output_path, sample_name) + '.root -chrom 1 2 3 4 5 6 7 8 9 10 12 13 14 15 16 17 18 19 21 22 X -call 100\n')


if __name__ == '__main__':
    files = os.listdir(wes_samples_folder_path)
    for fileitem in files:
        if fileitem.endswith('bam'):
            if 'NA19152' not in fileitem and 'mapped' in fileitem:
                sample_name = fileitem[:fileitem.index('.')]
                generate_cnvnator_shell(os.path.join(wes_samples_folder_path, fileitem), os.path.join(workdir_path, sample_name))
