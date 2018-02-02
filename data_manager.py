import random
from os import path
import os
from setting import project_path, result_path
import json

def read_graph(type, nodes_number, edge_probability, weight_range, experiment_number, r=None):
    graph_loc = get_graph_loc(type, nodes_number, edge_probability, weight_range, experiment_number, r)
    with open(graph_loc, 'r') as graph_data:
        data = graph_data.read()
    return data


def write_result(type, nodes_number, edge_probability, weight_range, data):
    file_name = 'result_{}_n-{}_p-{}_range-{}-{}.txt' \
        .format(type, nodes_number, edge_probability, weight_range[0], weight_range[1])
    weight_range = '{}-{}'.format(weight_range[0], weight_range[1])
    data_path = path.join(result_path,nodes_number, edge_probability, weight_range)
    os.makedirs(data_path, exist_ok=True)
    full_path = os.path.join(data_path, file_name)
    with open(full_path, 'w') as graph_data:
        data_string = json.dumps(data)
        graph_data.write(data_string)


def get_path(nodes_number, edge_probability, weight_range, experiment_number):
    weight_range = '{}-{}'.format(weight_range[0], weight_range[1])
    data_path = path.join(project_path, nodes_number, edge_probability, weight_range, experiment_number)
    os.makedirs(data_path, exist_ok=True)
    return data_path


def get_graph_loc(type, nodes_number, edge_probability, weight_range, experiment_number, r=None):
    path = get_path(nodes_number, edge_probability, weight_range, experiment_number)
    file_name = create_name(type, nodes_number, edge_probability, weight_range, experiment_number, r)
    return os.path.join(path, file_name)


def create_new_graph(nodes_number, edge_probability, weight_range, experiment_number):
    new_graph = build_new_graph(nodes_number, edge_probability, weight_range)
    dis = get_graph_loc('graph', nodes_number, edge_probability, weight_range, experiment_number)
    write_graph_to_file(new_graph, dis)
    return dis


def build_new_graph(nodes_number, edge_probability, weight_range):
    weight_low = int(weight_range[0])
    weight_high = int(weight_range[1])
    nodes_number = int(nodes_number)
    edge_probability = float(edge_probability)
    edges = []
    number_list = [num for num in range(nodes_number)]
    # for v, u in combinations_with_replacement(number_list, 2):
    #
    for v in number_list:
        for u in number_list:
            random_number = random.random()
            if random_number < edge_probability and v != u:
                weight = int(random.uniform(weight_low, weight_high))
                edges.append((v, u, weight))
    return nodes_number, edges


def write_graph_to_file(new_graph, dis):
    nodes = new_graph[0]
    edges = new_graph[1]
    with open(dis, 'w') as file:
        file.write("{}\n".format(nodes))
        for v, u, weight in edges:
            file.write('{} {} {}\n'.format(v, u, weight))


def create_name(graph_type, nodes_number, edge_probability, weight_range, experiment_number, r=None):
    file_name = '{}_n-{}_p-{}_range-{}-{}_i-{}' \
        .format(graph_type, nodes_number, edge_probability, weight_range[0], weight_range[1], experiment_number)
    if r:
        file_name += '_r-{}'.format(r)
    file_name += '.txt'
    return file_name
