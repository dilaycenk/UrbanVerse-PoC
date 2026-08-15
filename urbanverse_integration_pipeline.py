import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# ==========================================================
# 1. SPATIO-TEMPORAL FORECASTING STREAM (PDFormer Engine)
# ==========================================================
print("==================================================")
print(" URBANVERSE: END-TO-END PO-C INTEGRATION ENGINE   ")
print("==================================================")

# 12-hour simulated traffic stream for Sensor #50
time_steps = 144
np.random.seed(42)
base_speed = 65.0
congestion_dip = np.sin(np.linspace(0, 3 * np.pi, time_steps)) * 12
noise = np.random.normal(0, 3.5, size=time_steps)
predicted_speeds = np.clip(base_speed + congestion_dip + noise, 25, 75)

# Congestion Threshold
CONGESTION_THRESHOLD = 50.0  # mph

# Detect First Critical Anomaly
critical_indices = np.where(predicted_speeds < CONGESTION_THRESHOLD)[0]
alert_step = critical_indices[0] if len(critical_indices) > 0 else 22
alert_speed = predicted_speeds[alert_step]
alert_time_min = (alert_step + 1) * 5

print(f"[PDFormer Event] Time Step t={alert_step} (T+{alert_time_min} mins)")
print(f" -> Monitored Sensor: METR-LA Sensor #50")
print(f" -> Predicted Speed: {alert_speed:.1f} mph (Threshold: < {CONGESTION_THRESHOLD} mph)")
print(f" -> Status: CRITICAL CONGESTION PREDICTED\n")

# ==========================================================
# 2. DYNAMIC URBAN KNOWLEDGE GRAPH REASONING
# ==========================================================
G = nx.DiGraph()

entities = {
    "PDFormer_Alert": {"type": "Alert", "label": f"Speed Drop Alert\n({alert_speed:.1f} mph)"},
    "Sensor_50": {"type": "Traffic Sensor", "label": "Sensor #50"},
    "Road_I10": {"type": "Road", "label": "I-10 Highway"},
    "Metro_Central": {"type": "Metro Station", "label": "Central Metro"},
    "Hospital_General": {"type": "Hospital", "label": "St. Jude Hospital"},
    "Residential_Downtown": {"type": "Residential Area", "label": "Downtown Zone"},
    "School_District": {"type": "School", "label": "Metro High School"}
}

for k, v in entities.items():
    G.add_node(k, **v)

triplets = [
    ("PDFormer_Alert", "triggers_state", "Sensor_50"),
    ("Sensor_50", "monitors", "Road_I10"),
    ("Road_I10", "causes_delay_to", "Metro_Central"),
    ("Road_I10", "blocks_access_to", "Hospital_General"),
    ("Metro_Central", "disrupts_transit_to", "Residential_Downtown"),
    ("Metro_Central", "delays_commute_to", "School_District"),
    ("Hospital_General", "limits_emergency_for", "Residential_Downtown")
]

for s, r, d in triplets:
    G.add_edge(s, d, relation=r)

print("--- [UrbanKGent Context-Aware Multi-Hop Reasoning] ---")
print(f"1. Spatio-Temporal trigger activated on [{entities['Sensor_50']['label']}]")
print(f"2. Physical Road Bottleneck: [{entities['Road_I10']['label']}]")
print("3. Downstream Cascading Urban Impacts:")
print(f"   * [Healthcare Risk] -> {entities['Hospital_General']['label']} (Emergency route restricted)")
print(f"   * [Transit Congestion] -> {entities['Metro_Central']['label']} (Bus/metro transfer bottleneck)")
print(f"   * [Societal Impact] -> {entities['Residential_Downtown']['label']} & {entities['School_District']['label']} (Commuter delays)")

# ==========================================================
# 3. END-TO-END INTEGRATION VISUALIZATION
# ==========================================================
fig, (ax_st, ax_kg) = plt.subplots(1, 2, figsize=(16, 6.5), gridspec_kw={'width_ratios': [1, 1.3]})

# Subplot 1: PDFormer Forecasting Stream
ax_st.plot(predicted_speeds, color='#1f77b4', linewidth=1.8, label='PDFormer Predicted Speed')
ax_st.axhline(CONGESTION_THRESHOLD, color='red', linestyle='--', label=f'Congestion Threshold ({CONGESTION_THRESHOLD} mph)')
ax_st.scatter(alert_step, alert_speed, color='darkred', s=120, zorder=5, label='Anomaly Trigger Point')
ax_st.annotate(f'Alert Trigger\n({alert_speed:.1f} mph)', xy=(alert_step, alert_speed), xytext=(alert_step + 10, alert_speed - 10),
                arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=6), fontweight='bold', fontsize=9)
ax_st.set_title("1. Spatio-Temporal Dynamic Stream (PDFormer)", fontsize=11, fontweight='bold')
ax_st.set_xlabel("Time Step (5-min intervals)", fontsize=10)
ax_st.set_ylabel("Traffic Speed (mph)", fontsize=10)
ax_st.grid(True, linestyle=':', alpha=0.6)
ax_st.legend(loc='upper right', fontsize=8.5)

# Subplot 2: Dynamic Knowledge Graph Propagation
pos = {
    "PDFormer_Alert": (0.05, 0.5),
    "Sensor_50": (0.28, 0.5),
    "Road_I10": (0.50, 0.5),
    "Hospital_General": (0.75, 0.82),
    "Metro_Central": (0.75, 0.22),
    "School_District": (0.98, 0.22),
    "Residential_Downtown": (0.98, 0.82)
}

color_map = {
    "Alert": "#ff4d4d",
    "Traffic Sensor": "#ff9999",
    "Road": "#99ccff",
    "Metro Station": "#99ff99",
    "Hospital": "#ffcc99",
    "Residential Area": "#d9b3ff",
    "School": "#ffff99"
}
node_colors = [color_map[G.nodes[n]["type"]] for n in G.nodes()]

nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=2600, edgecolors="black", linewidths=1.2, ax=ax_kg)
node_labels = {n: f"{G.nodes[n]['label']}" for n in G.nodes()}
nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=7.5, font_weight="bold", ax=ax_kg)
nx.draw_networkx_edges(G, pos, edge_color="#333333", arrows=True, arrowsize=16, width=1.5, min_source_margin=22, min_target_margin=22, ax=ax_kg)
edge_labels = nx.get_edge_attributes(G, 'relation')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color="darkred", font_size=7, font_weight="bold", ax=ax_kg)

ax_kg.set_title("2. Context-Aware Knowledge Propagation (UrbanKGent)", fontsize=11, fontweight='bold')
ax_kg.axis("off")

plt.suptitle("UrbanVerse Framework: Spatio-Temporal Forecasting & Urban Knowledge Integration", fontsize=13, fontweight='bold', y=0.98)
plt.tight_layout()
plt.savefig("urbanverse_end_to_end.png", dpi=300)
print("\n[OK] Uçtan uca mimari şeması 'urbanverse_end_to_end.png' olarak kaydedildi!")