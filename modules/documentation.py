import datetime
import os
from config import DOCUMENTATION_OUTPUT_PATH

def generate_documentation(user_request, problem_type, performance_metrics, compliance_report, benchmark_report):
    now_str = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    doc_filename = f"ModelDoc_{problem_type}_{now_str}.txt"
    doc_path = os.path.join(DOCUMENTATION_OUTPUT_PATH, doc_filename)
    
    with open(doc_path, "w") as f:
        f.write("CREDIT RISK MODEL DOCUMENTATION\n")
        f.write("--------------------------------\n")
        f.write(f"Request: {user_request}\n")
        f.write(f"Problem Type: {problem_type}\n\n")
        
        f.write("Performance Metrics:\n")
        for k, v in performance_metrics.items():
            f.write(f"  {k}: {v}\n")
        
        f.write("\nCompliance Report:\n")
        for k, v in compliance_report.items():
            f.write(f"  {k}: {v}\n")
        
        f.write("\nBenchmark Report:\n")
        for k, v in benchmark_report.items():
            f.write(f"  {k}: {v}\n")
        
        f.write("\nGenerated on: " + now_str + "\n")
    return doc_path
