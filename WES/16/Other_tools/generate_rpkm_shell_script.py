#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''generate rpkm shell scripts'''

import os

confer_program_path = ''
probe_file_path = ''
cmd_prefix = 'python ' + os.path.join(confer_program_path, 'conifer.py') + ' rpkm --probes ' + probe_file_path + ' --input '
rpkm_folder_path = ''
bam_folder_path = '/data/chen/wes_sample_chr1'

def generate_every_bam_command():
    bam_names = [x for x in os.listdir(bam_folder_path) if x.startswith('NA') and x.endswith('bam')]
    with open('./ychen_conifer_rpkm_modified.sh', 'w+') as fw:
        for bam_name in bam_names:
            bam_command = cmd_prefix + os.path.join(bam_folder_path, bam_name)
            bam_command = bam_command + ' --output ' + os.path.join(rpkm_folder_path, bam_name + '.rpkm')
            fw.write(bam_command + '\n')

if __name__ == '__main__':
    generate_every_bam_command()
