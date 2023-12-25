from networkx import Graph, connected_components, minimum_edge_cut


def solve(lines):
    graph = Graph()

    for line in lines:
        comp, conns = line.split(":")
        graph.add_node(comp)
        conns = conns.strip().split(" ")
        for conn in conns:
            graph.add_node(conn)
            graph.add_edge(*(comp, conn))

    min_cut = minimum_edge_cut(graph)
    graph.remove_edges_from(min_cut)

    conns = connected_components(graph)
    result = 1
    for c in conns:
        result *= len(c)
    return result


with open("day25.txt", 'r') as f:
    lines = f.read().splitlines()

    total = solve(lines)

    print(f"Day 25-1: {total}")