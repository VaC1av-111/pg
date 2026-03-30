#SINGLETON

class Logger:
    __instance = None

    def __new__(cls, log_file):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
            cls.__instance._log_file = log_file
        return cls.__instance
    
    #def __init__(self, log_file):
    #    self._log_file = log_file

    def log(self, message):
        with open(self._log_file, 'a') as f:
            print(f"zapisuji do souboru {self._log_file}: {message}")
            f.write(message + '\n')

if __name__ == '__main__':
    log1 = Logger("log1.txt")
    log2 = Logger("log2.txt")
    log3 = Logger("log3.txt")

    log1.log('text1')
    log2.log('text2')
    log3.log('text3')