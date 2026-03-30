class Logger:
    
    _log_file = None

    def _now_(cls, filename):
        if not cls._log_file:
            cls.log_file = super().__new__(cls)
            cls.log_file = open(filename, 'a')
        return cls._log_file
    
    def add(self,message):
        self._log_file.write(message + '\n')

if __name__ == '__main__':
    log1 = Logger("log1.txt")
    log2 = Logger("log2.txt")
    log3 = Logger("log3.txt")

    log1.add('text1')
    log2.add('text2')
    log3.add('text3')
