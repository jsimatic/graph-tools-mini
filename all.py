class Graph:
    def __init__(self):
        self.vertex_list = []
        self.vertex_index = {}
        self.edge_list = []
        self.vp = {}
        self.ep = {}

    def new_vertex_property(self, str):
        return {}
    def new_edge_property(self, str):
        return {}

    def vertex(self, index, add_missing=False):
        for v in self.vertex_list:
            if v.index == index:
                return v
        if add_missing:
            v = Vertex(self, index)
            self.vertex_list.append(v)
            return v
        else:
            print("Could not find V({index}) in {vlist}"
                  "".format(index=index, vlist=self.vertex_list))
            raise LookupError

    def vertices(self):
        return self.vertex_list

    def edges(self):
        return self.edge_list

    def edge(self, src, dest, add_missing=False):
        for e in self.edge_list:
            if e.src == src and e.dest == dest:
                return e
        if add_missing:
            e = Edge(self, src, dest)
            self.edge_list.append(e)
            return e
        else:
            print("Could not find E(%d, %d)"% (src, dest))
            raise LookupError

    def remove_edge(self, e):
        self.edge_list.remove(e)

    def save(self, filename, **kwargs):
        with open(filename, "w") as fh:
            fh.write("")
        return
#------------------------------------------

class Vertex:
    def __init__(self, graph, index):
        self.index = index
        self.graph = graph
        graph.vertex_index[self] = index

    def __repr__(self):
        return "V({index})".format(index=self.index)

    def in_edges(self):
        for e in self.graph.edge_list:
            if e.dest == self:
                yield e

    def out_edges(self):
        for e in self.graph.edge_list:
            if e.src == self:
                yield e

class Edge:
    def __init__(self, graph, src, dest):
        self.graph = graph
        self.src = src
        self.dest = dest

    def source(self):
        return self.src

    def target(self):
        return self.dest
