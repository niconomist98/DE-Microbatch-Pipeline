from pipeline import replace_missing_values,execute,insert_csv_line_sqlite,remove_temp_files,pipeline_run
import time
if __name__ == "__main__":

    ##---------------Run pipeline with all the datasets------------------------
    print("Running pipeline on all the datasets\n")
    time.sleep(3)
    raw_data_path = "Data/raw"
    temp_path="Data/temp"
    sqlite_db_path='database/pragma.db'
    table_name='prices'
    pipeline_run(raw_data_path,temp_path,sqlite_db_path,table_name)
    time.sleep(1)
    print("##########################################")
    ###-------------------Run pipeline on validation dataset-----------------------
    print("Running pipeline on validation  dataset\n")
    time.sleep(3)
    validation_path = "Data/validation"
    validation_table_name='prices_validation'
    pipeline_run(validation_path,temp_path,sqlite_db_path,validation_table_name)
    