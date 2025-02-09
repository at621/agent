# Credit Risk AI Agent

A **proof-of-concept** AI-driven credit risk solution built with [LangChain](https://github.com/hwchase17/langchain), Python, and data science libraries. 

It demonstrates a typical workflow:
1. **Problem Identification**: Determines if a user requests a PD or LGD model.  
2. **Data Ingestion & Preprocessing**: Reads raw data (CSV), cleans/imputes missing values, and encodes categorical variables.  
3. **Modeling**: Trains a suitable model (e.g., Logistic Regression for PD, XGBoost for LGD) with basic hyperparameter tuning.  
4. **Compliance Check**: Uses an LLM-based chain to query regulation docs and identify potential issues.  
5. **Benchmarking**: Compares new model’s performance against a baseline (e.g., AUC = 0.70).  
6. **Documentation**: Generates a summary of the entire process (performance, compliance status, etc.).  

> **Note**: This is a toy example, **not** production-grade. It's meant to illustrate how you might structure a modular credit risk pipeline with LangChain.

---

## Folder Layout

```
credit_risk_ai_agent/
├─ main.py                    # Entry point (CLI usage)
├─ config.py                  # Configuration & paths
├─ data/
│  └─ example_data.csv        # Sample dataset
├─ knowledge_base/
│  └─ regulations/            # Regulatory text files
├─ modules/
│  ├─ problem_identifier.py   # Identifies PD vs. LGD, etc.
│  ├─ data_ingestion.py       # Loads CSV or DB data
│  ├─ data_preprocessing.py   # Cleans & transforms data
│  ├─ model_builder.py        # Model training & tuning
│  ├─ compliance_checker/     
│  │  ├─ compliance_chain.py  # LLM-based compliance checks
│  │  └─ compliance_utils.py
│  ├─ benchmarking.py         # Compare metrics to baseline
│  └─ documentation.py        # Auto-generate docs
├─ chains/
│  └─ credit_risk_chain.py    # Main LangChain orchestration
├─ models/                    # Folder to store or archive trained models
├─ docs/                      # Output for generated documentation
└─ requirements.txt           # Dependencies
```

---

## Usage

1. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```
   
2. **Run the Agent**:

   ```bash
   python main.py --request "Build a PD model to estimate default probability for auto loans"
   ```
   
   - This runs through problem identification, data ingestion/preprocessing, model building, compliance checking, benchmarking, and documentation.  
   - See console output for final results and check `./docs` for the generated documentation file.

---

## Highlights

- **LangChain** orchestrates each step via a simple chain function.
- **LLM Compliance Check**: Uses a local regulation store + retrieval augmented generation to surface relevant rules.
- **Benchmarking & Documentation**: Automated performance comparisons and text-based report generation.

> For further details, see each module’s docstring or comments. Adjust the example for real-world requirements (security, advanced data pipelines, more robust compliance logic, etc.).