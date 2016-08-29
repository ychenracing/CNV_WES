#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os


conifer_path = '/home/chen/CNV/Conifer'
output_path = '/home/chen/CNV/Conifer/placenta'
probe_file_path = '/data/chen/placenta.bed'
rpkm_folder_path = os.path.join(output_path, 'rpkm')
rpkm_shell_prefix = 'python ' + os.path.join(conifer_path, 'conifer.py') + ' rpkm --probes ' + probe_file_path + ' --input '
analysis_shell_prefix = 'python ' + os.path.join(conifer_path, 'conifer.py') + ' analyze --probes '
call_shell_prefix = 'python ' + os.path.join(conifer_path, 'conifer.py') + ' call --input '
bam_folder_path = '/data/chen/placenta_other_samples/'

# generate probe file
# def bed2probe(bed_file_path, output_path):
#     with open(output_path, 'w+') as fw:
#         with open(bed_file_path, 'r+') as fr:
#             lines = fr.readlines()
#             for line in lines:
#                 line = line.strip()
#                 new_line = line[3:] + '\n'
#                 fw.write(new_line)


# generate rpkm shell scripts
def generate_shell_and_run_every_step():
    bam_names = os.listdir(bam_folder_path)
    with open(os.path.join(output_path, 'conifer_rpkm.sh'), 'w+') as fw:
        for bam_name in bam_names:
            if bam_name.endswith('bam'):
                bam_command = rpkm_shell_prefix + bam_folder_path + bam_name
                bam_command += ' --output ' + os.path.join(rpkm_folder_path, bam_name[:bam_name.index('.')] + '.rpkm')
                fw.write(bam_command + '\n')
    # run rpkm shell
    # os.system('sh ' + os.path.join(current_path, 'wes_conifer_rpkm.sh'))
    # run analysis shell
    with open(os.path.join(output_path, 'conifer_analysis.sh'), 'w+') as fw:
        analysis_command = analysis_shell_prefix + probe_file_path + ' --rpkm_dir ' + rpkm_folder_path
        analysis_command += ' --output ' + os.path.join(output_path, 'analysis.hdf5') + '  --svd 3 --write_sd '
        analysis_command += os.path.join(output_path, 'sd_values.txt') + ' --write_svals ' + os.path.join(output_path, 'singular_values.txt')
        fw.write(analysis_command + '\n')
    # os.system('sh ' + os.path.join(current_path, 'wes_conifer_analysis.sh'))
    # run call shell
    with open(os.path.join(output_path, 'conifer_call.sh'), 'w+') as fw:
        call_command = call_shell_prefix + os.path.join(output_path, 'analysis.hdf5') + ' --output ' + os.path.join(output_path, 'call.txt')
        fw.write(call_command + '\n')
    # os.system('sh ' + os.path.join(current_path, 'wes_conifer_call.sh'))


if __name__ == '__main__':
    # generate probe file
    # bed_file_path = '/Users/racing/Lab/CNV/WES_samples/wes_without_chr11_and_chr20.bed'
    # bed2probe(bed_file_path, probe_file_path)
    generate_shell_and_run_every_step()
