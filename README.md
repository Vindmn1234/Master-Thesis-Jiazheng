# Master Thesis:Predicting Clinical Trial Completion and Success using Machine Learning and NLP

This repository contains the full codebase, data, and documentation for my master's thesis project at the University of Chicago, titled:

“Predicting Clinical Trial Completion and Success Using Machine Learning and Natural Language Processing”Author: Jiazheng Li | May 2025 | Faculty Advisor: Prof. Yuan Ji

📘 Overview

** This project introduces a dual-task machine learning framework to predict: **
1. Clinical Trial Completion — whether a trial reaches its intended completion or is prematurely terminated.
2. Clinical Trial Success — whether a trial meets its primary endpoints, inferred via LLM-based analysis of associated publications.
We leverage structured metadata from ClinicalTrials.gov and unstructured text (trial descriptions and publication abstracts), enhanced by modern NLP techniques (e.g., BioLinkBERT and GPT-4o-mini) to build predictive models.

- **🧠 Key Contributions**  
  - **Data Retrieval:**  
    - Effectively and scalably retrieved the entire ClinicalTrials.gov dataset (**500K+ clinical trials**) using the public API.  
  - **Data Integration:**  
    - Merged data from ClinicalTrials.gov API and PubMed for **120K+ trials**.  
  - **Dual-Prediction Pipeline:**  
    - **Operational Completion:**  
      - Trained XGBoost, Random Forest, and Dual-Tower Neural Networks on both **structured features** and **unstructured trial descriptions** (embedded via BioLinkBERT).  
    - **Scientific Success:**  
      - Implemented **GPT-4-based label generation** and predictive modeling.  
  - **LLM Labeling Pipeline:**  
    - Designed a **two-step GPT-4o-mini pipeline** to classify publication outcomes as *Positive* / *Negative* / *Unknown*.  
  - **Embedding Integration:**  
    - Compared **tabular-only models** vs. **embedding-enhanced models** (BioLinkBERT + PCA).  
  - **Interpretability:**  
    - Used **SHAP** to interpret predictions, highlighting key drivers (enrollment size, sponsor type, trial design).  

- **🗂️ Repository Structure**  
  ```
  .
  ├── Model training/                  # Scripts and notebooks for model training (e.g., XGBoost, Random Forest, Neural Network)
  ├── Parse Data/                      # Scripts for flattening, cleaning, and extracting ClinicalTrials.gov and PubMed data
  ├── feature_engineering_completion.ipynb    # Completion task: feature engineering and modeling
  ├── feature_engineering_success.ipynb       # Outcome task: feature engineering and modeling
  ├── link_pubmed.ipynb               # Linking trials with PubMed abstracts using PubMed API
  ├── example data.xlsx               # Sample trial-level (raw) data
  ├── thesis.pdf                      # Full thesis write-up (University of Chicago, 2025)
  └── README.md                       # This file
  ```
🔧 Technologies Used

Python, pandas, scikit-learn, XGBoost, pytorch, GPT-4 API, BioLinkBERT, Google colab, PCA, 
ClinicalTrials.gov API, PubMed API, Mesh API, xml, json

📊 Highlights from Results
- **Trial Completion Prediction:**
  - XGBoost consistently outperformed SVM, Random Forest, and Neural Networks across all class balancing strategies.
  - Under a 1:1.5 downsampling ratio, XGBoost with BioLinkBERT embeddings achieved an AUC of 0.894, accuracy of 82.8%, and balanced F1 scores for both completed and non-completed classes.
  - Incorporating BioLinkBERT embeddings improved AUC by approximately 1%, especially enhancing detection of non-completed trials.
  - Key predictors included enrollment size, trial duration, intervention model, number of facilities, and sponsor type.
    
- **Trial Outcome Prediction:
  - GPT-4o-mini achieved 94% accuracy in labeling publication outcomes when benchmarked against human annotations.
  - XGBoost trained on structured features achieved an AUC of 0.717 and accuracy of 66.1%.
  - Adding trial description embeddings did not improve performance, suggesting trial descriptions are more relevant to operational feasibility than outcome success.
  - Performance varied slightly by trial phase, with Phase 2 and 3 showing modestly higher predictive accuracy than Phase 1.
    
📌 Limitations & Future Work
- Include important features(number of patients at risk, adverse events, death) from a more well-structured database(AACT).
- Publication bias and incomplete linkage between trials and publications may affect label accuracy.
- Future directions: analyze full-text publications, clinical trial interim reports(if possible), and apply retrieval-augmented generation (RAG) for richer feature extraction(google news, google scholar, etc.).

📌 Citation

If you use any part of this work, please cite:
Jiazheng Li (2025). Predicting Clinical Trial Completion and Success Using Machine Learning and Natural Language Processing. Master’s Thesis, University of Chicago.PDF in this repo

📬 Contact
For questions or collaborations, feel free to reach out via GitHub or email: jiazheng123@uchicago.edu

