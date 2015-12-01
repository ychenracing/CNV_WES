#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

'''
    run SeqCNV on WES data, use NA19152 as control, other samples as case.
'''


seqcnv_program_path = '/Users/racing/Downloads/seqcnv_programs'
samples_path = '/Users/racing/Lab/CNV/WES_samples/Whole_exome_but1120'
control_path = '/Users/racing/Lab/CNV/WES_samples/Whole_exome_but1120' \
               '/NA19152.mapped.ILLUMINA.bwa.YRI.exome.20120522.bam'
bedfile_path = '/Users/racing/Lab/CNV_WES/EXCAVATOR/chr1_4.bed'
output_folder = '/Users/racing/Downloads/seqcnv_programs/wes'


def run_seqcnv(case_path, output_path):
    if not os.path.exists(output_path):
        os.mkdir(output_path)
    with open(os.path.join(output_folder, 'wes_seqcnv.sh'), 'a+') as fw:
        fw.write('perl /Users/racing/Downloads/seqcnv_programs/run_CNV.pl -c ' + control_path + ' -t ' + case_path +
                 ' -o ' + output_path + ' -r ' + bedfile_path + ' -p ' + seqcnv_program_path + '\n')

if __name__ == '__main__':
    files = os.listdir(samples_path)
    for fileitem in files:
        if fileitem.endswith('bam'):
            if 'NA19152' not in fileitem:
                sample_name = fileitem[:fileitem.index('.')]
                run_seqcnv(os.path.join(samples_path, fileitem), os.path.join(output_folder, sample_name))
