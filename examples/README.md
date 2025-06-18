# OGP-lib (Observer Geometry Protocol Library)

A conceptual Python library that demonstrates phase-based key generation using nested quantum observers.

## Core Concepts
- Each Observer collapses the input, generating a state
- Observers can observe other observers (nested interaction)
- A chain of observers creates a geometric structure — a "key"

## Structure
- `observer.py` — Defines the Observer class
- `generator.py` — Generates phase-based keys from observer chains
- `visualizer.py` — Visualizes the observer graph
- `examples/demo_recursive_key.py` — Minimal working demo

## How to Run

1. Install dependencies:
   ```bash
   pip install networkx matplotlib

   2.	Run the demo:python examples/demo_recursive_key.py

   DOI

Zenodo: 10.5281/zenodo.15684052

Author

Aziz Aysenov (Earth as Love)
