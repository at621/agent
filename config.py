import os

DB_URI = os.getenv("DB_URI", "sqlite:///credit_risk_db.sqlite")
REGULATIONS_PATH = "./knowledge_base/regulations"
DATA_PATH = "./data/example_data.csv"
MODEL_OUTPUT_PATH = "./models"
DOCUMENTATION_OUTPUT_PATH = "./docs"

# Example baseline thresholds
PD_BASELINE_AUC = 0.70
LGD_BASELINE_MSE = 0.10

# Could also store secrets / API keys here
