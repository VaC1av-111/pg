"""
fronta = []
fronta.append(5)
fronta.append(10)
fronta.append(15)

print (fronta.pop(0))

fronta.append(3)

print (fronta.pop(0))
print (fronta.pop(0))
print (fronta.pop(0))



zasobnik = []
zasobnik.append(5)
zasobnik.append(10)
zasobnik.append(15)

print (zasobnik.pop())

zasobnik.append(3)

print (zasobnik.pop(0))
print (zasobnik.pop(0))
print (zasobnik.pop(0))

"""
"""
def jaccardova_vzadelnost_mnozin(mnozina1, mnozina2):
    mnozina1 = set(mnozina1)
    mnozina2 = set(mnozina2)

    intersection = mnozina1.intersection(mnozina2)
    union = mnozina1.union(mnozina2)
    jindex = len(intersection) / len(union)
    return 1 - jindex

if __name__ == "__main__":
    serp1=["https://example.com/page1", "https://example.com/page7", "https://example.com/page3"]
    serp2=["https://example.com/page4", "https://example.com/page1", "https://example.com/page6"]
    serp3=["https://example.com/page7", "https://example.com/page9", "https://example.com/page9"]

print(jaccardova_vzadelnost_mnozin(serp1, serp2))
print(jaccardova_vzadelnost_mnozin(serp1, serp3))
print(jaccardova_vzadelnost_mnozin(serp2, serp3))
"""

def levensteinova_vzdalenost(dotaz1, dotaz2):
    length = max (len(dotaz1), len(dotaz2))
    i = 0
    levenstein = 0
    while i < length:
        if i < len(dotaz1) and i < len(dotaz2):
            if dotaz1[i] != dotaz2[i]:
                levenstein +=1
        else:
            levenstein +=1
    return levenstein

def levensteinova_vzdalenost_for(dotaz1, dotaz2):
    levenstein = 0
    length = min(len(dotaz1), len(dotaz2))
    for i in range(length):
        if dotaz1[i] != dotaz2[i]:
            levenstein += 1
    levenstein += abs(len(dotaz1) - len(dotaz2))
    return levenstein 
    
    
if __name__ == "__main__":
    query1 = "seznam"
    query2 = "seznamka"
    query3 = "sesnam"
    query4 = "seznam"

    print(levensteinova_vzdalenost(query1, query2))
    print(levensteinova_vzdalenost(query1, query3))  
    print(levensteinova_vzdalenost(query1, query4))  
    print(levensteinova_vzdalenost_for(query2, query3))  