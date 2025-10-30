def precti_hodnoty_a_incrementuj(file):
    all_results = []
    for line in file:
        data = line.split(',')
        result = []
        for value in data:
            value = value.strip()
            try:
                value = int(value)+1 
            except ValueError:
                pass
            result.append(value)
        all_results.append(result)
        return all_results
    
def precti_hodnoty_a_incrementuj2(file):
    data = []
    reader = csv.reader(file)
    for row in reader:
        data.append(row)
    print(data)
    return data

def zapis_do_csv(filen_name, data):
    with open(filen_name, 'w') as file:
        for row in data:
            #row2 = []
            #for value in row:
            #   row2.append(str(value))
            line = ', '.join([str(value) for value in row])
            file.write(line + '\n')
        

if __name__ == "__main__":

    try:
        name = input("Zadejte jemno souboru: ")
        file = open (name, 'r')
        result = precti_hodnoty_a_incrementuj(file)
        file.close()
        file.name = 'xxx'
        zapis_do_csv(file.name, result)
    except FileNotFoundError:
        print(f'Soubor {name} nalezen.')
        

    