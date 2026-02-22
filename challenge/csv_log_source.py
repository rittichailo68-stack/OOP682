from log_source import ILogSource

class CsvLogSource(ILogSource):    
    def get_logs(self):   
        return ["Log from CSV: user_id, action, status", "Log from CSV: 101, login, success"]  