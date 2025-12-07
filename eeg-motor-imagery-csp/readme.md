# Motor Imagery BCI: Comparing Spatial Filtering Methods

A comparative analysis of spatial filtering techniques for EEG-based brain-computer interfaces, demonstrating why Common Spatial Patterns (CSP) achieves superior performance in motor imagery classification.

## Overview

This project explores five spatial filtering methods for motor imagery BCIs:

1. **Raw Single Channel** - Baseline (55.6% accuracy)
2. **Bipolar Reference** - Differential filtering (62.2% accuracy)
3. **Common Average Reference** - Global noise removal (55.6% accuracy)
4. **Surface Laplacian** - Local spatial sharpening (62.2% accuracy)
5. **Common Spatial Patterns** - Data-driven optimization (93.3% accuracy)

**Key Finding:** CSP outperformed traditional methods by 31 percentage points, achieving 93.3% classification accuracy through personalized, data-driven spatial filtering.

## Background

EEG signals suffer from volume conduction - brain activity spreads through tissue and skull, causing each electrode to pick up signals from multiple sources. This "blurring" makes raw single-channel recordings difficult to classify.

After watching [this excellent YouTube tutorial on motor imagery BCIs](https://www.youtube.com/watch?v=tInGKSP65OY) and reading Blankertz et al.'s seminal 2008 paper, I wanted to understand *why* CSP is considered the gold standard for motor imagery BCIs. Through implementing and comparing five methods, I discovered that **data-driven approaches that adapt to individual brain patterns vastly outperform generic, fixed-rule methods**.

## Dataset

**PhysioNet Motor Imagery Dataset** (Subject 1)
- 64-channel EEG at 160 Hz
- 45 trials (23 LEFT hand, 22 RIGHT hand imagery)
- 2-second epochs filtered to 8-30 Hz (mu/beta rhythms)

[Dataset Link](https://physionet.org/content/eegmmidb/1.0.0/)

## Methods

### Method 1: Raw Single Channel
Uses channel C4 (right motor cortex) without spatial filtering.

**Problem:** Picks up noise from everywhere due to volume conduction.

### Method 2: Bipolar Reference
Subtracts neighboring channel: `C4 - CP4`

**How it helps:** Common noise (eye blinks, distant activity) affects both channels similarly and cancels out.

### Method 3: Common Average Reference (CAR)
Subtracts average of all 64 channels: `C4 - mean(all)`

**How it helps:** Removes global brain states (drowsiness, attention) affecting all sensors equally.

### Method 4: Surface Laplacian
Subtracts average of 4 neighbors: `C4 - mean(FC4, CP4, C2, C6)`

**How it helps:** More robust than bipolar - averaging 4 neighbors dilutes outliers.

### Method 5: Common Spatial Patterns (CSP)
Learns optimal combinations of all 64 channels that maximize class separation.

## Results

| Method | Accuracy | Improvement vs Raw |
|--------|----------|-------------------|
| Raw | 55.6% ± 9.9% | - |
| Bipolar | 62.2% ± 8.9% | +6.6% |
| CAR | 55.6% ± 9.9% | 0% |
| Laplacian | 62.2% ± 15.1% | +6.6% |
| **CSP** | **93.3% ± 5.4%** | **+37.7%** |

**Key Insight:** CSP's 31-point advantage over the next best method demonstrates the power of learning from individual data versus using generic rules.

## References

**YouTube Tutorial:** [Motor Imagery BCI and Spatial Filtering](https://www.youtube.com/watch?v=tInGKSP65OY) - Excellent visual explanation of why CSP works

Blankertz, B., Tomioka, R., Lemm, S., Kawanabe, M., & Muller, K. (2008). "Optimizing Spatial Filters for Robust EEG Single-Trial Analysis." *IEEE Signal Processing Magazine*, 25(1), 41-56.
