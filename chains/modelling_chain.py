from modules.problem_identifier import identify_problem
from modules.data_ingestion import ingest_data
from modules.data_preprocessing import preprocess_data
from modules.model_builder import train_model, evaluate_model
from modules.compliance_checker.compliance_chain import run_compliance_chain
from modules.benchmarking import benchmark_model
from modules.documentation import generate_documentation

def run_credit_risk_chain(user_request: str, status_callback=None):
    """
    Orchestrates the credit risk modeling flow, 
    reporting status updates via 'status_callback' if provided.
    """
    if status_callback is None:
        # If no callback is passed, define a no-op
        def status_callback(msg): pass

    status_callback("Starting workflow...")

    # 1) Problem Identification
    problem_type = identify_problem(user_request)
    status_callback(f"Identified problem type as: {problem_type}")

    # 2) Data Ingestion
    df = ingest_data()
    status_callback("Data ingestion complete. Loaded dataset.")

    # 3) Data Preprocessing
    df_prep = preprocess_data(df, problem_type)
    status_callback("Data preprocessing complete.")

    # 4) Model Building & Evaluation
    model, performance_metrics = train_model(df_prep, problem_type)
    status_callback(f"Model trained. Performance: {performance_metrics}")

    model_eval = evaluate_model(model, df_prep, problem_type)
    status_callback("Model evaluation complete.")

    # 5) Compliance Check
    compliance_report = run_compliance_chain(model_eval, problem_type)
    status_callback("Compliance check complete.")

    # 6) Benchmarking
    benchmark_report = benchmark_model(performance_metrics, problem_type)
    status_callback("Benchmarking complete.")

    # 7) Documentation
    doc_file = generate_documentation(
        user_request=user_request,
        problem_type=problem_type,
        performance_metrics=performance_metrics,
        compliance_report=compliance_report,
        benchmark_report=benchmark_report
    )
    status_callback(f"Documentation generated at: {doc_file}")

    status_callback("Workflow finished successfully.")

    return {
        "problem_type": problem_type,
        "performance": performance_metrics,
        "compliance": compliance_report,
        "benchmark": benchmark_report,
        "documentation_path": doc_file
    }
