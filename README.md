# Supply Chain Performance \& Delay Analytics Pipeline

An end-to-end supply chain analytics pipeline built on Azure, featuring delivery delay prediction, supplier performance analysis, and an interactive Power BI dashboard.

## Project Overview

Post-2020 supply chain disruptions exposed a critical gap in enterprise analytics visibility. This project builds a complete analytics pipeline to identify delay patterns, score supplier performance, and predict at-risk orders before they ship.

## Architecture

**Raw Data (Kaggle/Olist) → Azure Blob Storage → Python ETL → **

**XGBoost Model → Processed Data → Azure Blob Storage → Power BI Dashboard**

## Tech Stack

*- \*\*Cloud:\*\* Azure Blob Storage*

*- \*\*Data Processing:\*\* Python, Pandas, NumPy*

*- \*\*Machine Learning:\*\* XGBoost (AUC: 0.84)*

*- \*\*Visualization:\*\* Power BI*

*- \*\*Dataset:\*\* Brazilian E-Commerce (Olist) — 96,470 orders, 9 tables*

## Key Findings

- Overall late delivery rate: 6.77%

- Top delay predictor: purchase month (seasonality)

- Highest risk region: Amazonas (AM) — 33% late rate

- Same-state orders are significantly less likely to be delayed

- Orders placed in March have the highest late rate (\~15%)



*## ML Model Performance*

*- \*\*Algorithm:\*\* XGBoost Classifier*

*- \*\*AUC-ROC:\*\* 0.84*

*- \*\*Late order recall:\*\* 71%*

*- \*\*Class imbalance handled via:\*\* scale\_pos\_weight (13.76)*

*- \*\*Top features:\*\* purchase\_month, same\_state, carrier\_delay\_hours*



*## Project Structure*



*supply-chain-analytics/*

*├── notebooks/          # Jupyter notebooks - EDA, features, modeling*

*├── scripts/            # Azure ingestion scripts*

*├── models/             # Saved XGBoost model + encoders*

*├── dashboard/          # Power BI file + screenshots*

*├── processed\_data/     # Transformed datasets*

*└── raw\_data/           # Original Olist CSVs (gitignored)*



*## Dashboard Preview*

*!\[Supply Chain Dashboard](dashboard/supply\_chain\_dashboard\_ss.png)*



*## How to Run*

*1. Clone the repo*

*2. Create virtual environment: `python -m venv venv`*

*3. Activate: `venv\\Scripts\\activate`*

*4. Install dependencies: `pip install -r requirements.txt`*

*5. Add your Azure connection string to `.env`*

*6. Run `scripts/upload\_to\_azure.py` to ingest data*

*7. Open `notebooks/supply\_chain\_analysis.ipynb` and run all cells*



