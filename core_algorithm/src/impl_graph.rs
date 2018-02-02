#[derive(Debug)]
pub struct MyGraph {
     vertices: usize,
     edges: Vec<Edge>
}

impl MyGraph {

    #[inline]
    pub fn new() -> MyGraph{
        let vertices : usize = 0;
        let edges: Vec<Edge> = Vec::new();
        MyGraph {vertices, edges}
    }

    pub fn update_the_number_of_nodes(&mut self, nodes: usize){
        self.vertices = nodes;
    }

    pub fn add_vertice(&mut self, number_of_nods: usize){
        self.vertices = self.vertices + number_of_nods;
    }

    pub fn add_edge(&mut self, v: usize, u: usize, weight: f64){
        let new_edge = Edge{v, u, weight};
        self.edges.insert(0, new_edge);
    }

    pub fn order_edges(&mut self) -> &Vec<Edge>{
        self.edges
            .sort_unstable_by(|e1, e2|
                e1.weight.partial_cmp(&e2.weight).unwrap());
        return &self.edges;
    }

    pub fn get_nodes(& self) -> &usize{
      &self.vertices
    }

    pub fn get_edges(& self) -> &Vec<Edge>{
        &self.edges
    }

}

#[derive(Debug)]
pub struct Edge{
    v:usize,
    u:usize,
    weight: f64
}


impl Edge{

    pub fn get_v(&self) -> &usize{
        &self.v
    }

    pub fn get_u(&self) -> &usize{
        &self.u
    }

    pub fn get_weight(&self) -> &f64{
        &self.weight
    }

}

