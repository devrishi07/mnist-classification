
# MNIST Classification

An end-to-end MNIST digit classification project focused on model tuning and data augmentation.

## Overview

This project explores handwritten digit classification using the MNIST dataset.  
Starting from simple baselines, the work progresses through:

- Binary classification (digit vs. not-digit)
- Multiclass classification
- Hyperparameter tuning
- Data augmentation via image shifting
- Evaluation using accuracy and error-rate reduction

The goal is not state-of-the-art performance, but building a clear and well-structured machine learning pipeline.

## Project Structure

├── notebooks/
│ ├── 01_binary_classification.ipynb
│ ├── 02_multiclass_baseline.ipynb
│ ├── 03_hyperparameter_tuning.ipynb
│ └── 04_data_augmentation.ipynb
├── src/
│ ├── data.py
│ └── utils.py
└──  README.md


- **notebooks/** contain exploratory and explanatory workflows  
- **src/** contains reusable data loading, preprocessing, and utility functions  

---

## Methods

- **Models:** Linear classifiers trained with stochastic gradient descent
- **Evaluation:** Accuracy and relative error-rate reduction
- **Augmentation:** Image shifting to improve model robustness
- **Data:** MNIST dataset via `sklearn` / `openml`

---

## Results

Model performance improves through:
- careful hyperparameter tuning
- augmenting the training data with shifted images

Exact metrics are shown and discussed in the final notebooks.

---

## Notes

This repository is intended as a learning and demonstration project.  
The emphasis is on clarity, reproducibility, and understanding model behavior rather than maximizing leaderboard scores.

---

## Requirements

Install dependencies with:

```bash
pip install -r requirements.txt
