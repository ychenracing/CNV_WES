#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

'''
    run CNVnator on WES data, use NA19152 as control, other samples as case.
'''

samples_path = '/Users/racing/Lab/CNV/WES_samples/Whole_exome_but1120'
output_folder = '/Users/racing/Lab/CNV_WES/CNVnator/output'
head_wrote = False


def generate_wes_cnvnator_shell(case_path, output_path):
    global head_wrote
    if not os.path.exists(output_path):
        os.mkdir(output_path)
    sample_name = output_path[-7:]
    with open(os.path.join(output_path[:-7], 'wes_cnvnator.sh'), 'a+') as fw:
        if not head_wrote:
            fw.write('#!/bin/bash\n')
            fw.write('cd /Applications/root_v5.34.34\n')
            fw.write('. bin/thisroot.sh\n\n\n')
            head_wrote = True
        fw.write('/Users/racing/Lab/CNV/CNVnator/ychen/CNVnator_v0.3/src/cnvnator -root ' +
                  os.path.join(output_path, sample_name) + '.root -chrom 1 4 -tree ' + case_path + '\n')
        fw.write('/Users/racing/Lab/CNV/CNVnator/ychen/CNVnator_v0.3/src/cnvnator -root ' +
                  os.path.join(output_path, sample_name) + '.root -chrom 1 4 -d ' + os.path.join(output_path, 'hg19/Sequence/Chromosomes/') +
                  ' -his 100\n')
        fw.write('/Users/racing/Lab/CNV/CNVnator/ychen/CNVnator_v0.3/src/cnvnator -root ' +
                  os.path.join(output_path, sample_name) + '.root -stat 100\n')
        fw.write('/Users/racing/Lab/CNV/CNVnator/ychen/CNVnator_v0.3/src/cnvnator -root ' +
                  os.path.join(output_path, sample_name) + '.root -partition 100\n')
        fw.write('/Users/racing/Lab/CNV/CNVnator/ychen/CNVnator_v0.3/src/cnvnator -root ' +
                  os.path.join(output_path, sample_name) + '.root -chrom 1 4 -call 100\n')

if __name__ == '__main__':
    files = os.listdir(samples_path)
    for fileitem in files:
        if fileitem.endswith('bam'):
            if 'NA19152' not in fileitem and 'mapped' in fileitem:
                sample_name = fileitem[:fileitem.index('.')]
                print 'running', sample_name
                generate_wes_cnvnator_shell(os.path.join(samples_path, fileitem), os.path.join(output_folder, sample_name))


# CNVnator running commands

# /Users/racing/Lab/CNV/CNVnator/ychen/CNVnator_v0.3/src/cnvnator -root /Users/racing/Lab/CNV/CNVnator/ychen/placenta_BAC.root -chrom 1 2 3 4 5 6 7 8 9 10 12 13 14 15 16 17 18 19 21 22 X Y -tree /Users/racing/Lab/CNV/CNVnator/ychen/placenta_BAC.local_realigned.sorted.bam
# /Users/racing/Lab/CNV/CNVnator/ychen/CNVnator_v0.3/src/cnvnator -root /Users/racing/Lab/CNV/CNVnator/ychen/placenta_BAC.root -chrom 1 2 3 4 5 6 7 8 9 10 12 13 14 15 16 17 18 19 21 22 X Y -d /Users/racing/Lab/CNV/CNVnator/ychen/hg19/Sequence/Chromosomes/ -his 100
# /Users/racing/Lab/CNV/CNVnator/ychen/CNVnator_v0.3/src/cnvnator -root /Users/racing/Lab/CNV/CNVnator/ychen/placenta_BAC.root -stat 100
# /Users/racing/Lab/CNV/CNVnator/ychen/CNVnator_v0.3/src/cnvnator -root /Users/racing/Lab/CNV/CNVnator/ychen/placenta_BAC.root -partition 100
# /Users/racing/Lab/CNV/CNVnator/ychen/CNVnator_v0.3/src/cnvnator -root /Users/racing/Lab/CNV/CNVnator/ychen/placenta_BAC.root -chrom 1 2 3 4 5 6 7 8 9 10 12 13 14 15 16 17 18 19 21 22 X Y -call 100
