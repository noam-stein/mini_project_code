import subprocess
from statistics import mean
from itertools import combinations_with_replacement

from setting import number_of_experiments, r_list, algo_loc
from data_manager import *


def build_mst(dis_graph, dis_spanner):
    run_command = [algo_loc, 'mst', dis_graph, dis_spanner]
    subprocess.run(run_command)


def build_spanner(dis_graph, dis_spanner, r):
    run_command = [algo_loc, 'spanner', dis_graph, dis_spanner, r]
    subprocess.run(run_command)


def calculate_mean(type, nodes_number, edge_probability, weight_range, r=None):
    size_mean_list = []
    weight_mean_list = []
    for experiment_number in range(1, number_of_experiments + 1):
        experiment_number = str(experiment_number)
        data_graph = read_graph(type, nodes_number, edge_probability, weight_range, experiment_number, r)
        data_list = data_graph.split('\n')[1:-1]
        size = 0
        weight = 0
        for line in data_list:
            u, v, edge_weight = line.split(' ')
            size += 1
            weight += int(edge_weight)
        size_mean_list.append(size)
        weight_mean_list.append(weight)

    return mean(size_mean_list), mean(weight_mean_list)


def calculate_result(nodes_number, edge_probability, weight_range):
    size_result = {}
    weight_result = {}

    graph_size_mean, graph_weight_mean = calculate_mean('graph', nodes_number, edge_probability, weight_range)
    mst_size_mean, mst_weight_mean = calculate_mean('mst', nodes_number, edge_probability, weight_range)

    size_result['graph'] = graph_size_mean
    weight_result['graph'] = graph_weight_mean

    size_result['mst'] = mst_size_mean
    weight_result['mst'] = mst_weight_mean

    for r in r_list:
        r = str(r)
        spanner_size_mean, spanner_weight_mean = calculate_mean('spanner', nodes_number, edge_probability, weight_range,
                                                                r)
        size_result['spanner_{}'.format(r)] = spanner_size_mean
        weight_result['spanner_{}'.format(r)] = spanner_weight_mean

    write_result('size', nodes_number, edge_probability, weight_range, size_result)
    write_result('weight', nodes_number, edge_probability, weight_range, weight_result)


def start_the_experiment(nodes_number, edge_probability, weight_range):
    for experiment_number in range(1, number_of_experiments + 1):
        experiment_number = str(experiment_number)
        new_graph_loc = create_new_graph(nodes_number, edge_probability, weight_range, experiment_number)
        mst_path = get_graph_loc('mst', nodes_number, edge_probability, weight_range, experiment_number)
        build_mst(new_graph_loc, mst_path)
        for r in r_list:
            r = str(r)
            spanner_path = get_graph_loc('spanner', nodes_number, edge_probability, weight_range, experiment_number, r)
            build_spanner(new_graph_loc, spanner_path, r)

    calculate_result(nodes_number, edge_probability, weight_range)


def main():
    nodes = ['30', '50']
    probabilities = [str(p / 100.0) for p in range(10, 50, 10)]
    weights_list = ['1',  '45']
    for node in nodes:
        for probability in probabilities:
            weights = set(sorted(combinations_with_replacement(weights_list, 2)))
            for weight in weights:
                # if weight[0] < weights
                print('start working on node: {} probability: {} weight: {}'
                      .format(node, probability, weight))
                start_the_experiment(node, probability, weight)


if __name__ == '__main__':
    main()
