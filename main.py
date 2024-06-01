from pipeline import replace_missing_values,execute,insert_csv_line_sqlite,remove_temp_files
import time
if __name__ == "__main__":
    while True:
        try:
            option = int(input("Select a pipeline run option:\n1. Type (1) Run Pipeline on all the datasets\n2. Type (2) Run the pipeline on validation datasets only\n"))
            if option in [1, 2]:
                print(f"You selected option {option}.")
                break
            else:
                print("Invalid option. Please type 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    if option==1:
        raw_data_path = "Data/raw"
        temp_path="Data/temp"
    elif option==2:
        raw_data_path = "Data/validation"
        temp_path="Data/temp"
        
    replace_missing_values(raw_data_path,temp_path)
    sqlite_db_path='database/pragma.db'
    table_name='prices'
    drop_table=f"""drop table if exists {table_name}"""
    execute(drop_table,sqlite_db_path)
    create_table = f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        timestamp DATE,
        price double precision,
        user_id INTEGER
    );
    """
    execute(create_table,sqlite_db_path)
    insert_csv_line_sqlite(temp_path,sqlite_db_path,table_name)
    time.sleep(0.5)
    remove_temp_files(temp_path)

    print ("Data has been inserted, stats summarize ")

    
    select_table=f"""select count(1) from {table_name}"""
    print("Row count in sql database : ")
    execute(select_table ,sqlite_db_path)

    
    select_price_avg=f"""select avg(price) from {table_name}"""
    print("Price Average : ")
    execute(select_price_avg,sqlite_db_path)


    
    select_max_price_=f"""select max(price) from {table_name}"""
    print("Max Price : " )
    execute(select_max_price_,sqlite_db_path)


    
    select_min_price=f"""select min(price) from {table_name}"""
    print("Min Price")
    execute(select_min_price,sqlite_db_path)  

   
    select_min_price=f"""select * from {table_name}"""
    print("Final Query")
    execute(select_min_price,sqlite_db_path)