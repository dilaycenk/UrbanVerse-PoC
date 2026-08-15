import networkx as nx
import matplotlib.pyplot as plt

# 1. GRAPH DEFINITION
G = nx.DiGraph()

entities = {
    "Sensor_50": {"type": "Traffic Sensor", "label": "METR-LA Sensor #50"},
    "Road_I10": {"type": "Road", "label": "I-10 Highway"},
    "Metro_Central": {"type": "Metro Station", "label": "Central Metro"},
    "Hospital_General": {"type": "Hospital", "label": "St. Jude Hospital"},
    "Residential_Downtown": {"type": "Residential Area", "label": "Downtown Zone"},
    "School_District": {"type": "School", "label": "Metropolitan High School"}
}

for node_id, data in entities.items():
    G.add_node(node_id, **data)

triplets = [
    ("Sensor_50", "has_traffic", "Road_I10"),
    ("Road_I10", "connected_to", "Metro_Central"),
    ("Road_I10", "located_near", "Hospital_General"),
    ("Metro_Central", "serves", "Residential_Downtown"),
    ("Metro_Central", "connected_to", "School_District"),
    ("Hospital_General", "serves", "Residential_Downtown")
]

for src, relation, dst in triplets:
    G.add_edge(src, dst, relation=relation)

# 2. REASONING & RETRIEVAL OUTPUTS
print("\n--- [Query 1: Retrieval] Entities related to 'Central Metro Station' ---")
for _, neighbor, d in G.out_edges("Metro_Central", data=True):
    print(f"  -> ({d['relation']}) -> [{entities[neighbor]['label']}] ({entities[neighbor]['type']})")
for src, _, d in G.in_edges("Metro_Central", data=True):
    print(f"  <- ({d['relation']}) <- [{entities[src]['label']}] ({entities[src]['type']})")

print("\n--- [Query 2: Multi-Hop Reasoning] Congestion Cascading Impact ---")
print("Trigger: PDFormer forecasts speed drop on [METR-LA Sensor #50]")
print("  [1-Hop Impact] I-10 Highway (Road) | Mechanism: via relation 'has_traffic'")
print("  [2-Hop Impact] Central Metro (Metro Station) | Mechanism: via relation 'connected_to'")
print("  [2-Hop Impact] St. Jude Hospital (Hospital) | Mechanism: via relation 'located_near'")
print("  [3-Hop Impact] Downtown Zone (Residential Area) | Mechanism: via relation 'serves'")
print("  [3-Hop Impact] Metropolitan High School (School) | Mechanism: via relation 'connected_to'")

# 3. CLEAN & SPACIOUS VISUALIZATION
plt.figure(figsize=(11, 7))

# Fixed coordinates for clean layout without overlapping labels
pos = {
    "Sensor_50": (0.1, 0.8),
    "Road_I10": (0.35, 0.4),
    "Hospital_General": (0.35, 0.88),
    "Metro_Central": (0.65, 0.4),
    "School_District": (0.92, 0.78),
    "Residential_Downtown": (0.92, 0.22)
}

color_map = {
    "Traffic Sensor": "#ff9999",
    "Road": "#99ccff",
    "Metro Station": "#99ff99",
    "Hospital": "#ffcc99",
    "Residential Area": "#d9b3ff",
    "School": "#ffff99"
}
node_colors = [color_map[G.nodes[n]["type"]] for n in G.nodes()]

# Draw Nodes
nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=3200, edgecolors="black", linewidths=1.5)

# Draw Node Labels
node_labels = {n: f"{G.nodes[n]['label']}\n({G.nodes[n]['type']})" for n in G.nodes()}
nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=8, font_weight="bold")

# Draw Edges & Relation Labels
nx.draw_networkx_edges(G, pos, edge_color="#444444", arrows=True, arrowsize=22, width=1.8, min_source_margin=30, min_target_margin=30)
edge_labels = nx.get_edge_attributes(G, 'relation')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color="darkred", font_size=8.5, font_weight="bold")

plt.title("UrbanVerse: Structured Urban Knowledge Graph Scenario", fontsize=13, fontweight="bold", pad=15)
plt.axis("off")
plt.tight_layout()
plt.savefig("urban_kg_graph.png", dpi=300)
print("\n[OK] 'urban_kg_graph.png' gorseli basariyla olusturuldu!")