import sqlite3
import os
import time 
import csv
import os
import time 
import pandas as pd
import shutil

def remove_temp_files(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)  # This removes directories
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
    
def replace_missing_values(input_folder, output_folder):
    files = [f for f in os.listdir(input_folder) if f.endswith('.csv')]
    for file in files:
        in_file_path = os.path.join(input_folder, file)
        out_file_path=os.path.join(output_folder, file)
        dataset_name = os.path.splitext(file)[0]
        print(in_file_path)
        print(out_file_path)

        print(dataset_name)
        with open(in_file_path, 'r') as infile, open(out_file_path, 'w', newline='') as outfile:
            reader = csv.reader(infile)
            writer = csv.writer(outfile)
            for row in reader:
                # Replace empty strings with '0'
                row = [value if value.strip() else '0' for value in row]
                writer.writerow(row)

def connect_sqlite(path):
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    return conn
    
def close_sqlite(conn):
    conn.close()

def execute(statement,sqlite_db_path):
    conn = sqlite3.connect(sqlite_db_path)
    cursor = conn.cursor()
    query = statement
    cursor.execute(statement)
    conn.commit()
    rows = cursor.fetchall()

    for row in rows:
        print(row)
    conn.close()

   

def insert_csv_line_sqlite(directory_path,sqlite_db_path,table_name):
    conn = sqlite3.connect(sqlite_db_path)
    cursor = conn.cursor()
    files = [f for f in os.listdir(directory_path) if f.endswith('.csv')]
    log_row_count=0
    logs_prices=[]
    for file in files:

        file_path = os.path.join(directory_path, file)
        dataset_name = os.path.splitext(file)[0]
        print(file_path)
        print(dataset_name)
        
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)
            next(csv_reader)
            
            for row in csv_reader:
                query = f'INSERT INTO {table_name} (timestamp, price, user_id) VALUES (?, ?, ?)'
                log_row_count+=1
                logs_prices.append(int(row[1]))  
                print(f"--------------------- row {log_row_count} start---------------------\nStats:\nInserted rows count :  {log_row_count}\nAverage of Price: {sum(logs_prices) /len(logs_prices)}\nMinimun Price: {min(logs_prices)}\nMax Price : {max(logs_prices)}\n--------------------- row {log_row_count} end---------------------\n>>>")
                cursor.execute(query, row)
                time.sleep(0.)
        conn.commit()
    conn.close()