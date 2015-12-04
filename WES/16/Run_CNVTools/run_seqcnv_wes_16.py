# -*- coding: utf-8 -*-
import os

'''
    run SeqCNV on WES data, use NA19152 as control, other samples as case.
'''

seqcnv_program_path = '/home/chen/CNV/SeqCNV'
samples_path = '/data/chen/wes_samples_chr1_chr4'
control_path = '/data/chen/wes_samples_chr1_chr4/NA19152.chr1_chr4.mapped.ILLUMINA.bwa.YRI.exome.20120522.bam'
bedfile_path = '/home/chen/CNV/SeqCNV/chr1_chr4.bed'
output_folder = '/home/chen/CNV/SeqCNV/wes_chr1_chr4'


def run_seqcnv(case_path, output_path):
    if not os.path.exists(output_path):
        os.mkdir(output_path)
    sample_name = os.path.basename(output_path)
    with open(os.path.join(output_folder, 'wes_seqcnv.sh'), 'a+') as fw:
        fw.write('perl /home/chen/CNV/SeqCNV/run_CNV.pl -c ' + control_path + ' -t ' + case_path +
                 ' -o ' + output_path + ' -r ' + bedfile_path + ' -p ' + seqcnv_program_path + '\n')
    print 'Generate the running shell script for', sample_name, 'done!'

if __name__ == '__main__':
    files = os.listdir(samples_path)
    for file_item in files:
        if file_item.endswith('bam'):
            if 'NA19152' not in file_item:
                sample_name = file_item[:file_item.index('.')]
                run_seqcnv(os.path.join(samples_path, file_item), os.path.join(output_folder, sample_name))
    os.system('chmod 777 ' + os.path.join(output_folder, 'wes_seqcnv.sh'))
    print 'Please run the program use: sh', os.path.join(output_folder, 'wes_seqcnv.sh')
