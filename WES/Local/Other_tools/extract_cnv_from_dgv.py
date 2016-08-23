#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re


'''extract known cnv to tsv format from dbvar file.'''

dgv_files_folder = '/Users/racing/Desktop/dgv_known_cnv'
output_folder = '/Users/racing/Desktop/dgv_cnv'

## windows
# dgv_files_folder = r'C:\Users\Administrator\Desktop\dgv_known_cnv'
# output_folder = r'C:\Users\Administrator\Desktop\dgv_cnv'


def cnv_compare(cnv_line1, cnv_line2):
    features1 = re.split(r'\s+', cnv_line1)
    features2 = re.split(r'\s+', cnv_line2)
    chr1 = features1[0]
    chr2 = features2[0]
    if chr1 == chr2:
        if int(features1[1]) < int(features2[1]):
            return -1
        elif int(features1[1]) > int(features2[1]):
            return 1
        else:
            if int(features1[2]) < int(features2[2]):
                return -1
            elif int(features1[2]) > int(features2[2]):
                return 1
            else:
                return 0
    else:
        if chr1.isdigit() and chr2.isdigit():
            if int(features1[0]) < int(features2[0]):
                return -1
            else:
                return 1
        elif chr1.isdigit() and not chr2.isdigit():
            return -1
        elif chr2.isdigit() and not chr1.isdigit():
            return 1
        else:
            if chr1 < chr2:
                return -1
            else:
                return 1


def filter_line(line):
    features = re.split(r'\s+', line)
    if features[3] == '1000_Genomes_Consortium_Phase_3':
        if 'hg19' in features[8]:
            if features[9] == 'CNV':
                return True
    return False


def filter_and_sort(file_path):
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)
    file_name = os.path.basename(file_path)
    output_file_name = 'dgv_known_cnv_NA' + file_name.replace('csv', 'tsv')
    output_file_path = os.path.join(output_folder, output_file_name)
    with open(file_path, 'r+') as fr:
        with open(output_file_path, 'w+') as fw:
            lines = fr.readlines()
            header = lines.pop(0)
            lines = filter(filter_line, lines)
            lines = map(lambda line: re.sub(r'\s+', '\t', line.strip()) + '\n', lines)
            lines.sort(cnv_compare)
            fw.write(header)
            fw.writelines(lines)
        print output_file_name, 'done!'


if __name__ == '__main__':
    files = os.listdir(dgv_files_folder)
    for file_item in files:
        if file_item.endswith('csv'):
            filter_and_sort(os.path.join(dgv_files_folder, file_item))
