
use impl_graph::MyGraph;

use petgraph::{Graph, Undirected};
use petgraph::prelude::NodeIndex;
use petgraph::algo::bellman_ford;


fn build_empty_graph(graph: &MyGraph) -> Graph<u64, f64, Undirected>{
    let mut spanner : Graph<u64, f64, Undirected> =  Graph::<u64, f64, Undirected>::new_undirected();
    let zero : usize  = 0;
//    need +1 because the loop create until
    let max_nodes : usize = graph.get_nodes().clone();

    for i in zero .. max_nodes{
         spanner.add_node(0);
    }

    spanner
}


pub fn build_spanner(mut graph: MyGraph, r : f64) -> Graph<u64, f64, Undirected>{
    graph.order_edges();
    let mut spanner  = build_empty_graph(&graph);
    for edge in graph.get_edges() {
        let u = NodeIndex::new(edge.get_u().clone());
        let v = NodeIndex::new(edge.get_v().clone());
        let result = bellman_ford(&spanner, u).ok().unwrap();
        let dis: f64 = result.0.get(v.index()).unwrap().clone();
        if r * edge.get_weight() < dis {
            spanner.add_edge(u, v, edge.get_weight().clone());
        }
    }
    spanner
}


pub fn build_mst(mut graph: MyGraph) -> Graph<u64, f64, Undirected>{
    graph.order_edges();
    let mut mst  = build_empty_graph(&graph);
    for edge in graph.get_edges() {
        let u = NodeIndex::new(edge.get_u().clone());
        let v = NodeIndex::new(edge.get_v().clone());
        let result = bellman_ford(&mst, u).ok().unwrap();
        let dis: f64 = result.0.get(v.index()).unwrap().clone();
        if dis.is_infinite() {
            mst.add_edge(u, v, edge.get_weight().clone());
        }
    }
    mst
}
