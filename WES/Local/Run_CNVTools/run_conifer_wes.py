#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

'''
    run CoNIFER on WES data, use NA19152 as control, other samples as case.
'''
current_path = os.getcwd()
probe_file_path = '/stornext/snfs5/ruichen/dmhg/fgi/lily/CNV/Conifer/ychen/wes/wes_without_chr11_and_chr20.probe'
rpkm_folder_path = '/stornext/snfs5/ruichen/dmhg/fgi/lily/CNV/Conifer/ychen/wes/rpkm'
rpkm_shell_prefix = ('/stornext/snfs5/ruichen/dmhg/fgi/Software/virtual-python/bin/python '
          '/stornext/snfs5/ruichen/dmhg/fgi/Software/conifer_v0.2.2/conifer.py '
          'rpkm --probes /stornext/snfs5/ruichen/dmhg/fgi/lily/CNV/Conifer/ychen/wes/wes_without_chr11_and_chr20.probe --input ')
analysis_shell_prefix = '/stornext/snfs5/ruichen/dmhg/fgi/Software/virtual-python/bin/python ' \
                        '/stornext/snfs5/ruichen/dmhg/fgi/Software/conifer_v0.2.2/conifer.py analyze --probes '
call_shell_prefix = '/stornext/snfs5/ruichen/dmhg/fgi/Software/virtual-python/bin/python /stornext/snfs5/ruichen/dmhg/fgi/Software/conifer_v0.2.2/conifer.py call --input '
bam_folder_path = '/stornext/snfs5/ruichen/dmhg/fgi/wangfei/wes_samples/'

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
    with open(os.path.join(current_path, 'wes_conifer_rpkm.sh'), 'w+') as fw:
        for bam_name in bam_names:
            if 'mapped' in bam_name and bam_name.endswith('bam'):
                bam_command = rpkm_shell_prefix + bam_folder_path + bam_name
                bam_command += ' --output ' + os.path.join(rpkm_folder_path, bam_name[:7] + '.rpkm')
                fw.write(bam_command + '\n')
    # run rpkm shell
    # os.system('sh ' + os.path.join(current_path, 'wes_conifer_rpkm.sh'))
    # run analysis shell
    with open(os.path.join(current_path, 'wes_conifer_analysis.sh'), 'w+') as fw:
        analysis_command = analysis_shell_prefix + probe_file_path + ' --rpkm_dir ' + rpkm_folder_path
        analysis_command += ' --output ' + os.path.join(current_path, 'analysis.hdf5') + '  --svd 3 --write_sd '
        analysis_command += os.path.join(current_path, 'sd_values.txt') + ' --write_svals ' + os.path.join(current_path, 'singular_values.txt')
        fw.write(analysis_command + '\n')
    # os.system('sh ' + os.path.join(current_path, 'wes_conifer_analysis.sh'))
    # run call shell
    with open(os.path.join(current_path, 'wes_conifer_call.sh'), 'w+') as fw:
        call_command = call_shell_prefix + os.path.join(current_path, 'analysis.hdf5') + ' --output ' + os.path.join(current_path, 'call.txt')
        fw.write(call_command + '\n')
    # os.system('sh ' + os.path.join(current_path, 'wes_conifer_call.sh'))


if __name__ == '__main__':
    # generate probe file
    # bed_file_path = '/Users/racing/Lab/CNV/WES_samples/wes_without_chr11_and_chr20.bed'
    # bed2probe(bed_file_path, probe_file_path)
    generate_shell_and_run_every_step()


# /stornext/snfs5/ruichen/dmhg/fgi/Software/virtual-python/bin/python /stornext/snfs5/ruichen/dmhg/fgi/Software/conifer_v0.2.2/conifer.py analyze --probes /stornext/snfs5/ruichen/dmhg/fgi/lily/CNV/Conifer/ychen/test_probes_modified_2 --rpkm_dir /stornext/snfs5/ruichen/dmhg/fgi/lily/CNV/Conifer/rpkm/placenta_ychen/ --output /stornext/snfs5/ruichen/dmhg/fgi/lily/CNV/Conifer/ychen/analysis.hdf5  --svd 3 --write_sd /stornext/snfs5/ruichen/dmhg/fgi/lily/CNV/Conifer/ychen/sd_values.txt --write_svals /stornext/snfs5/ruichen/dmhg/fgi/lily/CNV/Conifer/ychen/singular_values.txt
# /stornext/snfs5/ruichen/dmhg/fgi/Software/virtual-python/bin/python /stornext/snfs5/ruichen/dmhg/fgi/Software/conifer_v0.2.2/conifer.py call --input /stornext/snfs5/ruichen/dmhg/fgi/lily/CNV/Conifer/ychen/analysis.hdf5 --output calls.txt