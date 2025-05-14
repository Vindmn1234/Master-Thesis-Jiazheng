# Master-Thesis-Predicting Clinical Trial Completion and Success using Machine Learning and NLP

This repository contains the full codebase, data, and documentation for my master's thesis project at the University of Chicago, titled:

“Predicting Clinical Trial Completion and Success Using Machine Learning and Natural Language Processing”Author: Jiazheng Li | May 2025 | Faculty Advisor: Prof. Yuan Ji

📘 Overview

This project introduces a dual-task machine learning framework to predict:

Clinical Trial Completion — whether a trial reaches its intended completion or is prematurely terminated.

Clinical Trial Success — whether a trial meets its primary endpoints, inferred via LLM-based analysis of associated publications.

We leverage structured metadata from ClinicalTrials.gov and unstructured text (trial descriptions and publication abstracts), enhanced by modern NLP techniques (e.g., BioLinkBERT and GPT-4o-mini) to build predictive models.

🧠 Key Contributions

Data Integration: Merged data from ClinicalTrials.gov API and PubMed for 500K+ trials.

Dual-Prediction Pipeline:

Operational Completion using XGBoost, Random Forest, and Dual-Tower Neural Networks.

Scientific Success via GPT-4-based label generation and predictive modeling.

LLM Labeling Pipeline: Designed a two-step GPT-4o-mini pipeline to classify publication outcomes as Positive / Negative / Unknown.

Embedding Integration: Compared tabular-only models with embedding-enhanced models using BioLinkBERT and PCA.

Interpretability: Used SHAP to interpret model predictions and highlight key drivers (e.g., enrollment size, sponsor type, trial design).

🗂️ Repository Structure

.
├── Model training/                  # Scripts and notebooks for model training (e.g., XGBoost, Random Forest, Neural Network)
├── Parse Data/                     # Scripts for flattening, cleaning, and extracting ClinicalTrials.gov and PubMed data
├── feature_engineering_completion.ipynb    # Completion task: feature engineering and modeling
├── feature_engineering_success.ipynb       # Outcome task: feature engineering and modeling
├── link_pubmed.ipynb              # Linking trials with PubMed abstracts using PubMed API
├── example data.xlsx              # Sample trial-level data used in modeling
├── thesis.pdf                     # Full thesis write-up (University of Chicago, 2025)
└── README.md                      # This file

🔧 Technologies Used

Python, pandas, scikit-learn, XGBoost, transformers

BioLinkBERT, PubMedBERT, GPT-4o-mini

SHAP for model interpretation

ClinicalTrials.gov API, PubMed API

📊 Highlights from Results

Trial Completion Prediction:

XGBoost with BioLinkBERT embeddings outperformed tabular-only models by ~1% AUC.

Enrollment size, trial duration, sponsor type, and intervention model were top predictors.

Trial Outcome Prediction:

GPT-4o-mini achieved 94% accuracy vs. human-annotated publications.

Structured features showed moderate predictive power (AUC ~0.72 with XGBoost).

Stratified by phase, Phase 3 trials had the most difficult prediction due to outcome complexity.

📌 Limitations & Future Work

Publication bias and incomplete linkage between trials and publications may affect label accuracy.

Future directions: analyze full-text publications, include adverse event data, and apply retrieval-augmented generation (RAG) for richer feature extraction.

📌 Citation

If you use any part of this work, please cite:

Jiazheng Li (2025). Predicting Clinical Trial Completion and Success Using Machine Learning and Natural Language Processing. Master’s Thesis, University of Chicago.PDF in this repo

📬 Contact

For questions or collaborations, feel free to reach out via GitHub or email: jiazhengli@uchicago.edu

