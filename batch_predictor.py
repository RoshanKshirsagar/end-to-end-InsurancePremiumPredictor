from insurance.pipeline.batch_prediction import start_batch_prediction
from insurance.pipeline.training_pipeline import start_training_pipeline

file_path=r"C:\Users\rosha\Documents\Projects\Machine learning\end-to-end-InsurancePremiumPredictor\insurance.csv"
print(__name__)

if __name__=="__main__":
    try:
        output_file = start_batch_prediction(input_file_path=file_path)
        print(output_file)
    except Exception as e:
        print(e)