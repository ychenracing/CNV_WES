#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

'''extract bam for chr1 & chr4 from a whole bam file'''

samples_folder = '/home/chen/CNV/wes_samples/Whole_exome_but1120'
bamtools_path = '/home/chen/bamtools/bin/bamtools'
samtools_path = '/bin/samtools'
output_folder = '/home/chen/CNV/wes_samples_chr1_chr4'


# use samtools to index bam file
def index_bam(bam_path):
    command = samtools_path + ' index ' + bam_path
    result = os.system(command)
    print bam_path, 'index finished!', result


# use samtools to merge two bam files
def merge_bam(in_bam_path1, in_bam_path2, out_bam_path):
    command = samtools_path + ' merge ' + out_bam_path + ' ' + in_bam_path1 + ' ' + in_bam_path2
    result = os.system(command)
    bam_name1 = os.path.basename(in_bam_path1)
    bam_name2 = os.path.basename(in_bam_path2)
    print 'merge', bam_name1, 'and', bam_name2, 'finished!', result


# use bamtools to extract interested region from bam file
def extract_region(in_bam_path, region, out_bam_path):
    command = bamtools_path + ' filter -in ' + in_bam_path + ' -region ' + str(region) + ' -out ' + out_bam_path
    result = os.system(command)
    print in_bam_path, 'filter region', str(region), 'finished!', result


# to extract interested region chr1 and chr4 from bam file
def extract_chr1_and_chr4_from_bam(bam_path):
    bam_file_name = os.path.basename(bam_path)
    chr1_bam_file_name = bam_file_name[:7] + '.chr1' + bam_file_name[7:]
    chr4_bam_file_name = bam_file_name[:7] + '.chr4' + bam_file_name[7:]
    chr1_chr4_bam_file_name = bam_file_name[:7] + '.chr1_chr4' + bam_file_name[7:]
    extract_region(bam_path, 1, os.path.join(output_folder, chr1_bam_file_name))
    extract_region(bam_path, 4, os.path.join(output_folder, chr4_bam_file_name))

    merge_bam(os.path.join(output_folder, chr1_bam_file_name), os.path.join(output_folder, chr4_bam_file_name),
              os.path.join(output_folder, chr1_chr4_bam_file_name))

    index_bam(os.path.join(output_folder, chr1_chr4_bam_file_name))

    os.remove(os.path.join(output_folder, chr1_bam_file_name))
    print chr1_bam_file_name, 'removed!'
    os.remove(os.path.join(output_folder, chr4_bam_file_name))
    print chr4_bam_file_name, 'removed!'

if __name__ == '__main__':
    bam_files = os.listdir(samples_folder)
    for bam_file in bam_files:
        if 'mapped' in bam_file and bam_file.endswith('bam'):
            extract_chr1_and_chr4_from_bam(os.path.join(samples_folder, bam_file))
    print 'done'
