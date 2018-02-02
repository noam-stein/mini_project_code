from os import path

algo_loc = path.abspath('./algorithm_binary/algo_run')
project_path = path.abspath('./data')
result_folder_name = 'result'
result_path = path.join(project_path, result_folder_name)

r_list = [i for i in range(1, 16)]
number_of_experiments = 30

