#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re


'''extract known cnv to tsv format from dbvar file.'''

dbvar_files_folder = '/Users/racing/Desktop/dbvar_known_cnv'
output_folder = '/Users/racing/Desktop/dbvar_cnv'
variant_accession_line_pattern = re.compile(r'^[0-9]+')


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


def extract_line(lines):
    result = []
    line_dict = {}
    variant_accession = str(lines[0].rstrip()).split()[1]
    i = 1
    while i < len(lines):
        line = lines[i].rstrip()
        if line:
            if not line.startswith('Remapped'):
                features = line.split(':')
                if len(features) <= 1:
                    line_dict[features[0].strip()] = None
                else:
                    line_dict[features[0].strip()] = features[1].strip()
            else:
                line = line[len('Remapped:'):].strip()
                if 'hg19' in line:
                    features = line.split(';')
                    first_space_index = features[0].index(' ')
                    line_dict['assembly'] = features[0][:first_space_index] + '/hg19'
                    region = features[1].strip().split(':')
                    line_dict['chromosome'] = region[0].strip()
                    line_dict['start'] = region[1].strip().split('-')[0]
                    line_dict['stop'] = region[1].strip().split('-')[1]
                else:
                    i += 1
                    line = lines[i].strip()
                    if not line or not line.startswith('ID'):
                        i += 1
                        continue
        i += 1
    chromosome = line_dict.get('chromosome', None)
    result.append(str(chromosome))
    start = line_dict.get('start', None)
    result.append(str(start))
    stop = line_dict.get('stop', None)
    result.append(str(stop))
    associated_study = line_dict.get('Associated study', None)
    result.append(str(associated_study))
    result.append(str(variant_accession))
    genes_in_region = line_dict.get('Gene(s) in region', None)
    result.append(str(genes_in_region).replace(', ', '/'))
    organism = line_dict.get('Organism', None)
    result.append(str(organism))
    location_information = line_dict.get('Location information', None)
    result.append(str(location_information))
    assembly = line_dict.get('assembly', None)
    result.append(str(assembly))
    if line_dict.get('Variant type', None):
        variant_type = 'CNV'
    else:
        variant_type = None
    result.append(str(variant_type))
    cnv_id = line_dict.get('ID', None)
    result.append(str(cnv_id))
    if not chromosome:
        return None
    else:
        return '\t'.join(result)


def extract(file_path):
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)
    file_name = os.path.basename(file_path)
    output_file_name = 'dbvar_known_cnv_NA' + file_name.replace('txt', 'tsv')
    output_file_path = os.path.join(output_folder, output_file_name)
    with open(file_path, 'r+') as fr:
        with open(output_file_path, 'w+') as fw:
            header = 'chromosome\tstart\tstop\tassiciated study\tvariant accession\tgenes in region' + \
                     '\torganism\tlocation information\tassembly\tvariant type\tID'
            fw.write(header + '\n')
            lines = fr.readlines()
            i = 0
            write_lines = []
            while i < len(lines):
                line = lines[i]
                if not line or not line.strip():
                    i += 1
                    continue
                param_lines = []
                if variant_accession_line_pattern.match(line):
                    param_lines.append(line)
                    i += 1
                    line = lines[i]
                    while i < len(lines) and not variant_accession_line_pattern.match(line):
                        param_lines.append(line)
                        i += 1
                        if i >= len(lines):
                            break
                        line = lines[i]
                    write_string = extract_line(param_lines)
                    if write_string:
                        write_string = re.sub(r'\s+', '\t', write_string.strip()) + '\n'
                        write_lines.append(write_string)
            write_lines.sort(cnv_compare)
            fw.writelines(write_lines)
    print output_file_name, 'done!'

if __name__ == '__main__':
    files = os.listdir(dbvar_files_folder)
    for file_item in files:
        if file_item.endswith('.txt'):
            extract(os.path.join(dbvar_files_folder, file_item))
