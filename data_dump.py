import pymongo # pip install pymongo
import pandas as pd
import json
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()
mongo_url = "MONGO_DB_URL"
mongo = os.getenv(mongo_url)

client = pymongo.MongoClient(mongo)

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