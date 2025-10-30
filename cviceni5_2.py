import sys



if __name__ == '__main__':
    
    try:
        file = open ("data.txt", 'r')
        data = file.readline().strip()
        print(data)
    
        """
        data = file.readline()
        print(data)
        """
        file.close()

    except FileNotFoundError as e:
        print(f'Soubor nebyl nalezen: {e}')