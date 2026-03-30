
fp = open("log.txt", "a")

def log(func):
    def wrapper(*args, **kwargs):
        fp.write(f"Volám funkci {func.__name__} s parametry: {args} a {kwargs}\n")
        return func(*args, **kwargs)
    return wrapper

@log
def ahoj(jmeno):
    print(f"Ahoj {jmeno}!")

@log
def cau():
    print("Čau!")

if __name__ == "__main__":
    ahoj("Vlado")
    cau()