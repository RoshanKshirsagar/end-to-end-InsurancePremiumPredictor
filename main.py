from insurance.logger import logging
from insurance.exception import InsuranceException
import os, sys
from insurance.utils import *


if __name__=="__main__":
    try:
        get_collection_as_dataframe(database_name="insurance", collection_name="insur_data")
    except Exception as e:
        print(e)