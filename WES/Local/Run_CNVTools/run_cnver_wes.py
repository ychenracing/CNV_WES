#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

'''
    run CNVer on WES data, use NA19152 as control, other samples as case.
'''
samples_path = '/Users/racing/Lab/CNV/WES_samples/Whole_exome_but1120'
output_folder = '/Users/racing/Lab/CNV_WES/CNVer/output'
samplelist_path = os.path.join(output_folder, 'sample_list')


def run_cnver():
    command = '/Users/racing/Lab/CNV/CNVer/cnver-0.8.1/src/cnver.pl --map_list ' + \
              samplelist_path + ' --ref_folder /Users/racing/Lab/CNV/CNVer/hg19comp --work_dir ' + \
              output_folder + ' --read_len 100 --mean_insert 300 --stdev_insert 70 --min_mps 2'
    with open(os.path.join(output_folder, 'wes_cnver.sh'), 'w+') as fw:
        fw.write(command)
    print 'Please run the command: sh', os.path.join(output_folder, 'wes_cnver.sh')
    os.system('chmod 777 ' + os.path.join(output_folder, 'wes_cnver.sh'))

if __name__ == '__main__':
    with open(samplelist_path, 'w+') as fw:
        files = os.listdir(samples_path)
        for fileitem in files:
            if fileitem.endswith('bam'):
                if 'NA19152' not in fileitem:
                    fw.write(os.path.join(samples_path, fileitem) + '\n')
    run_cnver()


# CNVer running commands
# /Users/racing/Lab/CNV/CNVer/cnver-0.8.1/src/cnver.pl --map_list
# /Users/racing/Lab/CNV/CNVer/ychen/sample_list --ref_folder
# /Users/racing/Lab/CNV/CNVer/hg19comp/ --work_dir
# /Users/racing/Lab/CNV/CNVer/ychen --read_len 100
# --mean_insert 300 --stdev_insert 70 --min_mps 2
