# UrbanVerse PoC: Spatio-Temporal Forecasting & Urban Knowledge Integration

This repository contains the Proof-of-Concept (PoC) demonstration for **UrbanVerse**, integrating spatio-temporal traffic forecasting (**PDFormer**) with structured urban knowledge graph reasoning (**UrbanKGent**).

---

## 1. Architecture Overview
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

- **Ground Truth vs. Prediction Profile:** `ground_truth_vs_prediction.png`
- **Multi-Horizon Error Curves:** `pdformer_results.png`

---

## 3. Urban Knowledge Graph Scenario & Reasoning (UrbanKGent)

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

## 4. Visual Deliverables

- `urbanverse_end_to_end.png`: End-to-end integration diagram (forecasting stream + knowledge graph).
- `urban_kg_graph.png`: Semantic urban knowledge graph topology.
- `ground_truth_vs_prediction.png`: 12-hour sensor forecasting evaluation curve.
- `pdformer_results.png`: Multi-horizon MAE/RMSE error curves.

---

## 5. Execution

```bash
# Run Urban Knowledge Scenario & Reasoning Engine
python urban_kg_scenario.py

# Run End-to-End Integrated Pipeline
python urbanverse_integration_pipeline.py