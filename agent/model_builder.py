import pandas as pd
from sklearn.linear_model import LogisticRegression
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, roc_auc_score, mean_squared_error

def train_model(df: pd.DataFrame, problem_type: str):
    if problem_type == "PD":
        if "default_flag" not in df.columns:
            return None, {"error": "No default_flag column found"}
        
        X = df.drop(columns=["default_flag"])
        y = df["default_flag"]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        model = LogisticRegression(max_iter=1000)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        y_prob = model.predict_proba(X_test)[:,1]

        acc = accuracy_score(y_test, y_pred)
        auc = roc_auc_score(y_test, y_prob)
        return model, {"accuracy": acc, "auc": auc}
    
    elif problem_type == "LGD":
        if "lgd" not in df.columns:
            return None, {"error": "No lgd column found"}

        X = df.drop(columns=["lgd"])
        y = df["lgd"]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        model = XGBRegressor(n_estimators=50)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        return model, {"mse": mse}
    
    else:
        return None, {"info": "Unknown problem type"}

def evaluate_model(model, df: pd.DataFrame, problem_type: str):
    # Additional validation / evaluation logic
    return {
        "model_name": str(model),
        "problem_type": problem_type,
        "status": "Evaluated"
    }
