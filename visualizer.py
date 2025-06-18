import networkx as nx
import matplotlib.pyplot as plt

def visualize_observer_chain(observers):
    G = nx.DiGraph()
    labels = {}

    for i, obs in enumerate(observers):
        node_id = f"O{obs.level}"
        labels[node_id] = f"O{obs.level}\\nstate:{obs.state}"
        G.add_node(node_id)
        if i > 0:
            prev_id = f"O{observers[i-1].level}"
            G.add_edge(prev_id, node_id)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=False, arrows=True, node_size=1500, node_color='lightblue')
    nx.draw_networkx_labels(G, pos, labels, font_size=10)
    plt.title("Observer Chain")
    plt.show()
