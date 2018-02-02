# On sparse spanners of weighted Graphs

## How to comile the rust code
1. download the Code from github
2. Download the rust comiler [Rust](https://www.rust-lang.org/en-US/install.html)
3. go to the folder `core_algorithm`
4. run `cargo build --release`
5. then copy the binary `algo_run` to the folder `algorithm_binary` or
  run `cp ./target/release/algo_run ./../algorithm_binary`

## How to build the data
to build the data set you need to run the command
```python3 ./run_algorithm.py```

## How to read the data
first install the dependency
run: `pip install -r ./requirement.txt`

if you want to get the charts for number of nodes
`python3 ./read_data.py  --edges_probability={probability}  --minimum_weights={int} --max_weights={int}`
for exmple `python3 ./read_data.py --edges_probability=0.4  --minimum_weights=1 --max_weights=1`

if you want to get the charts for edges probability
`python3 ./read_data.py  --number_of_nodes={int}  --minimum_weights={int} --max_weights={int}`
for exmple `python3 ./read_data.py --number_of_nodes=30  --minimum_weights=1 --max_weights=25`

if you want to get the charts for weights range
`python3 ./read_data.py  --number_of_nodes={int}  --edges_probability={probability}`
for exmple `python3 ./read_data.py  --number_of_nodes=10  --edges_probability=0.3`


!this code was testes with Python 3.6.3