# **Decoding Musical Genre from fMRI Brain Activity**

*A simple exploration of “Classifying the Brain on Music” (Casey et al., 2017)*

### Overview

This project aims to document my learning journey through analyzing functional MRI (fMRI) brain-activity data recorded while subjects listened to different genres of music.
The project is inspired by Michael Casey’s paper **“Classifying the Brain on Music” (Frontiers in Psychology, 2017)** and the accompanying Kaggle competition.

My goal here wasn’t to build the most advanced model, but to understand the full workflow from raw fMRI data to simple classification.

---

### Dataset Source

**Paper**

> *Classifying the Brain on Music*
> Michael Casey et al., 2017
> *Frontiers in Psychology, Vol. 8, Article 1179*
> [Read the paper](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2017.01179/full)

**Kaggle Competition**

> [Classifying the Brain on Music – Kaggle](https://www.kaggle.com/competitions/classifying-the-brain-on-music)

---

### Objective

To explore whether we can identify the **music genre** a person is listening to based solely on patterns of their fMRI brain activity.

```
Input:  Brain scan (22,036 voxel activation values)
Output: Predicted music genre (Ambient, Country, Metal, Rock, Classical)
```

---

### Goals

* Understand what fMRI data looks like in machine-learning form
* Practice preprocessing (standardization + PCA)
* Train a simple model (Logistic Regression) and interpret its results
* Visualize class distributions, PCA clusters, and confusion matrices
* Reflect on the neuroscience intuition behind patterns in the data


### Next Steps

* Compare non-linear models (SVM, Random Forest)
* Explore feature importance and voxel clusters

### Acknowledgements

Dataset and conceptual framework by **Michael Casey et al.**
Competition data hosted on Kaggle: *Classifying the Brain on Music*
