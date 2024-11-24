import argparse
import json
import networkx as nx


def compute_network_stats(input_file, output_file):
    # Load the interaction network from JSON
    with open(input_file, 'r') as f:
        interaction_network = json.load(f)

    # Create a graph from the interaction network
    G = nx.Graph()

    # Add edges and weights to the graph
    for character, neighbors in interaction_network.items():
        for neighbor, weight in neighbors.items():
            if weight > 0:  # Only add edges with positive weight
                G.add_edge(character, neighbor, weight=weight)

    # Compute centrality metrics
    degree_centrality = nx.degree_centrality(G)
    weighted_degree_centrality = {node: sum(data['weight'] for _, _, data in G.edges(node, data=True)) for node in G.nodes}
    closeness_centrality = nx.closeness_centrality(G)
    betweenness_centrality = nx.betweenness_centrality(G, weight='weight')

    # Get the top 3 characters for each metric
    top_degree = sorted(degree_centrality, key=degree_centrality.get, reverse=True)[:3]
    top_weighted_degree = sorted(weighted_degree_centrality, key=weighted_degree_centrality.get, reverse=True)[:3]
    top_closeness = sorted(closeness_centrality, key=closeness_centrality.get, reverse=True)[:3]
    top_betweenness = sorted(betweenness_centrality, key=betweenness_centrality.get, reverse=True)[:3]

    # Prepare the output structure
    stats = {
        "degree": top_degree,
        "weighted_degree": top_weighted_degree,
        "closeness": top_closeness,
        "betweenness": top_betweenness
    }

    # Write the stats to the output file
    with open(output_file, 'w') as f:
        json.dump(stats, f, indent=4)

    print(f"Network stats saved to {output_file}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", help="input JSON file", required=True)
    parser.add_argument("-o", help="output JSON file", default="stats.json")
    args = parser.parse_args()

    compute_network_stats(args.i, args.o)


if __name__ == "__main__":
    main()