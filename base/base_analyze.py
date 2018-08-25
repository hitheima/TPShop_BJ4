import os

import yaml


def analyze_with_file(file_name, case_name):

    with open("." + os.sep + "data" + os.sep + file_name + ".yml", "r", encoding='utf-8') as f:
        res = yaml.load(f)[case_name]

        temp_list = list()
        for values in res.values():
            temp_list.append(values)

        return temp_list
