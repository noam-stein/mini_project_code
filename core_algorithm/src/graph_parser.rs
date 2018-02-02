
use std::io::BufRead;
use std::io::BufReader;
use std::fs::File;

use impl_graph::MyGraph;



pub fn get_graph(graph_loc: &str) -> MyGraph {

    let mut graph = MyGraph::new();
//    println!("the graph is : {}", graph_loc);

    let file = File::open(graph_loc).expect("cannot open file");

    let mut file = BufReader::new(file);
    let mut buffer = String::new();

//    get the number of nodes
    file.read_line(&mut buffer);
    if buffer.ends_with("\n"){
        let buffer_len = buffer.len();
        buffer.truncate(buffer_len - 1);
    }
    let nuber_of_nodes : usize = buffer.parse().unwrap();
    graph.update_the_number_of_nodes(nuber_of_nodes);


    for line in file.lines().filter_map(|result| result.ok()) {
        //        split all the new line
//        println!("{:?}", line);
        let mut vec: Vec<_> = line.split(' ').collect();
        let v : usize = vec.remove(0).parse().unwrap();
        let u : usize = vec.remove(0).parse().unwrap();
        let weight : f64  = vec.remove(0).parse().unwrap();
        graph.add_edge(v, u, weight);
    }
//    println!("done reading");
    return graph;
}