# GmE 205 Laboratory 2: Object-Oriented Spatial Data Modeling

## Overview
This laboratory project demonstrates object-oriented modeling of spatial data features using Python. It defines custom classes for individual spatial points (`Point`) and aggregate spatial collections (`PointSet`), while decoupling visualization and metrics generation into a main runner workflow.

---

## Project Structure
```text
gme205-lab2/
├── data/
│   └── points.csv              # Input spatial dataset
├── output/
│   ├── lab2_preview.png        # Scatter plot visualization output
│   └── lab2_report.json        # Generated spatial metrics report
├── src/
│   ├── spatial.py              # Point and PointSet class definitions
│   ├── run_lab2.py             # Main execution and visualization script
│   └── demo.py                 # Quick testing and demonstration script
├── tests/
│   └── test_spatial.py         
├── .gitignore                  # Git tracking rules
├── README.md                   # Project documentation and reflections
└── requirements.txt            # Dependency list (pandas, matplotlib)
```

### Reflections

### 1. Object vs Geometry
Modeling spatial features as objects shifts the paradigm from passive table rows to active entities with state and behavior. Instead of treating coordinates as static numbers, a `Point` object actively enforces coordinate validity upon creation and carries spatial logic (like calculating distances), preserving domain integrity across the application.

### 2. Responsibility
Responsibilities are cleanly separated across three distinct tiers
* **`Point`**: Single-feature state, coordinate validation, and point-to-point spatial logic like validating bounds and calculating distances via `Point.distance_to()`
* **`PointSet`**: Aggregate collection management, dataset extents, and structural filtering like, calculating the global bounding box via `PointSet.bbox()`.
* **Runner Script (`run_lab2.py`)**: File I/O, application orchestration, visualization, and report generation (e.g., saving `output/lab2_preview.png` and `output/lab2_report.json`).

### 3. Modeling Insight
Separating geometry, domain meaning, and application behavior decouples core computational logic from visual output[cite: 1]. Core classes in `spatial.py` remain pure and reusable, ensuring that changing plot aesthetics or report formats in `run_lab2.py` does not break underlying spatial math or unit tests.
