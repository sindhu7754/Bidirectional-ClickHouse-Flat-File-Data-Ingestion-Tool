import csv
from clickhouse_driver import Client
from clickhouse_driver.errors import Error

def fetch_data_from_clickhouse(host, port, database, user, jwt_token, query):
    try:
        client = Client(host, port=port, user=user, password=jwt_token, database=database)
        return client.execute(query)
    except Error as e:
        raise Exception(f"Error while connecting to ClickHouse: {e}")
    except Exception as e:
        raise Exception(f"An unexpected error occurred while fetching data from ClickHouse: {e}")

def write_to_flatfile(file_name, data, delimiter=','):
    try:
        with open(file_name, mode='w', newline='') as file:
            writer = csv.writer(file, delimiter=delimiter)
            writer.writerows(data)
    except Exception as e:
        raise Exception(f"Error while writing to flat file: {e}")

def read_from_flatfile(file_name, delimiter=','):
    try:
        with open(file_name, mode='r') as file:
            reader = csv.reader(file, delimiter=delimiter)
            return list(reader)
    except FileNotFoundError:
        raise Exception(f"File '{file_name}' not found.")
    except Exception as e:
        raise Exception(f"An error occurred while reading from the flat file: {e}")

def ingest_flatfile_to_clickhouse(host, port, database, user, jwt_token, file_name, delimiter=','):
    try:
        data = read_from_flatfile(file_name, delimiter)
        client = Client(host, port=port, user=user, password=jwt_token, database=database)
        columns = data[0]
        rows = data[1:]
        query = f"INSERT INTO {database}.table_name ({', '.join(columns)}) VALUES"
        client.execute(query, rows)
        return len(rows)
    except Exception as e:
        raise Exception(f"Error while ingesting flat file to ClickHouse: {e}")
