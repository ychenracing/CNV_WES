#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

'''get cnv events by conrad [conrad paper]()for every wes samples'''

sample_file_names = ['NA10847.txt', 'NA18967.txt', 'NA18973.txt', 'NA18981.txt', 'NA19131.txt']
sample_output_file_names = ['_cnv.'.join(x.split('.')) for x in sample_file_names]
sample_file_paths = '/Users/racing/Downloads/WES'
output_path = sample_file_paths
cnv_file_path = os.path.join(sample_file_paths, 'conrad_cnv.txt')
cnv_dict = dict()


def read_cnv_dict():
    with open(cnv_file_path, 'r+') as fr:
        for line in fr.readlines():
            cnv_dict_item = line.strip().split(None, 1)
            cnv_dict[cnv_dict_item[0]] = cnv_dict_item[1]


def get_sample_cnv_items():
    for sample_file_name, sample_output_file_name in zip(sample_file_names, sample_output_file_names):
        sample_file_path = os.path.join(sample_file_paths, sample_file_name)
        sample_output_file_path = os.path.join(sample_file_paths, sample_output_file_name)
        with open(sample_file_path, 'r+') as fr:
            with open(sample_output_file_path, 'w+') as fw:
                for line in fr.readlines():
                    cnv_id, cnv_num = line.strip().split()
                    if cnv_dict.get(cnv_id) and cnv_num != 2:
                        if cnv_num != 'NA':
                            cnv_feature = cnv_dict.get(cnv_id).split()
                            if cnv_feature[-1] == 'gain/loss':
                                cnv_type = 'gain' if cnv_num > 2 else 'loss'
                                cnv_feature[-1] = cnv_type
                            fw.write('\t'.join(cnv_feature) + '\n')


if __name__ == '__main__':
    read_cnv_dict()
    get_sample_cnv_items()

