import fire
from sys import argv
import os
import subprocess
import json
import pandas as pd
from setting import result_path, r_list


def get_files(variable, number_of_nodes, edges_probability, weights_range):
    path_to_search = os.path.join(result_path, '*', '*', '*')
    number_of_nodes = number_of_nodes if number_of_nodes else '*'
    edges_probability = edges_probability if edges_probability else '*'
    weights_range = weights_range if weights_range else '*'
    regex = 'result_{}_n-{}_p-{}_range-{}.txt'.format(variable, number_of_nodes, edges_probability, weights_range)
    path_to_search = os.path.join(path_to_search, regex)
    run = "ls -1 {}".format(path_to_search)
    result = subprocess.check_output(run, shell=True).decode("utf-8")
    lines = result.split('\n')[:-1]
    return lines

def calculate_data(txt):
    result = {}
    with open(txt, 'r') as data:
        read_data = json.loads(data.read())
        mst = float(read_data['mst'])

        for r in r_list:
            spanner = float(read_data['spanner_{}'.format(r)])
            pre = ((spanner - mst) / spanner) * 100
            pre = float("{0:.2f}".format(pre))
            result[r] = pre
    return result



def variable_is(number_of_nodes=None, edges_probability=None, weights_range=None):
    if number_of_nodes and edges_probability and weights_range:
        raise Exception('please choose only two paramthers you choose all three')
    
    if number_of_nodes and edges_probability:
        return 'range'
    elif number_of_nodes and weights_range:
        return 'p'
    else:
        return 'n'

def get_data(number_of_nodes=None, edges_probability=None, minimum_weights=None, max_weights=None):
    # conver to a string
    if minimum_weights and max_weights:
        weights_range = '{}-{}'.format(minimum_weights, max_weights)
    else:
        weights_range = None

    for what_to_look_for in ['weight', 'size']:
        file_list = get_files(what_to_look_for, number_of_nodes, edges_probability, weights_range)
        variable = variable_is(number_of_nodes, edges_probability, weights_range)
        data_frame = {}
        for txt in file_list:
            file_name = os.path.split(txt)[-1]
            if variable == 'range':
                vat = file_name.split(variable)[1].split('-', 1)[1].split('.')[0]
                vat = vat.replace('-', '_')

            elif variable == 'n':  
                vat  = file_name.split(variable)[-2].split('-')[1].split('_')[0]

            elif variable == 'p':
                vat = file_name.split(variable)[1].split('-')[1].split('_')[0]

            data = calculate_data(txt)
            data_frame[vat] = data
        df = pd.DataFrame(data_frame)
        print('\n')
        print('{} n:{} p:{} wight:{}\n'.format(what_to_look_for, number_of_nodes, edges_probability, weights_range))
        print(df)
        print('\n')

if __name__ == '__main__':
      fire.Fire(get_data)
