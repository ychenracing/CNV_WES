#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''generate conifer shell scripts on 10.20.2.16'''

import os

confier_program_path = '/home/chen/CNV/Conifer'
probe_file_path = '/data/chen/chr1_chr4.bed'
rpkm_cmd_prefix = 'python ' + os.path.join(confier_program_path, 'conifer.py') + ' rpkm --probes ' + probe_file_path + ' --input '
output_folder_path = '/home/chen/CNV/Conifer/wes_chr1'
rpkm_folder_path = os.path.join(output_folder_path, 'rpkm')
analysis_cmd_prefix = 'python ' + os.path.join(confier_program_path, 'conifer.py') + ' analyze --probes '
call_cmd_prefix = 'python ' + os.path.join(confier_program_path, 'conifer.py') + ' call --input '
bam_folder_path = '/data/chen/wes_sample_chr1'


def generate_conifer_shell_script():
    bam_names = [x for x in os.listdir(bam_folder_path) if x.startswith('NA') and x.endswith('bam')]
    with open(os.path.join(output_folder_path, 'wes_conifer_rpkm.sh'), 'w+') as fw:
        for bam_name in bam_names:
            bam_command = rpkm_cmd_prefix + os.path.join(bam_folder_path, bam_name)
            bam_command = bam_command + ' --output ' + os.path.join(rpkm_folder_path, bam_name + '.rpkm')
            fw.write(bam_command + '\n')

    with open(os.path.join(output_folder_path, 'wes_conifer_analysis.sh'), 'w+') as fw:
        analysis_command = analysis_cmd_prefix + probe_file_path + ' --rpkm_dir ' + rpkm_folder_path
        analysis_command += ' --output ' + os.path.join(output_folder_path, 'analysis.hdf5') + ' --svd 6 --write_sd '
        analysis_command += os.path.join(output_folder_path, 'sd_values.txt') + ' --write_svals ' + os.path.join(output_folder_path, 'singular_values.txt')
        fw.write(analysis_command + '\n')

    with open(os.path.join(output_folder_path, 'wes_conifer_call.sh'), 'w+') as fw:
        call_command = call_cmd_prefix + os.path.join(output_folder_path, 'analysis.hdf5') + ' --output ' + os.path.join(output_folder_path, 'call.txt')
        fw.write(call_command + '\n')

if __name__ == '__main__':
    if not os.path.exists(rpkm_folder_path):
        os.mkdir(rpkm_folder_path)
    generate_conifer_shell_script()
