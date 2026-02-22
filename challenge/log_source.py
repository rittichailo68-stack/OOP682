from abc import ABC, abstractmethod

class ILogSource(ABC):
    @abstractmethod
    def get_logs(self):   
        pass

class FileLogSource(ILogSource):
    def get_logs(self):
        return ["Log from TXT: System Booting", "Log from TXT: Server Started"]  