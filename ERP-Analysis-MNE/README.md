# ERP Analysis with MNE-Python

## Project Overview 

This project aims to analyze brain responses to auditory and visual stimuli using MEG data. 
Shows **when** and **where** the brain activates when you hear a sound vs. see a light.

## The Experiment

- **Auditory stimuli:** Beeps in left/right ear
- **Visual stimuli:** Flashing checkerboards on left/right side
- **Data:** ~60 seconds of MEG recording, ~72 trials per condition

## Quick Start

```bash
# Install dependencies
pip install mne numpy matplotlib

# Run the notebook
jupyter notebook erp_analysis.ipynb
```

The sample dataset downloads automatically on first run (around 1.5GB).

## What You'll Get

**3 main visualizations:**

1. **ERP Waveforms** - Brain activity over time for each condition
2. **Topographic Maps** - Spatial patterns showing where activity occurs
3. **Global Field Power** - Overall strength comparison (auditory vs visual)

## Key Concepts

| Concept | What It Means |
|---------|---------------|
| **Raw data** | Continuous brain recording |
| **Filtering** | Remove noise, keep 1-40 Hz signals |
| **Events** | Timestamps when stimuli appeared |
| **Epochs** | Data chunks around each stimulus (-200 to +500 ms) |
| **Baseline** | Pre-stimulus activity we subtract out |
| **ERP** | Average of all trials (signal emerges, noise cancels) |
| **Topomap** | Bird's-eye view of head showing activity |

**Skills learned:** Loading MEG data • Preprocessing • Epoching • ERP computation • Data visualization
