import sys
from src.CreditPulse.exception import CustomException
from src.CreditPulse.logger import logging
from src.CreditPulse.components.data_ingestion import DataIngestion
from src.CreditPulse.components.data_ingestion import DataIngestionConfig

if __name__=="__main__":
    logging.info("The execution has Started.")

    try:
        #data_ingestion_config=DataIngestionConfig()
        data_ingestion=DataIngestion()
        data_ingestion.initiate_data_ingestion()

    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)
