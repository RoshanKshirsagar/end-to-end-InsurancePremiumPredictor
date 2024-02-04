from insurance.logger import logging
from insurance.exception import InsuranceException
import os, sys
from insurance.utils import *
from insurance.entity import config_entity
from insurance.entity import artifact_entity
from insurance.components.data_ingestion import DataIngestion


if __name__=="__main__":
    try:
        # get_collection_as_dataframe(database_name="insurance", collection_name="insur_data")
        training_pipeline_config = config_entity.TrainingPipelineConfig()
        
        # data ingestion
        data_ingestion_config  = config_entity.DataIngestionConfig(training_pipeline_config=training_pipeline_config)
        print(data_ingestion_config.to_dict())
        data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
        data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
    except Exception as e:
        print(e)