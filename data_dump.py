import pymongo # pip install pymongo
import pandas as pd
import json

client = pymongo.MongoClient("mongodb+srv://roshan1234:roshan12345@cluster0.kkal65f.mongodb.net/?retryWrites=true&w=majority")

DATA_FILE_PATH = (r"C:\Users\rosha\Documents\Projects\Machine learning\end-to-end-InsurancePremiumPredictor\insurance.csv")
DATABASE_NAME = "insurance"
COLLECTION_NAME = "insur_data"


if __name__=="__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and columns: {df.shape}")

    df.reset_index(drop = True, inplace = True)

    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)