extern crate petgraph;

mod graph_parser;
mod build_graphs;
mod impl_graph;
use std::env;
use build_graphs::{build_spanner, build_mst};
use std::fs::File;
use std::io::prelude::*;
use petgraph::{Graph, Undirected};
use petgraph::graph::{EdgeReference, EdgeReferences};

fn write_to_file(spanner: Graph<u64, f64, Undirected>, to : String){
    let mut file = File::create(to).unwrap();
    let node_count = spanner.node_count().to_string();
    file.write_all(node_count.as_bytes());
    file.write_all(b"\n");

    for edge in spanner.raw_edges(){
//        println!("{:?}", edge);
        let v = edge.source().index().to_string();
        let u = edge.target().index().to_string();
        let weight = edge.weight.to_string();
        file.write_all(u.as_bytes());
        file.write_all(b" ");
        file.write_all(v.as_bytes());
        file.write_all(b" ");
        file.write_all(weight.as_bytes());
        file.write_all(b"\n");
    }
}

fn main(){
    let args: Vec<String> = env::args().collect();
    let what_to_do =  &args[1];
    let from =  &args[2];
    let to = &args[3];

    let mut graph = graph_parser::get_graph(from);

    if what_to_do == "spanner" {
        let r: f64 = args[4].clone().parse().unwrap();
        write_to_file(build_spanner(graph, r), to.to_string());

    }else{
        write_to_file(build_mst(graph), to.to_string());

    }

}