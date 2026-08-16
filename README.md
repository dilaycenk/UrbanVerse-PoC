# UrbanVerse PoC: Spatio-Temporal Forecasting & Urban Knowledge Integration

This repository contains the Proof-of-Concept (PoC) demonstration for **UrbanVerse**, linking spatio-temporal traffic dynamics with structured urban knowledge graph reasoning.

---

## 1. Spatio-Temporal Traffic Forecasting (PDFormer)

PDFormer was reproduced on the **METR-LA** traffic speed benchmark (207 highway sensor nodes) to capture dynamic city states.

### Benchmark Evaluation Results
| Prediction Horizon | Time Ahead | masked_MAE (Speed Error) | masked_RMSE | masked_MAPE |
| :--- | :--- | :--- | :--- | :--- |
| **Horizon 1** | **5 Minutes** | **4.18 mph** | **7.24 mph** | **9.89%** |
| **Horizon 3** | **15 Minutes** | 14.41 mph | 15.73 mph | 30.24% |
| **Horizon 6** | **30 Minutes** | 11.64 mph | 13.42 mph | 26.29% |
| **Horizon 12** | **60 Minutes** | 30.34 mph | 32.69 mph | 58.27% |

### Forecasting Visualizations
| Sensor #50: Ground Truth vs. Prediction (12-Hour Profile) | Multi-Horizon Error Progression |
| :---: | :---: |
| ![Ground Truth vs Prediction](ground_truth_vs_prediction.png) | ![PDFormer Results](pdformer_results.png) |

---

## 2. Structured Urban Knowledge Graph Scenario & Reasoning (UrbanKGent)

A structured urban knowledge graph was constructed to represent physical city facilities and their semantic dependencies.

### Knowledge Graph Topology
![Urban Knowledge Graph](urban_kg_graph.png)

### Entities & Relations
- **Entities:** `METR-LA Sensor #50`, `I-10 Highway Segment`, `Central Metro Station`, `St. Jude Hospital`, `Downtown Residential Zone`, `Metropolitan High School`
- **Relations:** `has_traffic`, `connected_to`, `located_near`, `serves`

---

### Urban Reasoning & Retrieval Case Studies

#### Case 1: Entity Retrieval Query
* **Research Question:** *"Which urban facilities and transportation nodes are directly or indirectly related to Central Metro Station?"*
* **KG Retrieval Mechanism:** Identifies all 1-hop inbound and outbound semantic edges linked to the target node.
* **Retrieved Structural Context:**
  - `<- (connected_to) <- [I-10 Highway Segment]` (Physical transit corridor)
  - `-> (serves) -> [Downtown Residential Zone]` (Commuter destination)
  - `-> (connected_to) -> [Metropolitan High School]` (Student transit link)

#### Case 2: Multi-Hop Congestion Cascading Reasoning
* **Research Question:** *"Which critical public services and residential zones are disrupted if traffic congestion increases along the I-10 Highway corridor?"*
* **Triggering Event:** Dynamic forecasting alert from PDFormer (Speed on `METR-LA Sensor #50` drops below $50\text{ mph}$).
* **Multi-Hop Graph Propagation:**
  - **Hop 1 (Direct Road Bottleneck):** `METR-LA Sensor #50` $\xrightarrow{\text{has\_traffic}}$ `I-10 Highway Segment` (Congestion localized).
  - **Hop 2 (Public Services & Transit):**
    - `I-10 Highway Segment` $\xrightarrow{\text{connected\_to}}$ `Central Metro Station` (Transit feeder delays).
    - `I-10 Highway Segment` $\xrightarrow{\text{located\_near}}$ `St. Jude Hospital` (Emergency access risk flagged).
  - **Hop 3 (Socio-Urban Spillover):**
    - `Central Metro Station` $\xrightarrow{\text{serves}}$ `Downtown Residential Zone` (Workforce commuter disruption).
    - `Central Metro Station` $\xrightarrow{\text{connected\_to}}$ `Metropolitan High School` (Student transit delays).

---

## 3. End-to-End Architecture & Integration (UrbanVerse Integration)

This module fuses numeric spatio-temporal dynamics with relational graph reasoning to construct a comprehensive **Structured City Representation**.

![UrbanVerse End-to-End Integration](urbanverse_end_to_end.png)
```mermaid
flowchart TD
    subgraph UrbanVerse ["URBANVERSE: Structured City Representation"]
        direction TB
        
        subgraph Models ["Parallel Analysis Engines"]
            direction LR
            PDF["<b>PDFormer Engine</b><br/><i>Spatio-Temporal Dynamics</i><br/>• Speed Forecasting<br/>• MAE: 4.18 mph"]
            UKG["<b>UrbanKGent Engine</b><br/><i>Semantic Knowledge</i><br/>• Urban Topology<br/>• Multi-hop Tracing"]
        end
        
        Fusion["<b>Dynamic Urban Knowledge Fusion</b><br/>• Speed drop alert (&lt; 50 mph) triggers KG anomaly state<br/>• Evaluates cascading facility disruption across the city"]
        
        PDF -->|Dynamic Alert Signal| Fusion
        UKG -->|Semantic Urban Graph| Fusion
    end
---

## 4. Execution

To reproduce the PoC pipelines, execute the following commands from the repository root:

```bash
# 1. Run Urban Knowledge Scenario & Reasoning Engine
# (Constructs the KG topology, visualizes urban_kg_graph.png, and executes Queries 1 & 2)
python urban_kg_scenario.py

# 2. Run End-to-End Integrated Pipeline
# (Fuses PDFormer forecast speed drops with UrbanKGent multi-hop reasoning & outputs urbanverse_end_to_end.png)
python urbanverse_integration_pipeline.py
