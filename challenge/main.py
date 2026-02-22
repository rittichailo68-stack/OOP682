from log_source import FileLogSource
from csv_log_source import CsvLogSource

def get_log_source(source_type):
    if source_type == "file":
        return FileLogSource()   
    elif source_type == "csv": 
        return CsvLogSource()

if __name__ == "__main__":
    source = get_log_source("csv")
    print("--- Output Log จาก CSV ---")   
    for log in source.get_logs():
        print(log)   