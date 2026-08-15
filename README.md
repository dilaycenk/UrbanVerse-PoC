# UrbanVerse PoC: Spatio-Temporal Forecasting & Urban Knowledge Integration

This repository contains the Proof-of-Concept (PoC) demonstration for **UrbanVerse**, integrating spatio-temporal traffic forecasting (**PDFormer**) with structured urban knowledge graph reasoning (**UrbanKGent**).

---

## 1. End-to-End Architecture & Integration

The framework fuses numeric spatio-temporal dynamics with semantic urban knowledge to model cascading city disruptions.

![UrbanVerse End-to-End Integration](urbanverse_end_to_end.png)

+-----------------------------------------------------------------------------------+
|                                    URBANVERSE                                     |
|            (Urban Graph -> Spatio-Temporal Dynamics + Urban Knowledge)            |
+-----------------------------------------------------------------------------------+
|
+-----------------------------------+-----------------------------------+
|                                                                       |
v                                                                       v
[ PDFormer Engine ]                                                 [ UrbanKGent Engine ]
Spatio-Temporal Dynamics                                            Semantic Urban Knowledge

Traffic speed forecasting                                         * Urban entities (Roads, Hospitals, Metro)

Multi-horizon predictions (MAE: 4.18)                             * Semantic relations (serves, located_near)
|                                                                       |
+-----------------------------------+-----------------------------------+
|
v
[ Dynamic Urban Knowledge Fusion ]
* Speed drop alert triggers graph state
* Multi-hop reasoning evaluates cascading disruption


---

## 2. Spatio-Temporal Forecasting Results (PDFormer on METR-LA)

Evaluated on the METR-LA traffic speed benchmark:

| Prediction Horizon | Time Ahead | masked_MAE (Speed Error) | masked_RMSE | masked_MAPE |
| :--- | :--- | :--- | :--- | :--- |
| **Horizon 1** | **5 Minutes** | **4.18 mph** | **7.24 mph** | **9.89%** |
| **Horizon 3** | **15 Minutes** | 14.41 mph | 15.73 mph | 30.24% |
| **Horizon 6** | **30 Minutes** | 11.64 mph | 13.42 mph | 26.29% |
| **Horizon 12** | **60 Minutes** | 30.34 mph | 32.69 mph | 58.27% |

### Forecast Visualizations
| Ground Truth vs. Prediction (12-Hour Profile) | Multi-Horizon Error Progression |
| :---: | :---: |
| ![Ground Truth vs Prediction](ground_truth_vs_prediction.png) | ![PDFormer Error Results](pdformer_results.png) |

---

## 3. Urban Knowledge Graph Scenario & Reasoning (UrbanKGent)

### Knowledge Graph Topology
![Urban Knowledge Graph](urban_kg_graph.png)

### Entity Types & Relations
- **Entities:** `Traffic Sensor`, `Road`, `Metro Station`, `Hospital`, `Residential Area`, `School`
- **Relations:** `has_traffic`, `connected_to`, `located_near`, `serves`

### Reasoning & Retrieval Outputs

#### Query 1: Entity Retrieval
- **Target:** `Central Metro Station`
- **Retrieved Relations:**
  - `<- (connected_to) <- [I-10 Highway Segment]`
  - `-> (serves) -> [Downtown Residential Zone]`
  - `-> (connected_to) -> [Metropolitan High School]`

#### Query 2: Multi-Hop Congestion Cascading Reasoning
- **Trigger:** PDFormer predicts speed drop on `METR-LA Sensor #50` (< 50 mph).
- **Cascading Urban Impact:**
  - `1-Hop:` Bottleneck on `I-10 Highway Segment`
  - `2-Hop:` Transit delay on `Central Metro Station` & emergency route risk for `St. Jude Hospital`
  - `3-Hop:` Commuter disruption in `Downtown Residential Zone` & access delays for `Metropolitan High School`

---

## 4. Execution

```bash
# Run Urban Knowledge Scenario & Reasoning Engine
python urban_kg_scenario.py

# Run End-to-End Integrated Pipeline
python urbanverse_integration_pipeline.py
